import io

nums=[]
for i in range(0, 5):
	nums += [int(raw_input())]
#print nums

hasOdd = 0
bigOdd = 0
for num in nums:
	if 1==num%2:
		hasOdd = 1
		if bigOdd == 0:
			bigOdd = num
		elif bigOdd < num:
			bigOdd = num
if hasOdd == 0:
	print "No Odd Number Given"
else:
	print "Biggest Odd Number Is : " + str(bigOdd)
