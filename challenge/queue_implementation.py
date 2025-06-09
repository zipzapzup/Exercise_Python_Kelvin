
# class Queue implemented using two stacks
# first stack
# - implement a list
# second stack
# - implement
#
# a stack is a FILO (first in last out)
# data structure. Our first stack acts as 
# normal function.
# 
# a queue has two main functionality
# enqueue
#       - is just a simple operation
#       that append to the normal stack
# dequeue
#       - is an operation that you will
#       need to transfer the object 
#       and later just pop it in a stack

# O(1) constant time for enqueue
# O(n) time for dequeue

# stack can be reversed
# O(1) constant for dequeue
# O(n) time for enqueue

class Queue(object):
    def __init__(self):
        self.stack_main = []
        self.stack_temp = []

    def enqueue(self, data: int):
        self.stack_main.append(data)

    def dequeue(self):
        while self.stack_main:
            self.stack_temp.append(self.stack_main.pop())
        self.stack_temp.pop()

        while self.stack_temp:
            self.stack_main.append(self.stack_temp.pop())
        return self.stack_main

    def peek_top(self):
        if self.stack_main:
            return self.stack_main[0]
        return None
    
    def peek_tail(self):
        if self.stack_main:
            return self.stack_main[-1]
        return None


def main():
    inputs = [
        [1,4,1,401,2,104,10],
        [1,7,0,5,9,2],
        [17,11,9,5,3],
        [1,3,5],
        [10,15,18,20]
    ]

    for i in range(len(inputs)):
        new_queue = Queue()
        for data in inputs[i]:
            new_queue.enqueue(data)
        print("\nqueue main stack:",
              new_queue.stack_main,
              "\nqueue temp stack:",
              new_queue.stack_temp)
        for k in range(3):
            new_queue.dequeue()
        
        print(
            "queue main stack after dequeue",
            new_queue.stack_main
            )


if __name__ == "__main__":
    main()