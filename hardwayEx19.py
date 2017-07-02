def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a wet blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
che = 10
cra = 50
cheese_and_crackers(che, cra)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(che + 100, cra + 1000)
