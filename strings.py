strg = input("Enter a string: ")
strg = strg.lower()  

i = 0
while i < len(strg):
    c = strg[i]

    if c != ' ':
        frequency = strg.count(c)
        if strg[:i].count(c) == 0:
            print(f"{c}: {frequency}")

    i += 1
