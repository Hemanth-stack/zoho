l = list()

while True:
    try:
        s = input("Name: ")
        l.append(s)
    except EOFError:
        print()
        res = 'Adieu,adieu,to'
        for i in l[:-1]:
            res += ' '+i+','
        res += ' and '+l[-1]
        print(res)
        break