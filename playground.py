from algos.DFS import dfs_recursive as df
from algos.DFS import dfs_iterative as dfi



graph = {0:[0,1], 1:[3,0], 2:[2], 3: [1,3]}

search = df(graph)

s = dfi()
s.dfs(graph, 1)

# search.dfs(2)






