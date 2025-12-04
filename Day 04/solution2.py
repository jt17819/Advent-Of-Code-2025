import numpy as np


def main():
    with open("Day 04/data.txt", "r") as file:
        data = file.read().split("\n")
    data = np.array([[char for char in line] for line in data])
    # print(data)

    total = 0
    prev = None
    while prev != total:
        prev = total
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == "@":
                    if count_neighbours(row, col, data) < 4:
                        total += 1
                        data[row][col] = "."
    return total


def count_neighbours(y, x, grid):
    max_y, max_x = len(grid) - 1, len(grid[0]) - 1
    top = y == 0
    bottom = y == max_y
    left = x == 0
    right = x == max_x
    count = 0

    if not top:
        count += grid[y - 1][x] == "@"
        if not left:
            count += grid[y - 1][x - 1] == "@"
        if not right:
            count += grid[y - 1][x + 1] == "@"
    if not bottom:
        count += grid[y + 1][x] == "@"
        if not left:
            count += grid[y + 1][x - 1] == "@"
        if not right:
            count += grid[y + 1][x + 1] == "@"
    if not left:
        count += grid[y][x - 1] == "@"
    if not right:
        count += grid[y][x + 1] == "@"

    return count


if __name__ == "__main__":
    print(main())
