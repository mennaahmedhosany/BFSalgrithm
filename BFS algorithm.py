import ast

with open('BFS_graph.txt') as f:
    data_graph = f.read()


data_dic = ast.literal_eval(data_graph)



visited = []
queue = []
def bfs(visited, data_dic, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in data_dic[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
# Driver Code
print('the result of the is the Breadth-First Search')
bfs(visited, data_dic, '5')