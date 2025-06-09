# stacks
# are data structure with LIFO operations
# last elements are added to the stack
# and popping stack will take the top
# most element. Stacks are efficient
#
# typical methods
# push(element)
# pop()
# peek()
# is_empty()
# size()
#
# Time Complexity
# push      O(1) - O(n)* armortised
# pop       O(1)
# is_empty  O(1)
# peek      O(1)
# size      O(1)

class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
    
    def push(self, element):
        self.stack_list.append(element)
        self.stack_size += 1

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        self.stack_size -= 1
        return self.stack_list.pop()
    
    def is_empty(self) -> bool:
        if self.stack_list == 0:
            return True
        return False
    
    def size(self) -> int:
        return self.stack_size


def main():
    inputs = [
        ## 
    ]

if __name__== "__main__":
    main()