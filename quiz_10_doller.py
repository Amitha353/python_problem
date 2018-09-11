

def collectMoney(m, n):
    ts = 0
    nts = 0
    mat = False
    for a in range(1, m + 1):
        if ts != n:
            ts += a
            mat = True
    if mat:
        for a in range(2, m + 1):
            if nts != n:
                nts += a
    if ts > nts:
        print(ts)
    else:
        print(nts)
    print(ts, nts)


collectMoney(6, 15)
