name = 'Swaroop'

if name.startswith("S"):
    print "Yes"

if 'a' not in name:
    print "Yes"
else:
    print "No"

if name.find('war') != -1:
    print "Yes"

delimiter = "_*_"
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
