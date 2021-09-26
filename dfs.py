#!/usr/bin/env python
# Author: Suwidiana Ketut. Created at: Sept. 26, 2021

graph = {
    '1': ['4', '2'],
    '2': ['3', '5', '7', '8'],
    '3': ['9', '10'],
    '4': [],
    '5': ['6', '7'],
    '8': ['7']
}

def dfs(graph, root = list(graph.keys())[0], visited = []):
    if not root in visited: visited.append(root)
    for node in graph[root]:
        if not node in visited: visited.append(node)
        if node in graph.keys():
            dfs(graph, node, visited)

    return visited

def bfs(graph, root = list(graph.keys())[0], visited = []):
    if root not in visited: visited.append(root)
    queue = []
    if root in graph.keys():
        for node in graph[root]:
            if node not in visited: visited.append(node); queue.append(node)
    for node in queue:
        bfs(graph, node, visited)
    else: pass
    return visited

if __name__ == "__main__":
    print(dfs(graph))
    print(bfs(graph))
