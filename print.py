from sys import exit
a=input()

if a.find('print(')==-1:
    print('IndexError')
    exit()

for i in range(len(a)):

    if (a[i:i+7]=="print('"):
        new_a=a[i+5:]
        if len(new_a)==2:
                print('IndexError')
                break
        for j in range(len(new_a)):
            if new_a[2]==" "or (new_a[j]=="'" and j-1==1):
                print("IndexError")
                break
            if new_a[j]=="'" and new_a[j+1]==")":
                print(new_a[2:j])
                break
# print(new_a)