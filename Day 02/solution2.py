# import numpy as np


def main():
    with open("Day 02/data.txt", "r") as file:
        data = file.read().split(",")
    # data = np.loadtxt("Day 02/data.txt", dtype=str)
    # print(data)

    total = 0
    for id_range in data:
        start, end = id_range.split("-")
        for num in range(int(start), int(end) + 1):
            s = str(num)
            if s in (s + s)[1:-1]:
                total += num
    return total


if __name__ == "__main__":
    print(main())
