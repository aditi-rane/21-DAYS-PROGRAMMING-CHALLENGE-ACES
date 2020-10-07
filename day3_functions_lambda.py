#FUNCTIONS

#---------------creating and calling function--------------------------
def my_function():
  print("Hello from a function")

my_function()

#---------------argument--------------------------
def my_function1(name):
  print("Hello "+name)

my_function1("Tulip")

#--------------number of argument------------------------
def my_function2(name1,name2):
  print("Hello "+name1+name2)

my_function2("Tulip",",Welcome!")

#--------------arbitrary arguments---------------------------
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Tulip", "Tobias", "Linus")

#--------------keyword arguments---------------------------
def my_function4(child3, child1, child2):
  print("The youngest child is " + child2)

my_function4(child1 = "Tulip", child2 = "Tobias", child3 = "Linus")

#----------------arbitrary keyword arguments-------------------------
def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")

#-----------------default parameter value------------------------
def my_function6(country = "Norway"):
  print("I am from " + country)

my_function6("Sweden")
my_function6("India")
my_function6()

#---------------passing list as argument--------------------------
def my_function7(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]

my_function7(fruits)

#-------------return value----------------------------
def my_function8(x):
  return 5 * x

print(my_function8(3))

#LAMBDA FUNCTIONS

x = lambda a:a+10
print(x(5))

#--------------------------------------------------
y = lambda a,b:a*b
print(y(5,6))

#--------------------------------------------------
z = lambda a,b,c:a+b+c
print(z(5,6,2))

#--------------------------------------------------
def myfunc(n):
  return lambda a:a*n
a=myfunc(2)

print(a(11))

#---------------lambdas in filter()---------------
li1=[5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li1))
print(final_list)

#---------------lambdas in map()---------------
li2=[5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li2))
print(final_list)

#---------------lambdas in reduce()---------------
from functools import reduce
li3=[5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li3)
print (sum)

