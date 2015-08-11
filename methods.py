
#// code //


#//first iteration.//

class Vector2D:
    x = 0.00
    y = 0.00

    def Set(self, x, y):
        self.x = x
        self.y = y
        

def Main():
    vec = Vector2D()
    vec.Set(5,6)
    print "X: " + str(vec.x) + ",Y: " + str(vec.y)


if __name__ == '__main__':
    Main()




#//second iteration.//
class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def Main():
    vec = Vector2D(5,6)
    print "X: " + str(vec.x) + ",Y: " + str(vec.y)


if __name__ == '__main__':
    Main()



#//third iteration.//
import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __div__(self, other):
        return Vector2D(self.x/float(other.x), self.y/float(other.y))

    def __idiv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        length = self.getLength()
        if length != 0:
            return self/Vector2D(length, length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return "X:" + str(self.x) + ",Y:" + str(self.y)

def Main():
    vec = Vector2D(5,6)
    vec2 = Vector2D(2,3)
    print vec
    print vec2
    
    vec = vec + vec2
    print vec

    vec += vec2
    print vec

    vec *= Vector2D(2,2)
    print vec

    print vec.normalized()
    print vec.getAngle()
    
if __name__ == '__main__':
    Main()


#//fourth iteration.//
import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __div__(self, other):
        return Vector2D(self.x/float(other.x), self.y/float(other.y))

    def __idiv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        length = self.getLength()
        if length != 0:
            return self/Vector2D(length, length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return "X:" + str(self.x) + ",Y:" + str(self.y)

def Main():
    vec = Vector2D(5,6)
    vec2 = Vector2D(2,3)
    print vec
    print vec2

    tempmethod = vec.getAngle
    
    vec = vec + vec2
    print vec

    vec += vec2
    print vec

    vec *= Vector2D(2,2)
    print vec

    print vec.normalized()
    print vec.getAngle()

    print tempmethod()
    
if __name__ == '__main__':
    Main()


#-----------------// extra code //-------------------------

#//Here is what proper numeric methods look like...//
import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            return Vector2D(self.x + other, self.y + other)
    __radd__ = __add__
 
    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self
 
    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        else:
            return Vector2D(self.x - other, self.y - other)
    def __rsub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(other.x - self.x, other.y - self.y)
        else:
            return Vector2D(other - self.x, other - self.y)
    def __isub__(self, other):
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self
 
    # Multiplication
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x*other.x, self.y*other.y)
        else:
            return Vector2D(self.x*other, self.y*other)
    __rmul__ = __mul__
 
    def __imul__(self, other):
        if isinstance(other, Vector2D):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self
