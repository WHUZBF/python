#ONE
'''def display_message():
	print('sb')
display_message()

def favorite_book(title):
	print(f"my favorit book is {title}")
favorite_book(input('enter'))''' 

#TWO
'''def city_country(name,country):
	print(f'{name},{country}')

name=input('name:')
country=input('country:')
city_country(name,country)'''

#THREE
def make_album(name,album,num=None):
	album={'name':name,'album':album}
	if num:
		album['num']=num
	return album

'''while True:
	name=input('name:')
	if name == 'q':
		break
	album=input('album:')
	if album == 'q':
		break
	num=input('num:')
	if num == 'q':
		break
	dictionary = make_album(name,album,num)
	print(dictionary)'''



