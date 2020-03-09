def is_even(n):
     return n%2==0
num=[1,5,2,8,9,7,6,4]

even =list(filter(is_even,num))
print(even)