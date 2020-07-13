class dfs_recursive:
    def __init__(self, graph):
        self.visited = set()
        self.graph = graph
    
    def dfs(self, node):
        if node not in self.visited:
            print("just visited "+str(node))
            self.visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor)

class dfs_iterative:
    def dfs(self, graph, node):

        stack, visited = [], set()
        stack.append(node)

        while len(stack):
            curr_node = stack.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                print("just visited "+str(curr_node))
                for neighbor in graph[curr_node]:
                    stack.append(neighbor)

        