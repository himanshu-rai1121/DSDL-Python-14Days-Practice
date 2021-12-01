list=[18,20,8,16,4,10,12,3] 
list.sort()
print(list)
num=list[-2]
print(num)
count=0
while(num!=0):
    if num%2==0:
        num=num/2
    else:
        num=num-1
    
    count+=1
    print(num)
print("min no of step:",count)
#task 1