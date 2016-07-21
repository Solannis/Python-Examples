#!/usr/bin/python

# Open a file for writing
writeString = "This is text for the file writing and reading test."
writeFile = open("text.txt", "wb")
print "Name of the file: ", writeFile.name
print "Closed or not: ", writeFile.closed
print "Opening mode: ", writeFile.mode
print "Softspace flag: ", writeFile.softspace
print "Writing content to file: ", writeString
writeFile.write(writeString)
writeFile.close()

readFile = open("text.txt", "rb")
print "Name of the file: ", readFile.name
print "Closed or not: ", readFile.closed
print "Opening mode: ", readFile.mode
print "Softspace flag: ", readFile.softspace
readString = readFile.read(100)
print "Reading content from file: ", readString
readFile.close()