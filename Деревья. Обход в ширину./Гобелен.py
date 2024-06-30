n = int(input())
graph = eval(input())
a, b = map(int, input().split())

def find_min_parent(graph, a, b):
    def dfs(node, target_node, path):
        if node == target_node:
            return path
        for vertex in graph.get(node, []):
            path = path + [node]
            result = dfs(vertex, target_node, path)
            if result:
                return result
        return None

    path_a = dfs(next(iter(graph)), a, [])
    path_b = dfs(next(iter(graph)), b, [])
    common_ancestors = set(path_a) & set(path_b)
    general_parent = max(common_ancestors, key=path_a.index)

    return general_parent

print(find_min_parent(graph, a, b))