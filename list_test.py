#!/usr/bin/python

class test:
    def __init__(self):
        self.name = ""
        self.code = ""
        

list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]
print len(list)
list2 = []
print list2
list2.append("Test")
print list2
list2.append(49)
print list2

list3 = []
print len(list3)

myTest = test()
myTest.name = "Fred"
myTest.code = "HPL1"

list3.append(myTest)

print len(list3)

newTest = list3[0]

print newTest.code