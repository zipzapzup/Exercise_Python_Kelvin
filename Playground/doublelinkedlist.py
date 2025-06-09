


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # optional

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return self.head
        
        self.head.previous_node = new_node
        new_node.next_node = self.head
        self.head = new_node

        # if there is a head
        # do the following
        # head.prev = new_node
        # new_node.next = self.head

    def delete_at_head(self):
        if self.head is None:
            return
        
        temp_node = self.head
        self.head = temp_node.next_node

        if temp_node.previous_node:
            temp_node.previous_node = None

        return self.head



    def list_nodes(self):
        if self.head is None:
            return
        
        current_node = self.head
        while current_node:
            print(
                current_node.data, 
                end =" "
            )
            current_node = current_node.next_node

        
        



class Node(DoubleLinkedList):
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


def main():
    linked_list = DoubleLinkedList()
    for i in range(10):
        linked_list.insert_at_head(i)
    linked_list.list_nodes()
    print("\ndelete at head:")

    for i in range(5):
        linked_list.delete_at_head()
    linked_list.list_nodes()

if __name__== "__main__":
    main()