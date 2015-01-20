from sys import argv

script, filename = argv #uses argv to get a filename

txt = open(filename) #does NOT return contents of file, but makes
#something called a "file object."

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
