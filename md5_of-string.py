import hashlib

string=input("Enter the string: ")

m=hashlib.md5()
m.update(string.encode('utf-8'))
print("MD5 Hash of "+string+" is "+m.hexdigest())