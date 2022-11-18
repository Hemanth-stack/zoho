import datetime as dt
import sys

import num2words as nw


def main():
    try:
        s = input("date of birth ")
        year, month, day = map(int, s.split("-"))
        date = dt.datetime(year, month, day)
    except:
        sys.exit()
    value = cal_min(date)
    return to_word(value)


def cal_min(date: str) -> float:
    today = dt.datetime.today()
    interval = today - date
    return int(interval.total_seconds() / 60)


def to_word(value: int) -> str:
    return nw.num2words(value, ordinal="numbers")


if __name__ == "__main__":
    print(f"{main()} minutes")
