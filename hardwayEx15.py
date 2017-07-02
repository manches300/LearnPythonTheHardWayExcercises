# get the argv module
from sys import argv

# unpack the argument that was passed in.
script, filename = argv

# open the file that was passed in.
txt = open(filename)

# Tell the user what is about to happen.
print "Here's your file %r: \n" % filename

# print out the result of reading the file.
print txt.read()
# Close the file.
txt.close()


# Ask the user for the name of the file.
# **** NOTE ****
# This doesn't check to make sure it is the same file that
# was passed. The user can specify any file on the same path.
print "Type the filename again:"
file_again = raw_input(">>>>> ")

# put the resulting file
# into a variable. This does no checking to even see if
# the file exists.
txt_again = open(file_again)

# print out the content of the file.

print txt_again.read()
