import sys

sys.path.insert(1, "/home/local/ZOHOCORP/hemanth-pt6518/Desktop/vs/week_2")

from twttr import shorten


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert shorten("twitter") == "twttr"


def test_2():
    assert shorten("hemanth") == "hmnth"


def test_3():
    assert shorten("chennai") == "chnn"


if __name__ == "__main__":
    main()
