def dfs_iterative(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.append(vertex)
            
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited

def main():
    V = int(input())
    E = int(input())
    
    graph = [[] for _ in range(V)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(V):
        graph[i].sort()
    
    start_node = int(input())

    visited = dfs_iterative(graph, start_node)
    
    print(" ".join(map(str, visited)))

if __name__ == "__main__":
    main()
