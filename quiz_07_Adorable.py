import re


def checkAdorable():
    lengths = input()
    for x in range(int(lengths)):
        str = input()
        if re.match(r'([a-z])([0]+|[a-z]+|[0-9]+|[:]+)([\/])([a-z]+|[0-9]+)[\\]([a-z]+)', str):
	        print("Its Adorable word")


checkAdorable()

