# import numpy as np


def main():
    with open("Day 05/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 05/data.txt", dtype=str)
    # print(data)
    fresh_ranges = [r.split("-") for r in data[0].split("\n")]
    fresh_ranges = [[int(r[0]), int(r[1])] for r in fresh_ranges]
    # ingredients = data[1].split("\n")
    fresh_ranges.sort()
    pointer = 0
    total = 0

    while pointer < len(fresh_ranges):
        start = fresh_ranges[pointer][0]
        end = fresh_ranges[pointer][1]
        while pointer < len(fresh_ranges) - 1 and end >= fresh_ranges[pointer + 1][0]:
            pointer += 1
            end = max(end, fresh_ranges[pointer][1])
        total += end - start + 1
        pointer += 1

    return total


if __name__ == "__main__":
    print(main())
