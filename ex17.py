from sys import argv
from os.path import exists #returns True if file exists

script, from_file, to_file = argv #from_file=test.txt/to_file=new_file.txt

print "Copying from %s to %s" % (from_file, to_file)

#in_file = open(from_file) #open test.txt put in variable in_file
#indata = in_file.read() #read what's in the in file put in variable indata
#The two files above is the original code, but nstead of the two lines above, 
#you can do:
indata = open(from_file).read() #if using this, have to comment out in_file.close() at the bottom

#length of the string in the file
print "The input file is %d bytes long" % len(indata)

#if output file (new_file.txt) is open, True/False
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input() #if RETURN, will proceed to next line

out_file = open(to_file, 'w') #open new_file.txt write it to variable
out_file.write(indata) #writed data from indata (test.txt) 

print "Alright, all done."

out_file.close()
#in_file.close()
