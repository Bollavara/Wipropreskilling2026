n=[1,2,3,4,5,6,7,8,9,10]
a=filter(lambda x:x%2==0,n) #Even numbers
z=map(lambda x:x*x,a) #Square numbers
for num in z:
    print(num)