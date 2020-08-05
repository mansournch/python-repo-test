import sys
import math
import numpy as np
import os
import array as arr


##########################
M = np.zeros((1000))
Z = np.zeros((1000))
zipf_exp = 0.6
fre = np.zeros((1000))

for file_index in range(1000):
    numen = 1 / ((file_index + 1) ** zipf_exp)
    denum = sum(1 / ((Z + 1) ** zipf_exp))
    fre[file_index] = numen / denum

print(fre)
print(sum(fre))


# frequency_i = (1/(file_index^zipf_exp))/sum( 1/(z^(zipf_exp)))

# print(sum(1 / (z ** (zipf_exp))))
