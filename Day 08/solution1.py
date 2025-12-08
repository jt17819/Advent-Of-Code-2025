from heapq import heappop, heappush


def main():
    with open("Day 08/data.txt", "r") as file:
        data = file.read().split("\n")
    # data = np.loadtxt("Day 08/data.txt", dtype=str)
    # print(data)
    graph = {}
    nodes = {i: list(map(int, data[i].split(","))) for i in range(len(data))}
    # print(nodes)

    h = find_all_distances(nodes)
    for _ in range(1000):
        _, n1, n2 = heappop(h)
        graph[n1] = graph.get(n1, set()) | {n2}
        graph[n2] = graph.get(n2, set()) | {n1}

    open_nodes = set(graph.keys())
    connected = []
    sizes = []
    while open_nodes:
        n = open_nodes.pop()
        c = get_connected_nodes(n, graph)
        connected.append(c)
        sizes.append(len(c))
        open_nodes = open_nodes - c
    sizes.sort(reverse=True)
    total = 1
    for i in range(3):
        total *= sizes[i] 
    return total


def find_all_distances(nodes):
    h = []
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            x = nodes[i][0] - nodes[j][0]
            y = nodes[i][1] - nodes[j][1]
            z = nodes[i][2] - nodes[j][2]
            dist = x * x + y * y + z * z
            heappush(h, (dist, i, j))
    return h


# def find_closest_node(target, nodes):
#     min_dist = float("inf")
#     for node in nodes.keys():
#         if node == target:
#             continue
#         x = nodes[target][0] - nodes[node][0]
#         y = nodes[target][1] - nodes[node][1]
#         z = nodes[target][2] - nodes[node][2]
#         dist = x * x + y * y + z * z 
#         if dist < min_dist:
#             closest = node
#             min_dist = min(min_dist, dist)

#     return closest


def get_connected_nodes(node, graph):
    nodes = [node]
    connected = set()
    while nodes:
        n = nodes.pop()
        if n not in connected:
            connected.add(n)
            nodes.extend(graph[n])
    return connected


if __name__ == "__main__":
    print(main())
