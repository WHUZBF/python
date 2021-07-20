cities={
	'zhuhai' : {
		'country' : 'china',
		'population' : 10,
		'fact' : 'no'
	},
	'fronita' : {
		'country' : 'america',
		'population' : 9,
		'fact' : 'yes'
	}	
}
for city_name,city_items in cities.items():
	print(f"{city_name} is a city in {city_items['country']}")
	print(f"its population is {city_items['population']}")

As=[{'country' : 'china',
		'population' : 10,
		'fact' : 'no'},{
		'country' : 'america',
		'population' : 9,
		'fact' : 'yes'
	}	]
print(As[0]['fact'])