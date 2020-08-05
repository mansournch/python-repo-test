import sys
import math
import numpy as np
import os
import array as arr

M, gamma_r = 1000, 0.8
pop = []
m = np.array([x + 1 for x in range(M + 1)])
denum = sum(1 / ((m) ** gamma_r))

for c in range(M + 1):
    numen = 1 / ((c + 1) ** gamma_r)
    pop.append(float(numen / denum))

print(sum(pop))


# print(fre)


# frequency_i = (1/(file_index^zipf_exp))/sum( 1/(z^(zipf_exp)))

# print(sum(1 / (z ** (zipf_exp))))
