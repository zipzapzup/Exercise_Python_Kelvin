# Graph is a data structure
# that consists of a vertex(node) and edges
# vertex is the node of the graph
# and edges are the relationship pointing
# to the connection
#
# two different types of graph
# 
# undirected graph 
# a graph data structure with a two way connection
# it can go from vertex a and b whilst
# spinning it out as well
# maximum number of edges is: n(n-1) / 2
# 
# directed graph 
# a graph data structure where connection flows
# in according to one direction
# maximum number of edges is: n* (n-1)


# time complexities
# Operation         Adjacent List       Adjacent Matrix
# Add Vertex:           O(1)                O(V^2)
# Remove Vertex         O(V + E)            O(V^2)
# Add Edge              O(1)                O(1)
# Remove Edge           O(E)                O(1)
# Search                O(V)                O(1)
# Bread First Search    O(V+E)              O(V^2)
# Depth First Search    O(V+E)              O(V^2)

from typing import Type

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next_element = self.head_node
            self.head_node = new_node
    
    def list_nodes(self):
        nodes = []
        current_node = self.head_node

        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next_element
        return nodes


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def get_length(self):
        return len(self.queue)


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.array = []
        for i in range(self.vertex):
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if (source < self.vertex and destination < self.vertex):
            self.array[source].insert_at_head(destination)
        return False

    def add_edge_birection(self, source, destination):
        if (source < self.vertex and destination < self.vertex):
            self.array[source].insert_at_head(destination)
            self.array[destination].insert_at_head(source)
        return False

    def print_graph(self):
        print("\nprinting graph : ")
        for i in range(self.vertex):
            print("|", i, end=" | => ")

            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")



def bfs_traversal_graph(graph: Type[Graph], source):
    result = []
    num_of_vertices = graph.vertex
    visited = [False] * num_of_vertices

    # create a queue for the DFS
    queue = Queue()

    queue.enqueue(source)
    visited[source] = True

    while queue.queue:
        current_vertex= queue.dequeue()
        result.append(current_vertex)





def main():
    inputs = [
        [1,2,3,1,4,1,4],
        [9,1,8,5,1,9]
    ]

    for i in range(len(inputs)):
        new_linkedlist = LinkedList()
        for value in inputs[i]:
            new_linkedlist.insert_at_head(value)
            print("inserting :", value)
        print("finished linkedlist :", new_linkedlist.list_nodes())
    
    g = Graph(4)
    g.add_edge(0,2)
    g.add_edge(0,1)
    g.add_edge(1,3)
    g.add_edge(2,3)

    g.print_graph()


if __name__ == "__main__":
    main()