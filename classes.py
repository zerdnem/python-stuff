
#// code //

class MyClass:
	number = 0
	name = "noname"

def Main():
	me = MyClass()
	me.number = 1337
	me.name = "Draps"
	
	friend = MyClass()
	friend.number = 3
	friend.name = "Steve"

	print "Name: " + me.name + ", Favorite Number: " + str(me.number) 
	print "Name: " + friend.name + ", Favorite Number: " + str(friend.number) 

if __name__ == '__main__':
	Main()



#// extra code //


class MyNames:
	names = []
	
	#this is a method to add a new name to the 'names' list
	def add(self, name):
		self.names.append(name)

def Main():
	list = MyNames() #create a object of MyNames and calls it 'list'
	
	#calling the add function/method to add new names to the list.
	list.add("Draps")
	list.add("Steve")
	list.add("John")

	print "Names: " + str(list.names)

if __name__ == '__main__':
	Main()
