

class StackOverFlow(Exception):
    pass

class StackUnderFlow(Exception):
    pass



class TwoStakcs:
    def __init__(self, size):
        self.queue = [0] * size
        self.pointer1 = -1
        self.pointer2 = len(self.queue) 

    def push1(self, value):
        if self.pointer1 < self.pointer2 - 1:
            self.pointer1 += 1
            self.queue[self.pointer1] = value
        else:
            raise StackOverFlow

    def push2(self, value):
        if self.pointer2 - 1 > self.pointer1:
            self.pointer2 -= 1    
            self.queue[self.pointer2] = value
        else:
            raise StackUnderFlow
        

    def pop1(self) -> int:
        if self.pointer1 >= 0:
            value = self.queue[self.pointer1]
            self.queue[self.pointer1] = 0
            self.pointer1 -= 1
            return value
        else:
            raise StackUnderFlow
    
    def pop2(self) -> int:
        if self.pointer2 <= len(self.queue):
            value = self.queue[self.pointer2]
            self.queue[self.pointer2] = 0
            self.pointer2 += 1
            return value
        else:
            raise StackOverFlow


def main():
    new_stacks = TwoStakcs(8)
    inputs = [
        [2,4,1,0],
        [2,1,9,10]
    ]

    for i in range(len(inputs)):
        for stack in inputs[i]:
            if i == 0:
                new_stacks.push1(stack)
                print("adding to stack1: ", stack)
            else:
                new_stacks.push2(stack)
                print("adding to stack2 ", stack)
    print("twostacks :", new_stacks.queue)

    for i in range(3):
        print(new_stacks.pop1())
        print(new_stacks.pop2())

    print("twostacks :", new_stacks.queue)
    


if __name__=="__main__":
    main()