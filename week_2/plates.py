def main() -> None:
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    flag = True
    if s[0].isalpha() and s[1].isalpha():
        flag = True
    else:
        flag = False
        return flag
    if len(s) not in range(2, 6):
        flag = False
        return flag

    l = 0

    for i in s[::-1]:
        if i in "0123456789":
            l += 1

    for i in s[:l]:
        if i in "0123456789":
            flag = False
            return flag

    if s[l] == "0":
        flag = False
        return flag

    for i in s:
        if i in ".,/!@#$%^&*()_+=-:;~`":
            flag = False
            return flag

    return True


if __name__ == "__main__":
    main()
