def main():
    n = int(input('Enter a number : '))
    print(even_odd(n))
    n = int(input('enter number to find fibonaci : '))
    print(fibanocci(n))

def even_odd(n):
    if n%2 == 0:
        return 'even'
    else:
        return 'odd'

def fibanocci(n):
    f,f1 = 0,1
    for i in range(n):
        f2 = f1+f
        f,f1 = f1,f2
    return f

if __name__ == '__main__':
    main()