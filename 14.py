num = int(input("Enter The Number : "))
str = str(num)	
arr = list(str)
arr.reverse()
str = ""
str = (str.join(arr))
rnum = int(str)
print("Reverse Of The Number :",rnum)