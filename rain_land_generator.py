# coding=utf-8
from random import seed, randint
import numpy as np
np.random.seed(2312)
length = 997
max_value = 99
L = []
for i in range(length):
    l = []
    for _ in range(length):
        r = round(np.random.normal(25, 50))
        l.append(abs(r)%max_value)
    L.append(l)
print(L)
with open('land.txt', mode='wt') as f:
    for i in L:
        for j in i:
            f.write(f'{j:2} ')
        f.write('\n')