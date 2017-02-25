import sys


print "name file : ", sys.argv[0]
for i in range (1, len(sys.argv)):
	print i, sys.argv[i]
rep()



def rep():
	print "fun"
