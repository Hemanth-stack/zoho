def main():
    s = input('Fraction : ')
    x,y = convert(s)
    print(gauge(x,y))

def convert(s:str)->tuple:
    x,y = map(int,s.split('/'))
    return (x,y)

def gauge(x:int,y:int)->str:
    if y != 0 and  x<=y:
        value = round((x/y)*100)
    elif y == 0:
        raise ZeroDivisionError
    elif x>y:
        raise ValueError
    if value == 0:
        return 'E'
    elif value == 100:
        return 'F'
    else:
        return f'{value}%'

if __name__ == '__main__':
    while True:
        try:
            main()
        except:
            pass
        else:
            break