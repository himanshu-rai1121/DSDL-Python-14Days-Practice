from types import EllipsisType


list = [18,20,8,16,4,10,12,3]
list.sort()
a = list[-2]
count  =0 
while(a != 0):
    if a%2 == 0:
        a/= 2
        count+= 1
    else:
        a-= 1
        count += 1 
print(count)           