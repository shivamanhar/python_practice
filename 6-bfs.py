graph = {
    '5':['3', '7'],
    '3':['2', '4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited = [] # List for visited nodes
queue= [] # Initialize a queue
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Driver code 
print("Following is the Breath-First Search")

bfs(visited, graph, '5')