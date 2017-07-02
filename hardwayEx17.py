from sys import argv
from os.path import exists

script, from_file, to_file= argv

print "Coping from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)

print "Does the outfile exist? %r" % exists(to_file)
print "Ready, hit RETurn to continue or CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "All Done!"

out_file.close()
in_file.close()
