
def main()->None:
    s = input('Greeting: ')
    greet(s)

def greet(s:str)->str:
    if s.lower() == 'hello':
        return '$0'
    elif s.lower()[0] == 'h':
        return '$20'
    else:
        return '$100'

if __name__=='__main__':
    main()