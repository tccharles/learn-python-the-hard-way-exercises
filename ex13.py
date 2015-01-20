from sys import argv

#This line says, Take whatever is in argv, unpack it, and assign 
#it to all of these ariables on the left in order."
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "%s ran this script." % (name)
