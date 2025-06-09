# Class

class School():
    name = "school of coding"

    @classmethod
    def set_school_name(cls, name):
        cls.name = name
    
    @classmethod
    def set_capacity(cls, capacity):
        cls.capacity = capacity

class Student(School):
    # constructor
    def __init__(self, nums):
        # create member variable
        self.nums = nums
        self.size = len(nums)
        self.__private_attribute = "private attribute"

    # private - private method, a method that is only used by the sole class
    def __set_uuid__(self, uuid):
        self.uuid = uuid

    # protected - protected method that is only used by the class and subclasses
    def _set_name(self, name):
        self._name = name

    # self is passed to every method to a class
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2* self.getLength()
    


