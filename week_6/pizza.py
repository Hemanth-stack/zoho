import sys

import pandas as pd
import tabulate


def main():
    if len(sys.argv) == 2:
        menu(sys.argv[1])


def menu(s: str) -> None:
    data = pd.read_csv(s)
    print(tabulate.tabulate(data, headers=data.columns.values, tablefmt="grid"))


if __name__ == "__main__":
    main()
