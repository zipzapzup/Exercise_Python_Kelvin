
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return self.head
        
        new_node.next_node = self.head
        self.head = new_node
        return self.head
    
    def list_nodes(self):
        if self.head is None:
            return ""
        current_node = self.head
        nodes = []
        
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next_node
        
        return nodes
    
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return self.head
        
        current_node = self.head
        while current_node:
            if current_node.next_node is None:
                current_node.next_node = new_node
                break
            else:
                current_node = current_node.next_node

        return self.head
        
            
        


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None



def main():
    inputs = [
        [2,1,4,5,10,20],
        [9,1,3,10,2]
    ]

    
    for i in range(len(inputs)):
        linkedlist = LinkedList()
        for node in inputs[i]:
            linkedlist.insert_at_head(node)
        print(
            "listing nodes:\n\t",
            linkedlist.list_nodes()
        )

    end = [200,100,300]
    for i in range(len(end)):
        linkedlist.insert_at_tail(end[i]),
    print(
        linkedlist.list_nodes()
    )


if __name__=="__main__":
    main()