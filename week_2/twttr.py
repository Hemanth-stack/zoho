def main():
    s = input('Enter a string ')
    shorten(s)

def shorten(s):
    res = ''
    for i in s:
        if i.lower() not in 'aeiou':
            res+=i
    return res

if __name__ == '__main__':
    main()