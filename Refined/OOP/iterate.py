class CountToMax:
    """Class to Count to N"""
    # __iter__ method is a special method that allows class
    # to be iteratable
    def __init__(self, max=10):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration



number = CountToMax(10)

# Note to start the iterate use loop.
# One way is
#
# number.__iter__()
# number.__next__()


for i in number:
    print(i)