from collections import deque, defaultdict


def bfs(start, graph, visited, component):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        component.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


def solve(N, D, heights):
    graph = defaultdict(list)

    # 建立图的邻接表
    for i in range(N - 1):
        if abs(heights[i] - heights[i + 1]) <= D:
            graph[i].append(i + 1)
            graph[i + 1].append(i)

    visited = [False] * N
    components = []

    # 找到所有连通分量
    for i in range(N):
        if not visited[i]:
            component = []
            bfs(i, graph, visited, component)
            components.append(component)

    # 对每个连通分量进行排序
    result = [0] * N
    for component in components:
        sorted_heights = sorted([heights[i] for i in component])
        for idx, node in enumerate(sorted(component)):
            result[node] = sorted_heights[idx]

    return result


# 读取输入
N, D = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# 计算结果并输出
result = solve(N, D, heights)
for height in result:
    print(height)