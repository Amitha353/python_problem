import random
import numpy as np


def slotGenarator(num):
    whe = random.randint(3, 5)
    print(whe)
    lst = []
    for a in range(num):
        spin = ""
        for b in range(whe):
            num = random.randint(1, 9)
            spin += str(num) + " "
        print(spin)
        lst.append(spin.strip())
    findSlotNumber(lst)


def findSlotNumber(ary):
    lst = []
    agn = []
    for a in ary:
        tlt = a.split(" ")
        ntl = []
        for b in tlt:
            ntl.append(int(b))
        ntl = sorted(ntl)
        lst.append(ntl)
    agn = np.array(lst).T.tolist()
    ttl = 0
    for b in agn:
    	ttl += max(b)
    # print(lst)
    print(ttl)


slotGenarator(50)
