

# O(n) time // N^2 armortised time complexity
# O(n) space
def generate_binary_using_queue(n: int):
    queue = Queue()
    for i in range(1, n + 1):
        binary = bin(i).lstrip('0b')
        queue.enqueue(binary)
    return queue.queue

# O(n) time complexity
# O(n) space complexity
# interesting idea using queue here
# start the binary with "1" and then
# at every loop, generate 2 more to the 
# queue of "10" and "11", adding 0 and 1
# to the queue. At every loop, append the
# function and dequeue
def generate_binary_queue(n: int):
    list_binary = []
    queue = Queue()

    binary_0 = "0"
    binary_1 = "1"
    queue.enqueue("1")

    for i in range(n):
        list_binary.append(queue.dequeue(i))

        s1 = list_binary[i] + binary_0
        s2 = list_binary[i] + binary_1
        queue.enqueue(s1)
        queue.enqueue(s2)

    return list_binary

class Queue:
    def __init__(self):
        self.queue = []

    def seek_front(self):
        if len(self.queue) == 0:
            return ""
        return self.queue[0]
    
    def seek_end(self):
        if len(self.queue) == 0:
            return ""
        return self.queue[-1]
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.pop(0)


def main():
    inputs = [
        [1,2,3,10,4,10],
        [8,2,49,1,5,10]
    ]

    for i in range(len(inputs)):
        newqueue = Queue()
        print('queue :')
        for element in inputs[i]:
            print(
                "enqueue :", element,
            )
            newqueue.enqueue(element)
        print(newqueue.queue)

    print(generate_binary_using_queue(5))
    


if __name__=="__main__":
    main()