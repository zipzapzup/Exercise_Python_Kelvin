# Stack

# stack implementation using list
# analysis
# ArrayStack.push() - O(1) Armortised / O(n)
# ArrayStack.pop() - O(1) Armortised / O(n)
# ArrayStack.top() - O(1)
# ArrayStack.len() - O(1)
#
class ArrayStack:
    def __init__(self,name):
        self.name = name
        self.stack = []

    def __len__(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    

