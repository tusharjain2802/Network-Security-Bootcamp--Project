import hashlib
string=input("Enter the string: ")
md5=hashlib.md5()
sha1=hashlib.sha1()
sha224=hashlib.sha224()
sha256=hashlib.sha256()
sha384=hashlib.sha384()
sha512=hashlib.sha512()


md5.update(string.encode('utf-8'))
sha1.update(string.encode('utf-8'))
sha224.update(string.encode('utf-8'))
sha256.update(string.encode('utf-8'))
sha384.update(string.encode('utf-8'))
sha512.update(string.encode('utf-8'))

print("Result: ")
print("md5 Hash: "+md5.hexdigest())
print("sha1 Hash: "+sha1.hexdigest())
print("sha224 Hash: "+sha224.hexdigest())
print("sha256 Hash: "+sha256.hexdigest())
print("sha384 Hash: "+sha384.hexdigest())
print("sha512 Hash: "+sha512.hexdigest())