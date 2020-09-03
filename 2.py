login=["admin","admin1"]
password=["pass", "pass1"]

a=input()
b=input()

for i in range(len(login)):
    if(a==login[i] and b==password[i]):
        print("Welcome!")
        break
else:
    print("Not correct!")