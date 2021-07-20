#kill_list=['green','red','yellow','red']
kill_list=[]
score=[]

if kill_list:  #检查列表是否为空
	for kill in kill_list:

		if 'green' == kill:
			score.append(10)
		elif 'red' == kill:
			score.append(20)
		elif 'yellow' == kill:
			score.append(30)
	print(f"you have killed {len(kill_list)} ,you can get {sum(score)}")
else :
	print("you need more exercise!")
		
