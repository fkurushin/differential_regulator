import math
import numpy as np

fo = open("f5exp.txt", "w+")

t = np.linspace(0.0, 100.0, num=1000)
print(t)
e = np.exp(t)

for e_, t_ in zip(e, t):
    fo.write(str(t_) + ";" + str(e_) + "\n")

fo.close()

fo = open("f5sin.txt", "w+")

s = [300 + 500 * math.sin(t_*100) for t_ in t]

for s_, t_ in zip(s, t):
    fo.write(str(t_) + ";" + str(s_) + "\n")

fo.close()
