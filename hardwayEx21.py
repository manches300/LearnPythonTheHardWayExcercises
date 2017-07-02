def add(a,b):
    print "Adding %d and %d" % (a,b)
    return a+b
def sub(a,b):
    print "Subtracting %d and %d" % (a,b)
    return a-b
def mul(a,b):
    print "Multiplying %d and %d" % (a,b)
    return a*b
def div(a,b):
    print "dividing %d and %d" % (a,b)
    return a/b
print "Let's do math with functions!"

age = add(30, 5)
height = sub (78, 4)
weight = mul(90, 2)
iq = div(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# riddle me this
print "Here is a puzzle."

what = add(age, sub(height, mul(weight, div(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
