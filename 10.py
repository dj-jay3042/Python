marks = {}
marks["gujarati"] = 50
marks["english"] = 60
marks["science"] = 70
marks["social science"] = 80
marks["maths"] = 90
i = 0
sum = 0
for i in marks.values():
	sum = i + sum
per  = (sum * 100) / 500
print("Persantage Is : ",per) 