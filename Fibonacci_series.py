# To print the fibonacci series

print("Enter the number of terms in fibonacci series")

n = int(input())

x = [0,1]

if n > 2:
	for i in range(2, n):
		
		nextElement = x[i-1] + x[i-2]
		
		x.append(nextElement)

print("The fibonacci series is : ")

print(x)