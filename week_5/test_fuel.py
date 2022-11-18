import sys

sys.path.insert(1, "/home/local/ZOHOCORP/hemanth-pt6518/Desktop/vs/week_3")

from fuel import convert, gauge


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


def test1():
    assert convert("4/5") == (4, 5)


def test2():
    assert gauge(7, 8) == "88%"


def test3():
    assert gauge(2, 4) == "50%"


def test4():
    assert gauge(0, 7) == "E"


def test5():
    assert gauge(4, 4) == "F"


if __name__ == "__main__":
    main()
