sandwich_orders = ['sb','sf','sb']
while 'sb' in sandwich_orders:
	sandwich_orders.remove('sb')
finished_sandwiches = []
while sandwich_orders:
	print('I made your tuna sandwich')
	finished_sandwiches.append(sandwich_orders.pop())

for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche)