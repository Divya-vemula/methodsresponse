# Passing lists and individual list elements to functions.
def modifyList(aList):
    for i in range( len( aList) ):
        aList [ i ] *= 2
def modifyElement( element ):
    element *= 2
aList = [1, 2, 3, 4, 5]
print("Effects of passing entire list:")
print("The values of the original list are:")
for item in aList:
    print(item,end=" ")
modifyList( aList )
print("\n\nThe values of the modified list are:")
for item in aList:
    print(item,end=" ")
print("\n\nEffects of passing list element:")
print("aList[ 3 ] before modifyElement:", aList[ 3 ] )
modifyElement( aList[ 3 ] )