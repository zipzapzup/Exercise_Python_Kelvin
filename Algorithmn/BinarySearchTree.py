

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert Node
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print Tree
    def PrintTree(self):
        print(self.data)


root = Node(10)
root.PrintTree()








print("Implement Tree Data Structure:")

Company = {




}

Prizes = ['Gold', 'Silver', 'Bronze', 'Nothing', 'Zilch']

for i, medals in enumerate(Prizes):
    print("Coming {} place will earn you {}".format(i, medals))



class Tree1():
    def __init__(self, root):
        self.root = root
        self.children = []
    def addNode(self, obj):
        self.children.append(obj)

class Node1():
    def __init__(self,data):
        self.data = data
        self.children = []
    def addNode(self, obj):
        self.children.append(obj)



Winner = Tree1()