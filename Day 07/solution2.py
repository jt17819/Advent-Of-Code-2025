import numpy as np


def main():
    with open("Day 07/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 07/data.txt", dtype=str)
    start = 0
    while data[0][start] != "S":
        start += 1
    beams = [0] * len(data[0])
    beams[start] = 1

    for i in range(2,len(data),2):
        new_beams = [0] * len(data[0])
        
        for char in range(len(data[i])):
            if data[i][char] == "^":
                new_beams[char - 1] += beams[char]
                new_beams[char + 1] += beams[char]
            else:
                new_beams[char] += beams[char]
        beams = new_beams

    return sum(beams)


if __name__ == "__main__":
    print(main())
