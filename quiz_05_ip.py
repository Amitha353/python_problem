import re


def ifip(ip):
    sip = ip.split(":")
    if len(sip) == 8:
        tip = True
        for a in sip:
            if not re.match(r'[0-9a-fA-F]', a):
                tip = False
                break
        if tip:
            print("An IPv6 address")
        else:
            print("Neither an IPv6 address nor an IPv4 address")
    else:
        sip = ip.split(".")
        if len(sip) == 4:
            tip = True
            for a in sip:
                if int(a) > 255:
                    tip = False
            if tip:
                print("An IPv4 address")
            else:
                print("Neither an IPv6 address nor an IPv4 address")
        else:
            print("Neither an IPv6 address nor an IPv4 address")
    print(ip)


ifip("255.234.234.33")
ifip("12:32:84:22:43:23:32:43")
