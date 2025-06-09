# graph
# 
# can be represented using two forms: 
# adjacency matrix and adjaceny list
#
# ADJACENCY MATRIX lists graph in the format 
# of a binary table, where 0 means not connected
# and 1 means that it is connected
#   
#       0   1   2
# 0     0   1   1
# 1     0   0   1
# 2     0   0   0
#
# Above adjacency matrix shows that it is a directed graph
# of 0 > 1 > 2
#    0 > 2
#
#
# ADJACENCY LIST is a graph in the format 
# of a linked list. It can be implemented using dict
# and a set. One example is as follows:
#
# graph = {
#   0 : {1,2}
#   1 : {2,3}
#   2 : {3}
#   3 : {}
#           }
#
# comparison        adjacency matrix        adjacency list
# add edge               O(1)                   O(1)
# remove edge            O(1)                   O(E)
# search edge            O(1)                   O(V)
# add vertex            O(V^2)                  O(1)
# remove vertex         O(V^2)                  O(V^2)
# bfs                   O(V^2)                  O(V+E)
# dfs                   O(V^2)                  O(V+E)
#                 pros speed for large graph     more space efficient 
#                   cons large memory space      expensive compute
#                   requirements.

# 
# implementation of graph
# using adjacency list
from typing import Type

# Node Adjacency List
# NodeList = 1 : {2,3,4}
class NodeList:
    def __init__(self, value):
        self.vertex = value
        self.next_element = None


class Graph:
    def __init__(self, number):
        self.vertices = number
        self.graph = [None] * number

    def add_edge(self, source: Type[NodeList], destination):
        dest_node = NodeList(destination)

        if source.next_element is None:
            source.next_element = set()
        source.next_element.add(dest_node)


