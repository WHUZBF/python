#difine name
first_name = " bufan "
last_name = " zheng "
name = f"{last_name.strip()}{first_name.rstrip()}"     #use 'f'
#main codes
print(f"hello\t{name.title()}\n'may yuo be happy!'")

names=['bufan','wenjun',"haoming"]
print(names)    #"" will be changed into '' 
names.append('gaozhu')
names.insert(1,'dengfeng')
print(names)  
print(names[-1])
