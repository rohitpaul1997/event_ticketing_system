
import bcrypt


print("input password: ")
password = input()

password = password.encode('utf-8')

hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt(10))
print(hashedPassword)

check = str(input("check password: ")) 
 
check = check.encode('utf-8') 
 
if bcrypt.checkpw(check, hashedPassword):
    print("login success")
else:
    print("incorrect password")