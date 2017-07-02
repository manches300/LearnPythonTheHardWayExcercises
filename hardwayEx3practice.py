# Find something you need to calculate and write a new
# .py file that does it for you

print ""
print "Paint Calculator for house exterior."

print ""
window = 3.0*3.0
windows = 18.0*window
houselen = 80.0
housewid = 40.0
housearea = (houselen+housewid)*2.0*12.0 - windows
print "My house is ", housearea, " sq ft."
print ""
print "At 300sqft per gallon I will need ", housearea/300.0, " gallons."
