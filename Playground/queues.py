# queues
# is a linear data structure which store elements
# in a sequential manner. Queues are implemented
# using a FIFO structure, where the left is normally
# head of the queue and the right is back of the queue
#
#
# types of queues:
# LinearQueue
# CircularQueue
# PriorityQueue
# DoubleEndedQueue
#
# operations:
#
# enqueue - insert to the right         O(1)
# of the queue, added a new person to the queue
#
# dequeue - shorten the queue           O(1)
# analogy of a person who has gotten his part
# front()                               O(1)
# back()                                O(1)
# empty                                 O(1)
# size                                  O(1)
#
#
# implementation
# queues via
#           list     linkedlist     doublelinklist
# enqueue   O(1)        O(1)          O(1)
# dequeu    O(n)        O(1)          O(1)
# seekhead  O(1)        O(1)          O(1)
# seeklast  O(1)        O(n)          O(1)
# capacity  O(1)        O(1)          O(1)
# find #    O(n)        O(n)          O(n)   - bad
# isempty   O(1)        O(1)          O(1)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:    
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node 
        self.length += 1
        return 

    def remove_at_head(self):
        if self.head is None:
            return False
        if self.head.next_node is None:
            self.head = None
            return True
        else:
            current_node = self.head
            current_node.previous_node = None
            self.head = self.head.next_node
            return True
        


class Node:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None

class Queue:
    def __init__(self):
       self.queue = DoubleLinkedList()

    def enqueue(self, data):
        self.queue.insert_at_tail(
            data
        )

    def dequeue(self):
        return self.queue.remove_at_head()
    
    def seek_last(self):
        return self.queue.tail.data
    
    def seek_first(self):
        return self.queue.head



def main():
    new_queue = Queue()
    for i in range(10):
        new_queue.enqueue(i)
        print("enqueue", i)
    print(
        "\nfirst :",
        new_queue.seek_first(),
        "\nlast :",
        new_queue.seek_last()
    )
    for i in range(5):
        print(
            "\ncurrent head: ", new_queue.seek_first().data,
            "\nremove head: ",new_queue.dequeue(),
            "\nnew head: ", new_queue.seek_first().data,
        )

if __name__=="__main__":
    main()