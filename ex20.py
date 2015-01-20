from sys import argv #imports argv from sys module

script, input_file = argv #unpacks the startup arguments to script and input_file variables

#defines a function that uses the read() function on whatever is in the parameter(current_file in this case)
def print_all(f): 
    print f.read()

def rewind(f):
    f.seek(0) #seek goes back to the beginning of the file. Without it, you can only iterate through the file once.
    		      #The code seek(0) moves the file to the 0 byte (first byte) in the file (seek deals with bytes, not lines.

#sets a function that reads a line from the current_file
def print_a_line(line_count, f): 
    print line_count, f.readline()
    #Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file 
    #to return what it found so far. The file f is responsible for maintaining the current position in the file after each 
    #readline() call, so that it will keep reading each line.

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# the variable current_line is passed into the function, in that first parameter. as a result, 1 is printed
current_line = 1
print_a_line(current_line, current_file)

# now it will print 2 and that new value in the variable is passed into the function
current_line = current_line + 1
print_a_line(current_line, current_file)

# now it will print 3
current_line = current_line + 1
print_a_line(current_line, current_file)
