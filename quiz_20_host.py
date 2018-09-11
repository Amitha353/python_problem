import re

fcon = open("hosts_access_log_00.txt", "r")
txt = fcon.read()
fcon.close()
res = re.findall(r"([a-z0-6]+[.][a-z]+[.][a-z]+)\s(- -)", txt)
lst = []
cunt = []
for a in res:
    nex = True
    for b in lst:
        if b == a[0]:
            nex = False
            cunt[lst.index(b)] += 1
    if nex:
        lst.append(a[0])
        cunt.append(1)

fil = open('records_hosts_access_log_00.txt', 'w')
for i in range(len(lst)):
    fil.write(lst[i] + " " + str(cunt[i]) + '\n')

fil.close()
