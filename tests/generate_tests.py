import math


fo = open("f5exp.txt", "w+")

for i in range(100):
    e = math.exp(i)
    fo.write(str(i) + ";" + str(e) + "\n")

fo.close()

fo = open("f5sin.txt", "w+")

for i in range(100):
    s = 300 + 900 * math.sin(i)
    fo.write(str(i) + ";" + str(s) + "\n")

fo.close()