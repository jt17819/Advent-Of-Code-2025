# import numpy as np


def main():
    with open("Day 06/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 06/data.txt", dtype=str)
    # print(data)
    operations = [op for op in data.pop().split(" ") if op]
    vals = [int(num) for num in data[0].split(" ") if num]
    for line in data[1:]:
        line = [int(num) for num in line.split(" ") if num]
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    vals[i] += line[i]
                case "*":
                    vals[i] *= line[i]
    return sum(vals)


if __name__ == "__main__":
    print(main())
