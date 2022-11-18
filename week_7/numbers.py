import re
import sys


def main():
    return validate(input("IP Address : "))


def validate(s):
    try:
        v = list(map(int, s.split(".")))
    except:
        return False
    for i in v:
        if i not in range(0, 256):
            return False
    return True


if __name__ == "__main__":
    print(main())
