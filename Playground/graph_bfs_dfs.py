# a graph can be implemented using a different method
# another method is to implement graph
# using a dictionary and sets
#
# graph implementation:
# 1. graph with dictionary and sets
# 2. graph with linkedlist
#
#
# implementation with dict and sets
#
# graph = {
#       "a" : {"b", ""c"},
#       "b" : {"d"},
#       "c" : {"d"}
#       "d" : {}
#       }
# in graph, a vertex is a node
# and an edge is what points one vertex 
# to another vertex
#
# vertex -> vertex
# the arrow is the edge

from typing import Type



class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, source, destination):
        # graph is dictionary and a set
        # graph = {
        #           "a" : {"b", "c"} 
        #         }

        if source in self.graph:
            for item in destination:
                self.graph[source].add(item)
        else:
            self.graph[source] = {destination}

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, self.graph[vertex])


# Q: given a directed graph where there is a vertex
# and edges. Assuming that all of the vertex value is unique
# write a BFS algorithmn
# 
# time complexity O(V+E)
# the time complexity here is vertex + edges
# because the algorithmn will need to visit
# every vertex and every edges the vertex connects to
# it makes it a linear complexity algorithmn
#
# space O(E)
# as high as the queue is
            
def bfs_traversal_graph( graph: Type[Graph], source):
    # result holds the traversal final data
    #
    # for visited we use set to determine whether an 
    # element has been visited. In this graph, we assume
    # that an element is unique. Note that a set can
    # be used to hold object as well.
    #
    # >>> new_set
    # {'A', <__main__.Node object at 0x102a36f60>}
    # >>> a in new_set
    # True
    # >>> 
    result = []
    visited = set()

    queue = []
    
    queue.append(source)
    visited.add(source)

    while queue:
        current_vertex = queue.pop(0)
        result.append(current_vertex)

        for neighbor in graph.graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result




# Q: given a directed graph represented by an adjacency list and integer
# source, write a function that perform a depth first search. Return
# a list of the traversal
# 
# depth first search is a traversal algortihmn that traverse the
# graph in depth first and retrieve the result. A graph with an
# adjacency list is represented with a dictionary and set
#  
# dfs can be implemented using a recursive function. Recursive
# keep track of itselves. if the node is in visited then return
# if not:
#   - add it to visited
#   - add to result
# recursively iterate through every neighbor in the graph
# if its at the end of the neighbor, return the function
#
# DFS 
# time complexity (V + E)
# space: O(V)
class Counter:
    def __init__(self):
        self.counter = 0

def dfs_graph_traversal(graph: Type[Graph], source: int):
    count = Counter()
    visited = set()
    result = []
    recursive_dfs(visited, result, source, graph, count)
    return result, count.counter


def recursive_dfs(visited: set, result :list, node, graph: Type[Graph], count):
    if node in visited:
        return
    visited.add(node)
    result.append(node)
    count.counter += 1
    if node in graph.graph:
        for neighbor in graph.graph[node]:
            recursive_dfs(visited,result, neighbor, graph, count)
    return
        

    




def main():
    inputs =[
        {0: [1, 2], 
         1: [2], 
         2: [3], 
         3: [1, 2]},

        {0: [1], 
         1: [3], 
         2: [3], 
         3: []},

        {0: [1, 2], 
         1: [2], 
         2: [3], 
         3: [1, 2]},

        {0: [1, 2], 
         1: [2], 
         2: [3], 
         3: [1, 2,4],
         4: []},

         {0: [4,1],
          1: [2,5],
          2: [],
          3: [2],
          4: [3],
          5: []
         }
    ]

    for i in range(len(inputs)):
        graph = Graph()
        graph.graph = inputs[i]
        print(
            "\ninputs :", inputs[i],
            "\nbfs result :",
            bfs_traversal_graph(graph, 0)
              )
        
    for i in range(len(inputs)):
        graph = Graph()
        graph.graph = inputs[i]
        print(
            "\ninputs :", inputs[i],
            "\ndfs result :",
            dfs_graph_traversal(graph,0)
        )



if __name__=="__main__":
    main()

