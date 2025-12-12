# import numpy as np


def main():
    with open("Day 12/data.txt", "r") as file:
        data = file.read().split("\n\n")
    # data = np.loadtxt("Day 12/data.txt", dtype=str)
    # print(data)
    areas = data.pop()
    shapes = {}
    for shape in data:
        idx = int(shape.split(":")[0])
        size = shape.count("#")
        shapes[idx] = size

    total = 0
    for area in areas.split("\n"):
        area, req = area.split(": ")
        req = list(map(int, req.split(" ")))
        area = list(map(int, area.split("x")))
        
        req_area = sum(req[i] * shapes[i] for i in range(len(req)))
        total += req_area < (area[0] * area[1])

    return total


if __name__ == "__main__":
    print(main())
