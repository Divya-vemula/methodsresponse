import re
txt = "The rain in 456 Spain  falls mainly in the plain!"
x = re.search("^The?.Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")


  #findall
x = re.findall("[a-m]", txt)
print(x)

#digit
x = re.findall("\d", txt)
print(x)

# spl char
x = re.findall("ra.n", txt)
print(x)


#Exactly the specified number of occurrences
x = re.findall("al{2}", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#alternative
x = re.findall("falls|stays", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Returns a match if the specified characters are at the beginning of the string
x = re.findall("\AThe", txt)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")

#Returns a match where the specified characters are at the beginning or at the end of a word
x = re.findall(r"\bain", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


#Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
x = re.findall(r"\Bain", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Returns a match where the string DOES NOT contain digits
x = re.findall("\D", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Returns a match where the string contains a white space character
x = re.findall("\s", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")


#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


x = re.findall("[4-6]", txt)
print(x)





