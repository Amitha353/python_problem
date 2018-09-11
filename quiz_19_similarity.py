

def checkSimila(nam):
    sim = 0
    for a in range(len(nam)):
        snm = nam[a:]
        if nam.startswith(snm):
            sim += len(snm)
    print(sim)


checkSimila("ababaa")
