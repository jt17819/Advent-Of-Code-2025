import numpy as np, re


def main():
    with open("Day 01/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 01/data.txt", dtype=str)
    # print(data)

    sign_map = {"L": -1, "R": 1}
    start = 50
    count = 0
    for i in range(len(data)):
        sign, num = re.findall("([R,L])(.*)", data[i])[0]
        data[i] = (sign_map[sign] * int(num)) % 100
        start = (start + data[i]) % 100
        if start == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(main())
