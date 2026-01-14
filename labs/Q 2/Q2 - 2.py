#Set comprehension
data=[1,2,3,4,5,6,2,4]
c={x for x in data if x%2==0}
print(c)