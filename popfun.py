# popfun.py
import numpy as np


def popc(M, gamma_r):
    pop = []
    m = np.array([x + 1 for x in range(M + 1)])
    denum = sum(1 / ((m) ** gamma_r))

    for c in range(M + 1):
        numen = 1 / ((c + 1) ** gamma_r)
        pop.append(float(numen / denum))
    return pop
