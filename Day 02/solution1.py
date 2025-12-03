# import numpy as np


def main():
    with open("Day 02/data.txt", "r") as file:
        data = file.read().split(",")
    # data = np.loadtxt("Day 02/data.txt", dtype=str)
    # print(data)

    max_pattern_length = 6
    patterns = range(10 ** max_pattern_length)
    
    total = 0
    for id_range in data:
        start, end = id_range.split("-")
        start = int(start)
        end = int(end)
        i = 0
        while i < len(patterns):
            num = int(str(patterns[i]) * 2)
            if num > end:
                break
            if start <= num:
                total += num
            i += 1
    return total


if __name__ == "__main__":
    print(main())
