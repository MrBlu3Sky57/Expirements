from DataStructures import pQueue
import collections
from queue import LifoQueue

class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.b + self.a
        return fib

# for x in Fib(1000):
#     print(x, end=' ')

def binarySort1(size, item):
    list = [x for x in range(size)]
    a = 0
    b = len(list) - 1
    while a <= b:
        k = int((a + b)/2)
        if list[k] == item:
            break
        if list[k] > item:
            b = k - 1
        else:
            a = k + 1
    return k

stack = LifoQueue(maxsize= 3)


