
#--------------// code //-------------------


#//vector2D.py//
class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y


#//mod.py//
----------------------------
import vector2d

def Main():
    vec1 = vector2d.Vector2D(5,6)
    vec2 = vector2d.Vector2D(1,1)

    print vec1.x
    print vec1.y
    print vec2.x
    print vec2.y

if __name__ == '__main__':
    Main()


----------------------

from vector2d import Vector2D   #or alternativly a * for everything.

def Main():
    vec1 = Vector2D(5,6)
    vec2 = Vector2D(1,1)

    print vec1.x
    print vec1.y
    print vec2.x
    print vec2.y

if __name__ == '__main__':
    Main()
