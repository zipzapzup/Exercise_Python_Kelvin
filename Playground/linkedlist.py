# LinkedList has 2 classes
# head
# data

# SinglyLinkedList
#
# consists of two class
# SinglyLinkedList class which holds the head
# and the Node class which holds the data
# and contains one pointer to the next node

#tradeoffs
#             singlelinked list     list
# access        O(n)            O(1)
# insert head   O(1)            O(n)
# remove head   O(1)            O(n)
# insert tail   O(n)            O(1) *append() **armortised O(n)
# remove tail   O(n)            O(1) *pop()


class SingleLinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    #   1. create newnode
    #   2. set newnode.next_node point to current head
    #   3. set head to newnode
    #   4. return head
    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_node = self.head_node

        self.head_node = temp_node
        return self.head_node
    
    def list_nodes(self):
        current_node = self.head_node

        if current_node is None:
            return ""

        while current_node:
            temp_node = current_node
            current_node = temp_node.next_node
            print(
                temp_node.data, 
                end=" ")
    
    def delete_at_head(self):
        if self.head_node is None:
            return        
        temp_node = self.head_node
        self.head_node = self.head_node.next_node
        del temp_node

    def search_nodes(self, head_node, value) -> bool:
        if head_node is None:
            return False
        
        current_node = head_node
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next_node
        return False

    def delete_nodes_by_values(self, head_node, value):
        if head_node is None:
            return False
        
        # base case check first        
        current_node = head_node
        if current_node.data == value:
            current_node = None
            return True
        
        while current_node.next_node:
            skip_nodes = current_node.next_node
            if skip_nodes.data == value:
                current_node.next_node = skip_nodes.next_node
                return True
            else:
                current_node = current_node.next_node
        return False



class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


def main():
    linked_list = SingleLinkedList()
    inputs = [
        [5, 4,7,17,20,1,18],
        [4, 9,4,1,25,1,9,2]
    ]

    for i in range(len(inputs)):
        print(
            "\ninputs : \n",inputs[i]
            )

        for num in inputs[i]:
            print(
                "insert at head: ", 
            linked_list.insert_at_head(num)
            )

        print(
            "latest head:", 
            linked_list.get_head().data
            )
        
    linked_list.list_nodes()
    print('\ndelete')
    linked_list.delete_at_head()
    linked_list.list_nodes()

    print("\ndelete nodes by values:")
    print(
        linked_list.delete_nodes_by_values(linked_list.head_node, 18)
    )
    linked_list.list_nodes()



if __name__== "__main__":
    main()