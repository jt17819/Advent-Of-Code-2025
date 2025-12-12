# import numpy as np
# from functools import cache

#! METHOD TOO SLOW FOR TEST INPUT
# def main():
#     with open("Day 10/data.txt", "r") as file:
#         data = file.read().split("\n")
#     # data = np.loadtxt("Day 10/data.txt", dtype=str)
#     # print(data)

#     total = 0
#     for line in data:
#         parts = line.split(" ")
#         target = tuple(map(int, parts[-1][1:-1].split(",")))
#         buttons = tuple(tuple(map(int, b[1:-1].split(","))) for b in parts[1:-1])
#         # state = [0] * len(target)
#         # print(target)
#         # print(state)
#         # print(buttons)
#         total += dfs(buttons, target, 0)
#         print(total)

#     return total


# @cache
# def dfs(buttons, state, pressed):
#     # if (buttons, state) in memo:
#     #     return memo

#     if any(s < 0 for s in state):
#         return

#     if sum(state) == 0:
#         return pressed
    
#     if not buttons:
#         return None
    
#     # don't press
#     ans1 = dfs(buttons[1:], state, pressed)

#     # press
#     new_state = tuple(state[i] - 1 if i in buttons[0] else state[i] for i in range(len(state)))
    
#     ans2 = dfs(buttons, new_state, pressed + 1)

#     if ans1 and ans2:
#         return min(ans1, ans2)
#     elif ans1:
#         return ans1
#     elif ans2:
#         return ans2
#     else:
#         return None

# from z3 import *
import z3

def main():
    with open("Day 10/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 10/data.txt", dtype=str)
    # print(data)

    total = 0
    for line in data:
        parts = line.split(" ")
        target = tuple(map(int, parts[-1][1:-1].split(",")))
        buttons = tuple(tuple(map(int, b[1:-1].split(","))) for b in parts[1:-1])
    
        solver = z3.Solver()

        bvars = [z3.Int(f"a{n}") for n in range(len(buttons))]
        for b in bvars:
            solver.add(b >= 0)

        for i,v in enumerate(target):
            vvars = [bvars[j] for j,button in enumerate(buttons) if i in button]
            solver.add(z3.Sum(vvars) == v)

        while solver.check() == z3.sat:
            model = solver.model()
            n = sum([model[d].as_long() for d in model])
            solver.add(z3.Sum(bvars) < n)

        total += n

    return total


if __name__ == "__main__":
    print(main())
