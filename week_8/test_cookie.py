from cookie import Jar as j


def main():
    test1()
    test2()


def test1():
    assert j.capacity == 12


def test2():
    c = j(8)
    assert j.size == 0


if __name__ == "__main__":
    main()
