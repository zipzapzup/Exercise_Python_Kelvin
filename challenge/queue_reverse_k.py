from typing import Type


class Queue:
    def __init__(self):
        self.queue_list = []
    
    def enqueue(self, value):
        self.queue.append(value)
        self.length += 1

    def size(self):
        return len(self.queue_list)
    
    def dequeue(self):
        if self.is_empty():
            return False
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return False
        return self.queue[0]

    def last(self):
        return self.queue[-1]
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False


# given a queue and number k, reverse order the first k element
# in queue. If k is less than 0, k exceeds queue size or empty
# return NULL. Otherwise return the modified
    
# Example: [50,0,99,1,2,3,4], k = 3
#          [99,0,50,1,2,3,4]

# O(n^2) time complexity
# O(k) where k is the heigh of stack
def reverse_queue_k(queue: Type[Queue], k: int):
    if (queue.size() == 0 
            or k > queue.size()
            or k < 0):
        # when the following conditions
        # are met: empty queue,
        # k larger than length, or
        # k is negative. Return NULL
        return None
    
    internal_queue = []
    for i in range(k):
        internal_queue.append(queue.queue_list[i])
        queue.queue_list[i] = None
    
    for i in range(k):
        queue.queue_list[i] = internal_queue.pop()

    return queue

def reverse_queue_k_enqueue(queue: Type[Queue], k : int):
    pass
    

def main():
    queue = Queue()
    queue.queue_list = [50,0,99,1,2,3,4]
    print("\ninitial queue: ",queue.queue_list)
    print(
        "reverse queue: ",
        reverse_queue_k(queue, 3).queue_list,
        )
    
    inputs = [
        [11,3,5,99,10,40],
        [4,5,6,7,5,6,7,8,9],
        [119,100,23,10,401,201,400],
        [1,3,10],
        [9,1,2,3,1,4,1,5,1,2]
    ]

    for i in range(len(inputs)):
        new_queue = Queue()
        new_queue.queue_list = inputs[i]
        print("initial queue: ",
            inputs[i])
        
        value = reverse_queue_k(new_queue,4)
        if value is not None:
            print("reverse queue: ",
              value.queue_list)
        else:
            print("None")

if __name__=="__main__":
    main()