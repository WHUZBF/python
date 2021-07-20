numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers)
numbers_2=list(range(1,11))

for number in numbers_2:
	cube=number**3
	print(cube)

numbers_3=[num**3 for num in range(1,11)]                           #列表解析版
print(numbers_3)

print(numbers_3[0:3:2])

print("the first three items in the list are")
print(numbers_3[0:3])
