# Test Driven Development
# Overview
# Its an approach in Extreme Programming concepts, where the approach is to test the code, prior to deployment into production

# TDD vs UnitTest
# TDD differs a little compared to Unittest, the definition are:
# UnitTest: refers to the testing of individual code, to check the logic of a units of behaviour.
# TDD - test driven development: refers to the approach that testing drives the development. In TDD, there are usually 3 types of test: unit test, functional test and acceptance test.


import unittest


print("Hello World - Let's Begin TDD Approach")

def addOne(n: int)-> int:
    return n + 1

class UnitTestCase(unittest.TestCase):
    def test_addOne(self):
        # example of unittest assert one conditions to another
        self.assertEqual(addOne(5) ,6)
        self.assertEqual(addOne(9), 10)

        input = [10,11,12,13,14,15]
        output = [11,12,13,14,15,16]

        for i in range(len(input)):
            self.assertEqual(addOne(input[i]),output[i])

        for i in range(10000):
            self.assertEqual(addOne(i), i + 1)



if __name__ == '__main__':
    unittest.main()