# linked list implementation

# Node object
# In this object, it only holds 2 values: its val and the pointer to the next.
# Node object has methods to get data, set data
# It also has methods to interact with the next object, get_next and set_next

# object is for python2 compatibility
class Node(object):
    def __init__(self, val):
        self.val = val 
        self.next = None 

    def get_data(self):
        return self.val 

    def set_data(self, val):
        self.val = val 
    
    def get_next(self):
        return self.next 

    def set_next(self, next):
        self.next = next 


# LinkedList Class
# Class to hold the LinkedList, where each list contain a Node
# First node is called the head.
# First value of head is empty.
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head 
        self.count = 0 

    def get_count(self):
        return self.count 

    def insert(self, data):
        # insert new node
        new_node= Node(data) 
        new_node.set_next(self.head)
        self.head = new_node 
        self.count += 1

    def find(self, val):
        # find first item given value
        item = self.head 

        while (item != None):
            if item.get_data() == val:
                return item 
            else:
                item = item.get_next()

        return None 

    def deleteAt(self, idx):
        # delete item at index
        if idx > self.count-1:
            return 
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tempIdx = 0
            node = self.head 
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head 
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next() 


itemlist = LinkedList() 
itemlist.insert(37)
itemlist.insert(50)
itemlist.insert(99)
itemlist.insert(100)
itemlist.insert(20)

print(itemlist.dump_list())