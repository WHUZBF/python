#version 1
seq=[1,1]
i=1
while i<2000000:
	seq.append(seq[0]+seq[1])
	i+=1
	seq=seq[-2:]                                            #保留前两个值，为下次计算做准备
print(seq)                                                  #优化后的代码在计算时摒弃之前的数据，使内存占用更少


#版本2
a,b=1,1
i=1
while i <= 2000000:
	a,b=b,a+b
	i+=1                        #使用迭代的方式，代码更秀
print(a)