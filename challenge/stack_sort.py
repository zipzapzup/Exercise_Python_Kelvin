# use stack to sort
# 
# 

class Stack(object):
    def __init__(self):
        self.stack_list = []

    def push(self, data: int) -> None:
        self.stack_list.append(data)

    def pop(self) -> int:
        if not self.stack_list:
            raise IndexError("stack is empty")
        return self.stack_list.pop()
    
    def peek(self) -> int:
        if self.stack_list:
            return self.stack_list[-1]
        return IndexError("stack is empty")

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0
# algorithmn
# is as follow, when the lowest value
# place it there
# process:
#           - place the list in the main stack
#           - 
#           - 

def sort_using_stack(list_to_sort: list):
    main_stack = Stack()
    stack = Stack()

    while list_to_sort:
        placeholder = list_to_sort.pop()

        if (len(stack.stack_list) <= 0 
                or placeholder >= stack.peek()):
            stack.push(placeholder)
        else:
            while not len(stack.stack_list) == 0 and placeholder < stack.peek():
                list_to_sort.append(stack.pop())
            stack.push(placeholder)

    while stack.stack_list:
        main_stack.push(stack.pop())
    return main_stack


def main():
    inputs = [
        [1,3,1,5,1,8,6,7],
        [8,9,5,6,8,5,0],
        [10,12,15,8,20]
    ]
    for i in range(len(inputs)):
        print("\nstarting points: ",
              inputs[i])
        print("ending points: ",
            sort_using_stack(inputs[i]).stack_list)


if __name__== "__main__":
    main()