import numpy
import librosa, librosa.display
import sys
import os
from tqdm import tqdm

dirname = "/Volumes/외장하드/wavFile/other/"
files = os.listdir(dirname)

titles = ""

for file in tqdm(files):
    file_path = os.path.join(dirname, file)

    sig, sr = librosa.load(file_path, sr= None)


    hop_length = len(sig)//199
    n_fft = int(round(hop_length * 1.5))
    
    MFCCs = librosa.feature.mfcc(sig, sr, n_fft = n_fft,hop_length=hop_length, n_mfcc=10)
    if MFCCs.shape[1] != 200: continue
    
   # titles += file[:-10] + "\n"
    for line in MFCCs:
        for each in line: print(each, end = " ")

    print()
    sys.stdout.flush()

# f = open('bass_titles', 'w')
# f.write(titles)
# f.close
