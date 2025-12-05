# import numpy as np


def main():
    with open("Day 05/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 05/data.txt", dtype=str)
    # print(data)
    fresh_ranges = [r.split("-") for r in data[0].split("\n")]
    fresh_ranges = [[int(r[0]), int(r[1])] for r in fresh_ranges]
    ingredients = data[1].split("\n")
    fresh_ranges.sort(key=lambda x:x[0])

    count = 0
    for ingredient in ingredients:
        ingredient = int(ingredient)
        for r in fresh_ranges:
            if r[0] <= ingredient <= r[1]:
                count += 1
                break

    return count


if __name__ == "__main__":
    print(main())
