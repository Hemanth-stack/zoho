import random as r

while True:
    try:
        n = int(input('Level: '))
        rand = r.randint(1,n)
        guess = int(input('Guess: '))
        if rand == guess:
            print('Just right!')
        elif rand <guess:
            print('Too small!')
        else:
            print('Just right!')
        break
    except:
        pass