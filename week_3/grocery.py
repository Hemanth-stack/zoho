l = list()

while True:
    try:
        l.append(input().upper())
    except EOFError:
        for v in sorted(set(l)):
            print(f'{l.count(v)} {v}')