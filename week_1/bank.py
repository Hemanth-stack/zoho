"""this functions are written to greet the people"""


def main() -> None:
    """the main function"""
    name = input("Greeting: ")
    greet(name)


def greet(name: str) -> str:
    """greeting function takes string as input and return the strings"""
    if name.lower() == "hello":
        value = "$0"
    elif name.lower()[0] == "h":
        value = "$20"
    else:
        value = "$100"
    return value


if __name__ == "__main__":
    main()
