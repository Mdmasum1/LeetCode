
'''
---Problem: Write a problem, largest connected, that takes the 
---adjacency list of an undirected graph. The function
---should return the size of the largest connected component
---in the graph
'''
#Intution: 1. Start iterating through the input
#          2. 

def largestComponent(graph):
    visited = set()  # Tracking the node which has already been visited
    lcomponent = 0

    # Start iterating through every node in the graph
    for node in graph:
        size = exploreSize(graph, node, visited)

        # Checking the conditions
        if size > lcomponent:
            lcomponent = size

    return lcomponent

# Helper function - DFS type
def exploreSize(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    size = 1

    # Looping through the neighboring graph
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)

    return size

# Example graph with Adjsency list
example_graph = {
    1: [2, 3],
    2: [1],
    3: [1]
}

result = largestComponent(example_graph)
print(result)










