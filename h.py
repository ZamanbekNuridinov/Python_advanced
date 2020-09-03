a=int(input())
a1=int(input())

b=int(input())
b1=int(input())

c=int(input())
c1=int(input())

k = int((a-b)/(a1-b1))
b=a1-k*a
if(a1==b1):
    k==0
if(c==k*c1+b):
    print("point in the line")
if(c > k*c1+b):
    print("up")
else:
    print("down")