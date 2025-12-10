# import numpy as np


def main():
    with open("Day 09/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 09/data.txt", dtype=str)
    data = [tuple(map(int, line.split(","))) for line in data]
    # print(data)
    perimeter, sizes = get_perimeter(data)
    sizes.sort(reverse=True)
    perimeter.sort(reverse=True, key=lambda p: get_size(*p[0], *p[1]))
    
    for size, (x1, y1), (x2, y2) in sizes:
        if y1 > y2:
            y1, y2 = y2, y1
        if not any (
            (x4 > x1 and x3 < x2 and y4 > y1 and y3 < y2)
            for (x3, y3), (x4, y4) in perimeter
        ):
            return size


def get_perimeter(points):
    edges = []
    sizes = []
    for i in range(len(points)):
        line = (points[i], points[i - 1])
        edges.append(sorted(line))
        for j in range(i + 1, len(points)):
            e1, e2 = sorted((points[i], points[j]))
            sizes.append((get_size(*e1, *e2), e1, e2))

    return edges, sizes


def get_size(x1, y1, x2, y2):
        x = abs(x1 - x2) + 1
        y = abs(y1 - y2) + 1
        return x * y


if __name__ == "__main__":
    print(main())
