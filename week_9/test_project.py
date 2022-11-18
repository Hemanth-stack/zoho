import project as p


def main():
    test1()
    test2()
    test3()


def test1():
    assert p.even_odd(2) == "even"


def test2():
    assert p.even_odd(3) == "odd"


def test3():
    assert p.fibanocci(5) == 5


if __name__ == "__main__":
    main()
