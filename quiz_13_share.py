

def checkProfits(mins):
    share = 0
    profit = 0
    buy = 0
    pric = mins.split(" ")
    spri = []
    bpri = []
    prf = [0]
    for a in range(1, len(pric)):
        spri.append((a) * int(pric[a]))
        bpri.append(int(pric[a - 1]))
    for a in range(len(spri)):
        prf.append(spri[a] - bpri[a])
    for a in range(1, len(prf)):
        if int(prf[a - 1]) < int(prf[a]):
            if int(pric[a - 1]) < int(pric[a]):
                share += 1
                buy += int(pric[a - 1])

        else:
            profit += int(pric[a - 1]) * share
            share = 0
    profit += share * int(pric[len(pric) - 1]) - buy
    print(share, profit)


checkProfits("5 3 2")
checkProfits("1 2 100")
checkProfits("1 3 1 2")
