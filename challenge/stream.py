import array
from contextlib import AbstractContextManager


# add word
# since add word needs to be done the most
# adding word needs to be fast
# so prefer to be in O(1) time complexity
import unittest

class StreamRecorder(object):
    def __init__(self):
        self.counter = {}

    # time complexity O(n)
    def add_word(self, word: str):
        if word not in self.counter:
            self.counter[word] = 1
        else:
            self.counter[word] += 1
    
    # time complexity: O(N*Log N)
    # bigO( N^2)
    def top_words(self, k: int):
        # top words consist of
        # tuples ("apple", 10), ("orange",8)
        top_words = []

        counter_length = len(self.counter)

        if counter_length == 0:
            return self.counter
        elif k >= counter_length:
            k = counter_length

        for word, count in self.counter.items():
            top_words.append((word, count))
        
        top_words.sort(key= lambda x: x[1], reverse=True)
        return top_words[0:k]
    

class TestStreamRecorder(unittest.TestCase):
    def test_add_word(self):
        inputs = [
            "hello", "ball", "hello", "ball","apple"
        ]
        stream = StreamRecorder()
        for i in range(len(inputs)):
            stream.add_word(inputs[i])
        
        self.assertEqual( stream.counter, {})


    def test_top_words(self):
        pass


def main():
    stream = StreamRecorder()
    inputs = [
        "hello", "world", "hello", "anything", "ball", "ball", "orange",
        "durian", "apple", "hello", "anything", "ball", "hello", "boss",
        "orange", "apple"
    ]
    for i in range(len(inputs)):
        stream.add_word(inputs[i])
    
    print(
        stream.top_words(5), "\n",
        stream.top_words(4), "\n",
        stream.top_words(3))

            
if __name__=="__main__":
    main()


