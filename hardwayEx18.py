# this one is for an unknown number of args I think
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# better to just do this if the arg number is known
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# single arg
def print_one(arg1):
    print "arg1: %r" % arg1

# no arg
def print_none():
    print "I'm so lonesome..."

# for the fun part... calling the functions!!!

print_two("Lawney","Deasy")
print_two_again("Lawney","Deasy")
print_one("Bling")
print_none()
