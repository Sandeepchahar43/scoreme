def longest_path(graph):
    from collections import deque

    n = len(graph)
    in_degree = [0] * n

    # Calculate in-degrees of all nodes
    for u in range(n):
        for v, w in graph[u]:
            in_degree[v] += 1

    # Topological sorting using Kahn's Algorithm
    zero_in_degree_queue = deque()
    for u in range(n):
        if in_degree[u] == 0:
            zero_in_degree_queue.append(u)

    topo_order = []
    while zero_in_degree_queue:
        u = zero_in_degree_queue.popleft()
        topo_order.append(u)
        for v, w in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree_queue.append(v)

    # Initialize distances array
    dist = [-float('inf')] * n

    # Set the starting node distances to 0
    for u in range(n):
        if in_degree[u] == 0:
            dist[u] = 0

    # Relax edges according to the topological order
    for u in topo_order:
        if dist[u] != -float('inf'):
            for v, w in graph[u]:
                if dist[u] + w > dist[v]:
                    dist[v] = dist[u] + w

    # The longest path in the graph is the maximum value in the distance array
    # Return 0 if all values are -inf which means there were no valid paths
    return max(max(dist), 0)

def test_longest_path():
    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    result1 = longest_path(graph1)
    assert result1 == 7, f"Test case graph1 failed, got {result1}"

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    result2 = longest_path(graph2)
    assert result2 == 6, f"Test case graph2 failed, got {result2}"

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    result3 = longest_path(graph3)
    assert result3 == 30, f"Test case graph3 failed, got {result3}"

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    result4 = longest_path(graph4)
    assert result4 == 2, f"Test case graph4 failed, got {result4}"

    print("All test cases pass")

if __name__ == "__main__":
    test_longest_path()
