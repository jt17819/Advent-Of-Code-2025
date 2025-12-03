import numpy as np, re


def main():
    with open("Day 01/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 01/data.txt", dtype=str)
    # print(data)

    pointer = 50
    count = 0
    for i in range(len(data)):
        sign, num = re.findall("([R,L])(.*)", data[i])[0]
        if sign == "L":
            old = pointer
            pointer -= int(num)
            if pointer <= 0:
                if old > 0:
                    count += 1
                count += abs(pointer) // 100
                pointer %= 100
        if sign == "R":
            pointer += int(num)
            if pointer >= 100:
                count += pointer // 100
                pointer %= 100

    return count


if __name__ == "__main__":
    print(main())
