import math
flag=True
#定义题中所说的两个函数
def f(n):
	N=n**0.5  
	output = 0
	if math.ceil(N)==math.floor(N): #调用math模块中的取整函数
		output = N
	else:
		output = 1+f(n+1)
	return output

def g(n):
	N=n**0.5  
	output = 0
	if math.ceil(N)==math.floor(N): 
		output = N
	else:
		output = 2+g(n+2)
	return output
i=1    #初始化i

while flag:
	if f(i)/g(i)==4/7 :
		print(f'The answer is {i}')
		decision=input('是否要继续计算？y or n')
		if decision == 'y':
			i+=1
			continue
		else :
			flag = False
	else:
		i+=1  #结果是258
	




