num = int(input("Enter THe Number : "))
sum = 0
for i in range(num+1):
	if i % 2 == 0:
		sum = sum + i
print("Sum Of ",num," Natural Even Numbers Is : ",sum)