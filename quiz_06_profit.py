
def calculate_profit():
    costPerCut = input()
    salePrice = input()
    lengths = input()
    siz = []
    for x in range(int(lengths)):
        siz.append(int(input()))
    mx = 0
    mpf = 0
    for a in range(1, max(siz)):
    	tc, tp, pof = ck_profit(siz, costPerCut, salePrice, a)
    	if mpf < pof:
            mpf = pof
            mx = a
    print(mx, tc, tp, mpf)


def ck_profit(ary, cpc, sp, cl):
    tp = 0
    tc = 0
    for a in ary:
        b = a
        r = b % cl
        p = int(b / cl)
        c = p - 1
        if r > 0:
            c = p
        tp += p
        tc += c
    pof = tp * int(sp) * cl - tc * int(cpc)
    return tp, tc, pof


calculate_profit()
