

def sumUp(x, y):
    spx = x.split("/")
    spy = y.split("/")
    gc = gcd(int(spx[1]), int(spy[1]))
    low = int(int(spx[1]) * int(spy[1]) / gc)
    upr = (int(spx[0]) * low / int(spx[1])) + (int(spy[0]) * low / int(spy[1]))
    ngc = gcd(upr, low)
    print(str(upr/ngc) + "/" + str(low/ngc))


def gcd(x, y):
    gc = y
    if x > y:
        z = x % y
        if z != 0:
            gc = gcd(y, z)
    else:
        z = y % x
        if z != 0:
            gc = gcd(x, z)
        else:
            gc = x
    return gc


sumUp('2/3', '5/6')
sumUp('722/148','360/176')
sumUp('978/1212','183/183')
sumUp('358/472','301/417')
sumUp('780/309','684/988')
sumUp('258/840','854/686')