class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):  #init两边各有两个下划线
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number=0                             #设定默认值相当于已经初始化，不必要包含在用户的输入之中
	def describe_restaurant(self):
		print(f'{self.restaurant_name}{self.cuisine_type}')
	def open_restaurant(self):       #方法定义时一定要加入形参self
		print('openning')
	def set_number(self,num):
		if num >= self.number:
			self.number = num 
		else:
			print('you have not root')
	def increas_number(self,num):
		if num >=0:
			self.number+=num
		else:
			print('you have not root')

my_restaurant = Restaurant('zbf','no')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increas_number(20)
print(my_restaurant.number)
my_restaurant.set_number(19)