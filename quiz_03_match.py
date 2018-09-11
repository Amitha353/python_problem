

def matchMe(x, p, s):
    c = 0
    d = 0
    for a in reversed(range(len(p))):
        if x.startswith(p[a:]):
            c = len(p[a:])
    for a in range(len(s)):
        if x.endswith(s[:a]):
            d = len(s[:a])

    print(c + d)


a = "nothing"
b = "bruno"
c = "ingenious"
matchMe(a, b, c)
