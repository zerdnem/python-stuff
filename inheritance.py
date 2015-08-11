
#--------------// code //-------------------


#//first iteration.//

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age) # You can run and super class method like this.


def Main():

    thePet = Pet("Pet", 1)
    jess = Cat("jess", 3)

    print "is jess a Cat?" + str(isinstance(jess, Cat))
    print "is jess a Pet?" + str(isinstance(jess, Pet))
    print "is thePet a Cat?" + str(isinstance(thePet, Cat))
    print "is thePet a Pet?" + str(isinstance(thePet, Pet))
    
    print jess.name

if __name__ == '__main__':
    Main()


#//second iteration. (polymorphism)//

class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "Meowww"

class Dog(Pet):

    def __init__(self, name, age):
        Pet.__init__(self, name, age)

    def talk(self):
        return "Wooff!"

def Main():

    pets = [Cat("jess",3), Dog("Jack", 2), Cat("fred", 7), Pet("thePet", 5)]

    for pet in pets:
        print "Name:" + pet.name + ", Age:" + str(pet.age) + ", says:" + pet.talk()
    
if __name__ == '__main__':
    Main()



#-----------------// extra code //-------------------------

class Person():
 def pay_bill():
   raise NotImplementedError

class Millionare(Person):
 def pay_bill():
   print "Here you go! Keep the change!"

class GradStudent(Person):
 def pay_bill():
   print "Can I owe you ten bucks or do the dishes?"

def Main():

    peoples = [Millionare(), GradStudent()]

    for people in peoples:
        people.pay_bill()
    
if __name__ == '__main__':
    Main()
