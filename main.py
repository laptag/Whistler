from pydl.io.Data import Data, FileType
from pydl.analysis import reduceResolution
import matplotlib.pyplot as plt
import matplotlib
from time import sleep

from pydl._analysis.crossCorrelation import _staticCrossCorrelation

i_file = "Data/C1-sweep-00000.txt"
v_file = "Data/C3-sweep-00000.txt"

# i = Data(i_file, filetype=FileType.csv)
v = Data(v_file, filetype=FileType.csv)

sample = v.data[100:1000]
large = 0
large_a = 0
large_b = 0
d = 1

# p = plt.plot(v.data[0:6000])
corr_data = []

i = 1
try:
    while i < int(6000/d)+1:
        a = 100+(d*i)
        b = 1000+(d*i)
        test = v.data[a:b]
        res = _staticCrossCorrelation(reduceResolution(sample, 10), reduceResolution(test, 10))

        if (res > large):
            large = res
            large_a = a
            large_b = b

        corr_data.append(res)
        # plt.title(str(res))

        # if (i == 1):
        #     line, = plt.plot(range(a, b), sample, "g")
        # else:
        #     line.set_data(range(a, b), sample)
        #
        # if (res > 0.95):
        #     print(res, a, b)
        #     line.set_color("r")
        # else:
        #     line.set_color("g")
        #
        # plt.pause(0.01)
        i += 1
except KeyboardInterrupt:
    print("\nKilling")

plt.plot(corr_data)
plt.plot(v.data[0:6000])
plt.show()
plt.close()

print("largest", large, large_a, large_b)
