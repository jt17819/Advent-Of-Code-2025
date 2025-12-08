from functools import reduce


def main():
    with open("Day 06/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 06/data.txt", dtype=str)
    # print(data)
    total = 0
    stack = []
    for i in reversed(range(len(data[0]))):
        num = ""
        for line in data[:-1]:
            num += line[i]

        if not num.strip(): continue
        
        stack.append(int(num.strip()))
        match data[-1][i]:
            case "+":
                total += sum(stack)
                stack = []
            case "*":
                total += reduce(lambda x, y: x * y, stack)
                stack = []
            # case _:
                # pass
    return total


if __name__ == "__main__":
    print(main())
