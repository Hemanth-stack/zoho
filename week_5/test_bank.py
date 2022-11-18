import sys

sys.path.insert(1, "/home/local/ZOHOCORP/hemanth-pt6518/Desktop/vs/week_1")

from bank import greet


def main():
    test_1
    test_2
    test_3
    test_4


def test_1():
    assert greet("hello") == "$0"


def test_2():
    assert greet("Hemanth") == "$20"


def test_3():
    assert greet("mental") == "$100"


def test_4():
    assert greet("hi") == "$20"


if __name__ == "__main__":
    main()
