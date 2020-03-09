from functools import reduce

num=[1,2,3,4,0,9]
even=list(filter(lambda n:n%2==0,num))

#double
double=list(map(lambda n:n*2,even))

#reduce
sum=reduce(lambda a,b:a+b,double)

print(sum)




