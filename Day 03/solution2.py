# import numpy as np


def main():
    with open("Day 03/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 03/data.txt", dtype=str)
    # print(data)

    total = 0
    for line in data:
        p = 0
        l = len(line)
        num_digits = 12
        curr = 0
        joltage = ""
        while curr < num_digits:
            vals = line[p : l - num_digits + 1 + curr]
            m = 0
            for i in range(len(vals)):
                m = i if vals[m] < vals[i] else m
            joltage += vals[m]
            p += m + 1
            curr += 1
        total += int(joltage)

    return total


if __name__ == "__main__":
    print(main())
