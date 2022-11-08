import random as r


def main():
    v = get_level()
    generate_integer(v)

def get_level():
    while True:
        try:
            n = int(input('Level: '))
            return n
        except:
            pass


def generate_integer(level):
    score = 0
    for i in range(10):
        x = r.randint(0,10)
        y = r.randint(0,10)
        res = x+y
        ans = 0
        mis = 0
        while ans != res:
            print(f'{x} + {y} = ',end='')
            ans = int(input())
            mis += 1
            if mis == 3:
                print(f'{x} + {y} = {res}')
                miss = 0
                break
            if mis == 1:
                score += 1
                miss = 0
    print(f'score {score}')

        
            


if __name__ == "__main__":
    main()