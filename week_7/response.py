import validators

def main():
    return valid(input('enter ur email'))

def valid(s):
    return validators.email(s)

if __name__ == '__main__':
    print(main())