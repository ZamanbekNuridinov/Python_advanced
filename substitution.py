s=input()
d=['q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.',' ']
t=['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','я','ч','с','м','и','т','ь','б','ю',' ']


def encode_decode(name):
    p=""
    for i in range(len(name)):
        for j in range(len(d)):
            if name[i]==d[j]:
                p=p+t[j]
            elif name[i]==t[j]:
                p=p+d[j]

    print(p)
encode_decode(s)
