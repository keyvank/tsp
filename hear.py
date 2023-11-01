import sys, struct
import cmath
from numpy.fft import fft

def get():
    return struct.unpack("h", sys.stdin.buffer.read(2))[0] / 32767


def put(x):
    sys.stdout.buffer.write(struct.pack("h", int(x * 32767)))

SAMPLE_COUNT = 8192
SAMPLE_RATE = 44100


def freqs(x):
    return [abs(v) for v in fft(samples)][: len(x) // 2]

def argmax(x):
    ind = 0
    mx = 0
    for i, v in enumerate(x):
        if v > mx:
            mx = v
            ind = i
    return ind

while True:
    samples = [get() for _ in range(SAMPLE_COUNT)]
    ff= freqs(samples)

    ran440 = int(440/SAMPLE_RATE*SAMPLE_COUNT)
    ran660 = int(660/SAMPLE_RATE*SAMPLE_COUNT)

    
    com440 = sum(ff[ran440 - 3:ran440+3])
    com660 = sum(ff[ran660 - 3:ran660+3])
    print(com440, com660)
    if com440 > 10000 and com660 < 1000:
    #    print(0)
    #elif com660 > 10000 and com440 < 1000:
    #    print(1)
