'''Karplus-Strong'''
'''Musical overtones'''
'''python mO.py --display to display and python mO.py --play to play.'''

import sys, os
import time, random
import wave, argparse
import numpy as np
from collections import deque
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import pyaudio

gShowPlot = False

pmNotes = {'C4' : 262, 'Eb' : 311, 'F' : 349, 'G' : 391, 'Bb' : 466}

CHUNK = 1024

fig, ax = plt.subplots(1)
line, = ax.plot([],[])

def writeWAVE(fName, data):
    file = wave.open(fName, 'wb')
    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100
    file.setparams((nChannels, sampleWidth, frameRate, nFrames,
                    'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()

def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100
    N = int(sampleRate/freq)

    if gShowPlot:
        ax.set_xlim([0, N])
        ax.set_ylim([-1.0, 1.0])
        line.set_xdata(np.arange(0, N))
    buf = deque([random.random()-0.5 for i in range(N)], maxlen = N)
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        if gShowPlot:
            if i % 1000 == 0:
                line.set_ydata(buf)
                fig.canvas.draw()
                fig.canvas.flush_events()
    samples = np.array(samples * 32767, 'int16')
    return samples.tobytes()

class NotePlayer:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            output=True)
        self.notes = []
    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
    def add(self, filename):
        self.notes.append(filename)
    def play(self, filename):
        try:
            print("playing " + filename)
            wf = wave.open(filename, 'rb')
            data = wf.readframes(CHUNK)
            while data != b'':
                self.stream.write(data)
                data = wf.readframes(CHUNK)
            wf.close()
        except BaseException as err:
            print(f"Exception! {err=}, {type(err)=}.\nExiting")
            exit(0)
    def playRandom(self):
        index = random.randint(0, len(self.notes)-1)
        note = self.notes[index]
        self.play(note)

def main():
    global gShowPlot

    parser = argparse.ArgumentParser(description="Generating sounds with Karplus-Strong Algorithm.")
    parser.add_argument('--display', action = 'store_true', required=False)
    parser.add_argument('--play', action = 'store_true', required=False)
    args = parser.parse_args()
    if args.display:
        gShowPlot = True
        plt.show(block=False)
    
    nplayer = NotePlayer()

    print('Creating notes...')
    for name, freq in list(pmNotes.items()):
        filename = os.path.join('sounds', name + '.wav')

        if not os.path.exists(filename) or args.display:
            data = generateNote(freq)
            print('creating ' + filename + '...')
            writeWAVE(filename, data)
        else:
            print('Filename already created. skipping...')
        nplayer.add(filename)
        time.sleep(0.5)
    if args.play:
        while True:
            try:
                nplayer.playRandom()
                rest  =np.random.choice([1, 2, 4, 8], 1, p=[0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25 * rest[0])
            except KeyboardInterrupt:
                exit(0)
if __name__ == '__main__':
    main()