from pydl.io.Data import Data, FileType
from pydl.analysis import reduceResolution
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.fftpack import fft, ifft
from scipy import signal
from time import sleep

from pydl.analysis import staticCrossCorrelation, extrema, lowFreqFilter

i_file = "Data/C1-sweep-00000.txt"
v_file = "Data/C3-sweep-00000.txt"

i = Data(i_file, filetype=FileType.csv)
v = Data(v_file, filetype=FileType.csv)

sample = lowFreqFilter(v.data[100:1000])
large = 0
large_a = 0
large_b = 0
d = 10

p = plt.plot(lowFreqFilter(v.data[0:6000]))
plt.plot(lowFreqFilter(i.data[0:6000], sigma=25))
corr_data = []

i = 1
try:
    while i < 6001:
        a = 100+(i)
        b = 1000+(i)
        test = lowFreqFilter(v.data[a:b])
        res = staticCrossCorrelation(sample, test)

        if (res > large):
            large = res
            large_a = a
            large_b = b

        corr_data.append(res)
        # plt.title(str(res))
        #
        # if (i == 1):
        #     line, = plt.plot(range(a, b), sample, "g")
        #     corr_line, = plt.plot(corr_data)
        #     plt.pause(0.0001)
        # elif (i % d == 0):
        #     line.set_data(range(a, b), sample)
        #     corr_line.set_data(range(len(corr_data)), corr_data)
        #     plt.pause(0.0001)
        #
        # if (res > 0.95):
        #     # print(res, a, b)
        #     line.set_color("r")
        # else:
        #     line.set_color("g")

        i += 1
except KeyboardInterrupt:
    print("\nKilling")

print("largest", large, large_a, large_b)

# plt.plot(corr_data, "g")
# plt.plot(100 * np.diff(lowFreqFilter(corr_data[0:6000])), "r")

# xs = extrema(corr_data[0:6000])
# print(xs)
#
# for x in xs:
#     if x < 0: # minimum
#         plt.plot(abs(x), corr_data[abs(x)], "co")


plt.show()
plt.close()
