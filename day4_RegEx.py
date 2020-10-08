import re

#findall() function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#search() function
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print(x)

#split() function
x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

#sub() function
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

#Metacharacters
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

txt = "hello world"
x = re.findall("he..o", txt)
print(x)

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

x = re.findall("world$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", txt)
print(x)

x = re.findall("aix+", txt)
print(x)

x = re.findall("al{2}", txt)
print(x)

x = re.findall("falls|stays", txt)
print(x)

#Special Sequences
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)

x = re.findall(r"\bain", txt)
print(x)

x = re.findall(r"\Bain", txt)
print(x)

x = re.findall("\d", txt)
print(x)

x = re.findall("\D", txt)
print(x)

x = re.findall("\s", txt)
print(x)

x = re.findall("\S", txt)
print(x)

x = re.findall("\w", txt)
print(x)

x = re.findall("\W", txt)
print(x)

x = re.findall("Spain\Z", txt)
print(x)

#Sets
x = re.findall("[arn]", txt)
print(x)

x = re.findall("[a-n]", txt)
print(x)

x = re.findall("[^arn]", txt)
print(x)

x = re.findall("[0123]", txt)
print(x)

txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)
print(x)

x = re.findall("[0-5][0-9]", txt)
print(x)

x = re.findall("[a-zA-Z]", txt)
print(x)

x = re.findall("[+]", txt)
print(x)
