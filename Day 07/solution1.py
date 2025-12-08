import numpy as np


def main():
    with open("Day 07/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 07/data.txt", dtype=str)
    data = np.array([[char for char in line] for line in data])
    # print(data)
    start = np.where(data=="S")
    beams = set(start[1])
    count = 0
    for i in range(2,len(data),2):
        new_beams = set()
        for b in beams:
            if data[i][b] == "^":
                new_beams.add(b - 1)
                new_beams.add(b + 1)
                count += 1
            else:
                new_beams.add(b)
        beams = new_beams

    return count


if __name__ == "__main__":
    print(main())
