n, v = map(int, input().split())
visited_vertex = [False] * n

graph = [[] for x in range(n)]
for i in range(n):
    vertex = input().split()
    if vertex[0]!= '-1':
        graph[i] = list(map(int, vertex))

def find_connected_component(n, v, graph, visited_vertex):
    component = set()
    def _dfs(start_vertex):
        visited_vertex[start_vertex] = True
        component.add(start_vertex)
        for p in graph[start_vertex]:
            if not visited_vertex[p]:
                _dfs(p)

    _dfs(v)
    result = sorted(component)
    return ' '.join(map(str, result))

print(find_connected_component(n, v, graph, visited_vertex))