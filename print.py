a=input()

for i in range(len(a)):
    if (len(a)<9):
        print("IndexError")
        break

    if (a[i]=='p' and a[i+1]=='r' and a[i+2]=='i' and a[i+3]=='n' and a[i+4]=='t' and a[i+5]=='(' and a[i+6]=="'"):
        new_a=a[i+5:]
        for j in range(len(a)):
            if new_a[2]==" "or (new_a[j]=="'" and j-1==1):
                print("IndexError")
                break
            if new_a[j]=="'" and new_a[j+1]==")":
                print(new_a[2:j])
                break
        break
else: 
    print("IndexError")
# print(new_a)