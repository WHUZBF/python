age = 1
while age != 0:
	age =input('please enter your age :(enter 0 to leave)')
	age = int(age)
	if age == 0:
		break
	if age<3:
		money = 'free'
	elif 3<=age<=12:
		money = 10
	else:
		money = 15
	print(money)
ages=[1]
while ages:
	print(