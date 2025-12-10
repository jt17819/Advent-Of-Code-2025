# import numpy as np


def main():
    with open("Day 09/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 09/data.txt", dtype=str)
    data = [list(map(int, line.split(","))) for line in data]
    # print(data)

    max_size = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            x = abs(data[i][0] - data[j][0]) + 1
            y = abs(data[i][1] - data[j][1]) + 1
            max_size = max(max_size, x * y)

    return max_size


if __name__ == "__main__":
    print(main())
