#!/usr/bin/python

#print("hello");


print list(range(0,100))



n = 100
sum = 0

for counter in range (1,n+1):
	print sum
	sum = sum + 1

print("Sum of 1 until %d: %d" %(n,sum))

x = range(1,101)

for count in x:
	print (count)


fibonacci = [0,1,1,2,3,5,8,13,21]
for i in range(len(fibonacci)):
    print(i,fibonacci[i])
print()
