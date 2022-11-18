import sys

sys.path.insert(1, "/home/local/ZOHOCORP/hemanth-pt6518/Desktop/vs/week_2")

from plates import is_valid


def main():
    test1()
    test2()
    test3()
    test4()


def test1():
    assert is_valid("AA78") == True


def test2():
    assert is_valid("A234A") == False


def test3():
    assert is_valid("fffgg234") == False


def test4():
    assert is_valid("ASD43") == True


if __name__ == "__main__":
    main()
