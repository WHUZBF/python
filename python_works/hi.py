#lists=['zhengbufan','zhangwenjun','admin','luohaoming','lizhoubo']
lists=[]

if lists:
	for who in lists:	
		if who =='admin':
			print('hello admin,would you like to see a status report?')
		else:
			print('Hello Jaden,thank you for logging in again')

else:
	print('who need to find some users')


current_users=['zhengbufan','zhangwenjun','admiN','luohaoming','lizhoubo']
new_users=['zhangzixuan','Admin','xieyuhang','luohaoming','luokaiyue']
new_current_users=[]
for current_user in current_users:
	new_current_users.append(current_user.lower())
for new_user in new_users:
	if new_user.lower() in new_current_users:
		print('sorry')
	else:
		print('good')


numbers=list(range(1,10))
for number in numbers:
	if number == 1 :
		print('1st')
	elif number == 2 :
		print('2st')
	elif number == 3 :
		print('3rd')
	else:
		print(f'{number}th')

num = ['1']
if 1 in num :
	print('good')

