import pandas as pd
import matplotlib.pyplot as plt

pd=pd.read_excel('Task_Python_Advanced.xlsx')
pd2=pd['USD/KZT']
a=[]

for i in range(len(pd2)-6):
    profit1=pd2[i+1]/pd2[i]
    profit2=pd2[i+2]/pd2[i]
    profit3=pd2[i+3]/pd2[i]
    profit4=pd2[i+4]/pd2[i]
    profit5=pd2[i+5]/pd2[i]
    if(profit1>1 and profit1>profit2 and profit1>profit3 and profit1>profit4 and profit1>profit5):
        a.append(profit1)
    elif(profit2>1 and profit2>profit3 and profit2>profit4 and profit2>profit5):
        a.append(profit2)
    elif(profit3>1 and profit3>profit4 and profit3>profit5):
        a.append(profit3)
    elif(profit4>1 and profit4>profit5):
        a.append(profit4)
    elif profit5>1:
        a.append(profit5)   

c=[]
for i in range(len(a)):
    c.append(i)
plt.plot(c,a,'b-')    

maxi=a[0]
n=0
b=[]
while n<3:
    for i in range(len(a)):
        if a[i]>maxi:
            maxi=a[i]
            index=i
    b.append(maxi)
    b.append(index)
    a.pop(index)
    maxi=a[0]
    n+=1
print(a)
print(b)
plt.scatter(b[1],b[0],s=20,color='red')
plt.scatter(b[3],b[2],s=20,color='red')
plt.scatter(b[5]+1,b[4],s=20,color='red')
a.clear()
sort=b[1]
n1=0
while n1<3:
    for i in range(len(b)//2-1):
        if b[2*i+1]<=sort:
            sort=b[2*i+1]
            index1=2*i+1
    a.append(b[index1-1])
    b.pop(index1)
    b.pop(index1-1)
    b.append(10**6)
    b.append(10**6)
    n1+=1
    sort=b[1]

b.clear()
total=1
for i in range(len(a)):
    total=total*a[i]
total=(total-1)*10**6
print(int(total))

# for i in range(1,len(pd2)+1):
#     b.append(i)
# plt.plot(b,pd2,'b-')
plt.show()