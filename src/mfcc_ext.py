import numpy
import librosa
import os

def extract(file):

    sig, sr = librosa.load(file, sr= None)

    hop_length = len(sig)//199
    n_fft = int(hop_length * 1.5)

    MFCCs = librosa.feature.mfcc(sig, sr, n_fft = n_fft, hop_length=hop_length, n_mfcc=10)
    return MFCCs.reshape(-1)

def getMfcc(path):
    ret = []
    sessions = ['drums', 'bass', 'piano', 'other']
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        ret.append(extract(file_path))

    return ret
    
if __name__ == '__main__':
    extract("../seperated_audio/drums.wav")