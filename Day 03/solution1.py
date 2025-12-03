# import numpy as np


def main():
    with open("Day 03/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 03/data.txt", dtype=str)
    # print(data)

    total = 0
    for line in data:
        joltage = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                joltage = max(joltage, int(line[i] + line[j]))
        total += joltage

    return total


if __name__ == "__main__":
    print(main())
