# import numpy as np


def main():
    with open("Day 10/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 10/data.txt", dtype=str)
    # print(data)

    total = 0
    for line in data:
        parts = line.split(" ")
        target = [False if s == "." else True for s in parts[0][1:-1]]
        buttons = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
        state = [False] * len(target)
        total += sum(dfs(target, buttons, state, []))

    return total


def dfs(target, buttons, state, pressed):
    if target == state:
        return pressed
    
    if not buttons:
        return None
    
    # don't press
    ans1 = dfs(target, buttons[1:], state, pressed + [0])

    # press
    for s in buttons[0]:
        state[s] = not state[s]
    
    ans2 = dfs(target, buttons[1:], state, pressed + [1])

    # unpress
    for s in buttons[0]:
        state[s] = not state[s]

    if ans1 and ans2:
        return ans1 if sum(ans1) < sum(ans2) else ans2
    elif ans1:
        return ans1
    elif ans2:
        return ans2
    else:
        return None


if __name__ == "__main__":
    print(main())
