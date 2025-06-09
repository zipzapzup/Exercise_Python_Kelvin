# a list can hold homogenous types of elements

empty_list = ["one", "two", "three", 4, 5]
a_list = [2, "educative", "io"]
sequence_list = list(range(10))


# initialise a list
list1 = []

# append - O(1)
list1.append('storage')

# insert - O(n) if inserting at the start, technically O(k)
list1.insert(0,'more')

# pop - O(1) without element and O(n) with index
list1.pop()
list1.pop(0)

# remove O(n)
list1.remove("storage")

# reverse O(n)
list1.reverse()

def hello(name: str) -> str:
    return "hello " + name

# O(n) time complexity
def insert(lists: list, position: int, element: any) -> list:
    return lists.insert(position, element)


class List:
    def __init__(self):
        self.list = []
    
    def append(self, element: any):
        self.list.append(element)


# loop through elements
for i in list1:
    print(i)

# loop through index
for i in range(len(list1)):
    print(list1[i])


if __name__ == "__main__":
    pass