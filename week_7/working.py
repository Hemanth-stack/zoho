import re
import sys


def main():
    return convert(input("Hours: "))


def convert(s):
    try:
        am, pm = s.split("to")
        am = list(am.strip().split(" "))[0]
        pm = list(pm.strip().split(" "))[0]
        try:
            am = int(am)
            pm = int(pm)
        except:
            am = int(list(am.split(":"))[0])
            pm = int(list(pm.split(":"))[0])
        # print(am,pm)
    except:
        sys.exit()
    pm += 12
    am = str(am).zfill(2)
    pm = str(pm).zfill(2)
    return f"{am}:00 to {pm}:00"


if __name__ == "__main__":
    print(main())
