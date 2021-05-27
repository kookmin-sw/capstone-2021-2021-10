import spliter, mfcc_ext, knn_recommend, yt_search
import os
import time
from flask import Flask, render_template, redirect, request, url_for
from flask import send_from_directory
from flask import send_file
from werkzeug.utils import secure_filename
from pytube import YouTube


app = Flask(__name__)

TITLE = ""
THUMB = ""
STEMS = ""
@app.route('/')
@app.route('/<link>')
def inputTest(link=None):
    return render_template('main.html', link=link)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/recommendation')
def recommendation():
    global TITLE
    fileName = TITLE
    sessions = ['drums', 'bass', 'piano', 'other']
    mfcc = mfcc_ext.getMfcc(f"../seperated_audio/{fileName}")
    titles = [ t.strip() for t in open("titles.txt", "r")]
    reco = []
    print(len(titles))
    for i, sess in enumerate(sessions):
        reco.append(knn_recommend.get_recommend(sess, mfcc[i], fileName, titles))

    # with open("titles.txt", "a") as t:
    #     t.write(f"{fileName}\n")
    #     t.close()
    #print(reco)
    thumb_urls, video_urls = yt_search.get_thumbs(reco)
    print(thumb_urls)
    return render_template('Recommendation.html', fileName = fileName, reco = reco, thumb_urls=thumb_urls, video_urls= video_urls)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/getLink', methods=['POST'])
def getLink(link=None):
    if request.method == 'POST':
        temp = 'succ'
        yt = YouTube(request.form['link'])
        yt.streams.filter(only_audio=True).first().download("../audio")
        global THUMB
        THUMB= yt.thumbnail_url
        global STEMS
        STEMS = request.form.get('stems')
        fileName = spliter.split(yt.title)
    else:
        temp = None
    return redirect(url_for('down', title=fileName))

@app.route('/upload_file', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        fileName=os.path.splitext(f.filename[:-4])
        fileName=fileName[0]
        f.save(f'../audio/{fileName}.mp4')
        global THUMB
        THUMB=""
        global STEMS
        STEMS = request.form.get('stems')
        fileName = spliter.split(fileName)
        return redirect(url_for('down', title=fileName))

@app.route('/seperate_done/<title>')
def down(title=None):
    fileName = title
    global TITLE
    TITLE = fileName
    global STEMS, THUMB
    return render_template('download.html', fileName=fileName, stems=STEMS, thumb= THUMB)

@app.route('/download',  methods=['GET','POST'])
def download():
    source = request.form["source"]
    if source == 'MR' : source = 'accompaniment'
    global TITLE
    fileName = TITLE
    file_name = f"../seperated_audio/{fileName}/{source}.wav"
    return send_file(file_name,
                      mimetype='wav',
                      attachment_filename=f'{fileName}_{source}.wav',
                      as_attachment=True)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
