x,y,z = input('Expresion: ').split(' ')
x = int(x)
z = int(z)
if y == '+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y == '*':
    print(x*z)
elif y == '/':
    print(x/z)