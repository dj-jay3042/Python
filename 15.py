num = int(input("Enter The Number : "))
str = str(num)	
arr = list(str)
sum = 0
for i in arr:
	sum += int(i)
print("Sum Of Digits Is :",sum)