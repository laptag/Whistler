from pydl.io.Data import Data, FileType
from pydl.analysis import reduceResolution
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.fftpack import fft, ifft
from scipy import signal
from time import sleep

from pydl.analysis import staticCorrelation, extrema, lowFreqFilter

i_file = "Data/C1-sweep-00000.txt"
v_file = "Data/C3-sweep-00000.txt"

i_struct = Data(i_file, filetype=FileType.csv)
v_struct = Data(v_file, filetype=FileType.csv)

v = lowFreqFilter(v_struct.data, sigma=666, test_filter=False)
# v = v_struct.data[0:6000]
u = 300
l = 600
sample = v[u:l]
# plt.plot(v_struct.data[0:6000], "y")
# plt.plot(sample, "r")

d = 10

# p = plt.plot(v[0:6000], "r")
corr_data = []

i = 1
try:
    array = np.concatenate((v, np.zeros(l-u)))
    while i < len(v)+1:
    # while i < 6001:
        a = 0+(i)
        b = abs(u-l)+(i)
        test = array[a:b]

        res = staticCorrelation(sample, test)

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
        # if (res < 0.1):
        #     # print(res, a, b)
        #     line.set_color("g")
        # else:
        #     line.set_color("r")

        i += 1
except KeyboardInterrupt:
    print("\nKilling")

# plt.plot(corr_data, "g")
# plt.plot(100 * np.diff(lowFreqFilter(corr_data[0:6000])), "r")

xs = extrema(corr_data, threshold=(None, 0.1))
print(xs)

l = len(sample)
rs = []
print(l)
for x in xs:
    if x < 0: # minimum
        # plt.plot(abs(x), v[abs(x)], "co")
        # plt.plot(abs(x)+l, v[abs(x)+l], "bo")
        rs.append((abs(x), abs(x)+l))

import csv
p = 0
r = rs[18]
print(r)
plt.plot((i_struct.data[r[0]-550:r[1]+550]))
plt.show()
plt.close()
# for r in rs:
#     plt.plot((i_struct.data[r[0]:r[1]]))
#     plt.show()
#     plt.close()

# plt.plot(v[r[0]:r[1]], -i_struct.data[r[0]:r[1]], "g")
# plt.plot(v[r[0]:r[1]], -np.log(i_struct.data[r[0]:r[1]]), "b")

# a = []
# for val in i_struct.data[550:650]:
#     print(np.log(val), val)
#     a.append(np.log(val))
#
# plt.plot(a, "g")
# plt.plot(i_struct.data[400:600])
# plt.plot(np.log(a), ".")

#
# name = "devil{}.csv".format(p)
# with open(name, "w") as csvfile:
#     writer = csv.writer(csvfile)
#
#     for i in range(len(i_struct.data[r[0]:r[1]])):
#         writer.writerow([i_struct.data[r[0]+i]])
#
#     print("wrote file {}".format(p))

# plt.plot(np.arange(100))

# plt.plot(a)
# plt.plot(np.log(a))

# i = 0

# for r in rs:
#     fig.clear()
#     plt.title("{}: {}".format(i, r[0]))
#
#     if i == 0:
#         # v_line, = plt.plot(v[r[0]:r[1]], "r")
#         # i_line, = plt.plot(i_struct.data[r[0]:r[1]], "b")
#         line, = ax.plot(i_struct.data[r[0]:r[1]], v[r[0]:r[1]], "g")
#         plt.pause(0.1)
#     else:
#         # v_line.set_data(v[r[0]:r[1]])
#         # i_line.set_data(i_struct.data[r[0]:r[1]])
#         line.set_data(i_struct.data[r[0]:r[1]], v[r[0]:r[1]])
#         plt.pause(0.1)
#
#     i += 1
#     fig.canvas.draw()
