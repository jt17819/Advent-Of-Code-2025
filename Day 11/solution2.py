# import numpy as np
from functools import cache


def main():
    @cache
    def dfs(node, dac, fft):
        total = 0
        for dest in graph[node]:
            if dest == "out":
                if dac and fft:
                    return 1
                return 0

            if dest == "dac":
                total += dfs(dest, 1, fft)
            if dest == "fft":
                total += dfs(dest, dac, 1)
            else:
                total += dfs(dest, dac, fft)
        return total
    
    
    with open("Day 11/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 11/data.txt", dtype=str)
    # print(data)
    graph = {}
    for line in data:
        key, values = line.split(": ")
        graph[key] = graph.get(key, []) + values.split(" ")
    # print(graph)

    total = dfs("svr", 0, 0)

    # open_nodes = [["svr", 0 ,0, []]]
    # while open_nodes:
    #     node, dac, fft, h = open_nodes.pop()
    #     h.append(node)
    #     for dest in graph[node]:
    #         if dest in h:
    #             continue
    #         if dest == "out":
    #             if dac and fft:
    #                 total += 1
    #         else:
    #             if dest == "dac":
    #                 dac = 1
    #             if dest == "fft":
    #                 fft = 1
    #             open_nodes.append([dest, dac, fft, h[:]])

    return total


if __name__ == "__main__":
    print(main())
