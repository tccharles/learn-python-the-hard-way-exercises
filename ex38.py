ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # if not 10 items in 'stuff'
	next_one = more_stuff.pop() #The method pop() removes and returns last object or obj from the list.
								#So it will take Boy, then Girl, then Banana, etc.
	print "Adding: ", next_one  #This will print the last object in 'more_stuff'
	stuff.append(next_one)		#This will add (append) that last object to 'stuff'
	print "There are %d items now." % len(stuff) #This will print the number of items now in 'stuff'
print "There we go: ", stuff #Once the while loop is done (= 10), it will print the 'stuff' list with all
							 #10 items which is 'ten_things' + 'more_stuff'. Notice, not everything in 
							 #more_stuff will be added because the while loop just want 10 items.

print "Let's do some things with stuff."

print stuff[1] #Prints the 'second' item in 'stuff'
print stuff[-1] #Prints the last item in 'stuff'
print stuff.pop() #Removes and prints the last itme in 'stuff'
print ' ' .join(stuff) #This will only print 9 itmes from 'stuff' (with a space between items) since the 10th item 
					#was removed with pop above.
print '#' .join(stuff[3:5]) #That extracts a "slice" from the stuff list that is from element 3 to element 
							#4, meaning it does not include element 5. It's similar to how range(3,5) would work.
