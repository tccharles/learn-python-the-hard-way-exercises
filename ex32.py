'''
Before you can use a for-loop, you need a way to store the results 
of loops somewhere. The best way to do this is with lists. Lists are 
exactly what their name says: a container of things that are organized
in order from first to last.
'''

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can trhough mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty oranges
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

'''
Append:
When you write elements.append(i) you are actually setting off a chain of events inside Python to cause something to happen to the elements list. Here's how it works:
1. Python sees you mentioned elements and looks up that variable. It might have to look backward to see if you created with =, if it is a function argument, or if it's a global variable. Either way it has to find the elements first.
2. Once it finds elements it reads the . (period) operator and starts to look at variables that are a part of elements. Since elements is a list, it knows that elements has a bunch of functions.
3. It then hits append and compares the name to all the names that elements says it owns. If append is in there (it is) then Python grabs that to use.
4. Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.
5. That extra argument is ... elements! I know, weird, right? But that's how Python works so it's best to just remember it and assume that's the result. What happens, at the end of all this, is a function call that looks like: append(elements, 'i') instead of what you read which is elements.append('i').
Note: this info came from ex38, but its example was mystuff.append('hello')

Other things:
1. 2-dimensional list: [[1,2,3],[4,5,6]]

2. Are lists and arrays the same thing:
Depends on the language and the implementation. In classic terms a 
list is very different from an array because of how they're 
implemented. In Ruby though they call these arrays. In Python they 
call them lists. Just call these lists for now since that's what 
Python calls them.

3. Why does 'for i in range(1, 3):' only loop two times instead of three:
The range() function only does numbers from the first to the 
last, not including the last. So it stops at two, not three in 
the above. This turns out to be the most common way to do this 
kind of loop.
https://docs.python.org/2/library/functions.html#range

4. What does elements.append() do: simply appends to the end of the list.
