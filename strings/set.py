thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["black berry", "mango", "grapes"])
thisset.remove("banana")
thisset.discard("mango")
print(len(thisset))
x=thisset.pop()
for x in thisset:

    print(x)