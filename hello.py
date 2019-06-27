#!/usr/bin/python

print 'Content-type: text/html'
print ''

# for i in range(11):
for i in range(5,11):
  print i
  print "Rob"

print "Sam"

list = ["pizza","chocholate","ice cream"]

print "<br>"
for food in list:
  print "I like eating " + food + "."
  print "<br>"


x = 0
while x <= 10:
  print x
  x = x + 1
  # x += 1
print "<br>"

ages = {}
ages["Rob"] = 35
ages["Kirsten"] = 36
ages["Tommy"] = 5
ages["Rophie"] = 1

for age in ages:
 print age + " is " + str(ages[age]) + "."