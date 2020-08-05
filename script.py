import sys
import math
import numpy as np
import os
import array as arr

M = list(range(1, 1000))
z = list(range(1, 1000))

zipf_exp = 0.6
fre = np.empty((1, M))

for file_index in M:
    numen = 1 / file_index ** zipf_exp
    denum = sum(1 / (z ** zipf_exp))
    fre[file_index - 1] = numen / denum

print(fre)


# frequency_i = (1/(file_index^zipf_exp))/sum( 1/(z^(zipf_exp)))

# print(sum(1 / (z ** (zipf_exp))))
