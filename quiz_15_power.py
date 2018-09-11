import math


def powerNumber(i, r):
    lst = []
    pw = int(math.sqrt(r))
    if pw < 2:
        pw = 2
    for x in range(0, int(math.sqrt(r)) + 1):
        for y in range(x, int(math.sqrt(r)) + 1):
            for o in range(2, pw + 1):
                for p in range(2, pw + 1):
                    if x <= 1:
                        o = 2
                    if y <= 1:
                        p = 2
                    z = math.pow(x, o) + math.pow(y, p)
                    if z >= i and z <= r:
                        lst.append([z, x, o, y, p])
    # print(i, r)
    nlst = []
    for x in lst:
        nxt = True
        for y in nlst:
            if y == x:
                nxt = False
        if nxt:
            nlst.append(x)
            print(x)


powerNumber(0, 1)
powerNumber(25, 30)
