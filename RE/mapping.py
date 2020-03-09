

nums = [0, 4, 7, 2, 1, 0 , 9 , 3, 5, 6, 8, 0, 3]
nums = list(map(lambda x : x % 2, nums))
print(nums)
#[0, 4, 2, 2, 1, 0, 4, 3, 0, 1, 3, 0, 3]



def even (x):
 if (x % 2 == 0):
    return "even"
 else:
    return "odd"
list (map(even, nums)