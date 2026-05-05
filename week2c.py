def dup(d):
    d1=[]
    for i in d:
        if d.count(i) >1 and i not in d:
            d1.append(i)
    print("the duplicate elements are :- ")
    print(d1)
def uni(u):
    u1=[]
    for i in u:
        if u.count(i)==1:
            u1.append(i)
    print("the uniq elements elements are :- ")
    print(u1)

li=list(map(int,input("enter your elements hear").split()))
dup(li)
uni(li)