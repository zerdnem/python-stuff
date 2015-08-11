
#--------------// code //-------------------


#//first iteration. Iterator//
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def Main():
    rev = Reverse('Drapsicle')
    for char in rev:
        print char

if __name__ == '__main__':
    Main()



#//second iteration. Generator//
def Reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def Main():
    rev = Reverse('Drapsicle')
    for char in rev:
        print char

if __name__ == '__main__':
    Main()


#//third iteration. Generator Expression//
def Main():
    data = 'Drapsicle'
    print list(data[i] for i in range(len(data)-1, -1, -1))

if __name__ == '__main__':
    Main()



#-----------------// extra code //-------------------------
#This Iterator picks random items in the container and goes until it randomly hits the end.

import random

class Reverse:
    """Random Iterator that loops until it randomly hits the end."""
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        self.index = random.randint(0, len(self.data))
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

def Main():
    rev = Reverse('Drapsicle')
    for char in rev:
        print char

if __name__ == '__main__':
    Main()
