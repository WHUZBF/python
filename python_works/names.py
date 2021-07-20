names=['bu fan ',' wen jun','hao ming ']
absent=names.pop(2)
print(f"now we hear that {absent.title().strip()} can't enjoy our dinner")
del names[1]
print("there must be something going wrong! only one left!")
print(names)
sb='bu fan '
names.remove(sb)
print(f"ok {sb.title()} also has gone!")
print(names)