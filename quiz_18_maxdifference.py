

def getMexDiff(ary):
    nary = []
    amx = []
    for a in range(1, len(ary)):
        tay = []
        for b in ary[:a]:
            if b < ary[a]:
                tay.append(ary[a] - b)
        nary.append(tay)
        if len(tay) > 0:
	        amx.append(max(tay))
    print(nary)
    print(max(amx))


lst = [3, 4, 5, 8, 9, 3, 2, 5]
getMexDiff(lst)

lst = [2, 3, 10, 2, 4, 8, 1]
getMexDiff(lst)
