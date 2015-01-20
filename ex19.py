def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#this will temp substitute these variables within the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this will use the original variables in the function
#first addition is cheese_count
#second addition is boxes_of_crackers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#this will temp subsitute these variables within function
#will take the amounts 10 and 50 from above and add the new numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
