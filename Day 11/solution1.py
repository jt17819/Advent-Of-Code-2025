# import numpy as np


def main():
    with open("Day 11/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 11/data.txt", dtype=str)
    # print(data)
    graph = {}
    for line in data:
        key, values = line.split(": ")
        graph[key] = graph.get(key, []) + values.split(" ")
    # print(graph)

    open_nodes = ["you"]
    total = 0
    while open_nodes:
        node = open_nodes.pop()
        for dest in graph[node]:
            if dest == "out":
                total += 1
            else:
                open_nodes.append(dest)

    return total


if __name__ == "__main__":
    print(main())
