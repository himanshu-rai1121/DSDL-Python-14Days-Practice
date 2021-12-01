list = [18,20,8,16,4,10,12,3]
list.sort()
list.pop()
a=list.pop()
print(a)
c=0
while(a!=0):
    if(a%2==0):
        a=a/2
        c=c+1
    else:
        a=a-1
        c=c+1
print("no. of steps are",c)