# import numpy as np


def main():
    with open("Day 03/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 03/data.txt", dtype=str)
    # print(data)

    total = 0
    for line in data:
        joltage = [0] * 12
        for i in reversed(range(len(line))):
            val = line[i]
            for j in joltage:
                if joltage[j] < val:
                    val, joltage[j] = joltage[j], val
                joltage = max(joltage, int(line[i] + line[j]))
        total += joltage

    return total


if __name__ == "__main__":
    print(main())
