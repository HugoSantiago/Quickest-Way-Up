class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

# Class of the node
class Node:
   
    # Adjacency list that shows the
    # vertexNumber of child vertex
    # and the weight of the edge   
    def __init__(self, vertexNumber):       
        self.vertexNumber = vertexNumber
        self.children = []
   
    # Function to add the child for
    # the given node
    def Add_child(self, vNumber, length):   
        p = Pair(vNumber, length)
        self.children.append(p)