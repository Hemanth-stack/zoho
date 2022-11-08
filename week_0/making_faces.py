def convert(s):
    str(s).replace(':)','🙂')
    str(s).replace(':(','😟')
    str(s).replace(':|','😑')
    print(s)
    return s

def main():
    s = input()
    print(convert(s))

main()