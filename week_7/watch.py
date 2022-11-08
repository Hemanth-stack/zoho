import sys

def main():
    s = input("HTML : ")
    return parse(s)


def parse(s):
    new = ''
    for i in range(len(s)):
        if s[i] == '"':
            for j in range(i+1,len(s)):
                if s[j] == '\"':
                    break
                new+=s[j]
            break
    return new

if __name__=='__main__':
    print(main())