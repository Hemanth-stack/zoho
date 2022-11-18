def convert(s):
    hour, min = map(int, s.split(":"))
    value = hour
    value += min / 60
    return value


def main():
    s = input("what time is")
    v = int(convert(s))
    if v in range(7, 9):
        print("breakfast time")
    elif v in range(12, 2):
        print("lunch time")
    elif v in range(8, 10):
        print("Dinner time")


main()
