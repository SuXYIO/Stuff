"""
Show digit distribution of data, and compare to Benford's Law
"""

import csv
import math
from typing import Optional
import argparse as argp


def getFirstDigit(n: int, num_sys: int = 10) -> int:
    if args.num_sys < 2:
        raise ValueError("num_sys must be at least 2")
    while n >= num_sys:
        n //= num_sys
    return n


def readCsv(filename: str, colname: Optional[str] = None) -> list:
    with open(filename, newline="") as csvfile:
        if colname is None:
            return list(csv.reader(csvfile))
        reader = csv.DictReader(csvfile)
        if reader.fieldnames and colname not in reader.fieldnames:
            raise ValueError(f"Column {colname} not found in {reader.fieldnames}")
        return [row[colname] for row in reader if row and row[colname].isdigit()]


def toDistrib(freq: list[int]) -> list[float]:
    if sum(freq) == 0:
        raise ValueError("Frequency cannot be 0")
    return list(map(lambda x: x / sum(freq), freq))


def getDigitDistrib(
    data: list, num_sys: int = 10, skip_invalid: bool = False
) -> list[float]:
    if args.num_sys < 2:
        raise ValueError("num_sys must be at least 2")
    freq = list([0] * (num_sys - 1))
    for row in data:
        for n in row:
            if skip_invalid and not n.isdigit():
                continue
            digit = getFirstDigit(int(n), num_sys)
            if digit == 0:
                continue
            freq[digit - 1] += 1
    return toDistrib(freq)


def benfordDistrib(num_sys: int = 10):
    if num_sys < 2:
        raise ValueError("num_sys must be at least 2")
    for i in range(1, num_sys):
        yield math.log(i + 1, num_sys) - math.log(i, num_sys)


def visualizeDistrib(distrib: list[float], num_sys: int = 10) -> None:
    from matplotlib import pyplot as plt

    if num_sys < 2:
        raise ValueError("num_sys must be at least 2")
    plt.bar(range(1, num_sys), distrib, label="Data")
    plt.plot(
        range(1, num_sys),
        list(benfordDistrib(num_sys)),
        label="Benford",
        color="r",
        marker="x",
    )
    plt.xlabel("First Digit")
    plt.ylabel("Probability")
    plt.title("First Digit Distribution")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argp.ArgumentParser(description="Show digit distribution of CSV data")
    parser.add_argument("filename", type=str, help="CSV filename")
    parser.add_argument(
        "-n", "--num-sys", type=int, default=10, help="Number system, default 10"
    )
    parser.add_argument(
        "-c",
        "--column",
        type=str,
        default=None,
        help="Column name to read, default None",
    )
    parser.add_argument(
        "-s",
        "--skip-invalid",
        action="store_true",
        default=False,
        help="Skip invalid values, default False",
    )
    args = parser.parse_args()
    if args.num_sys < 2:
        raise ValueError("num_sys must be at least 2")

    data = readCsv(args.filename, args.column)
    distrib = getDigitDistrib(data, args.num_sys, args.skip_invalid)
    visualizeDistrib(distrib, args.num_sys)
