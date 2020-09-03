s=int(input())

h=int(s/3600)
m=int((s%3600)/60)
s1=int((s%3600)%60)

print("hour:", h, "minute:", m, "second:", s1)