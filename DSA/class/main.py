# Class

class Student:
    # constructor
    def __init__(self, nums):
        # create member variable
        self.nums = nums
        self.size = len(nums)

    # self is passed to every method to a class
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2* self.getLength()