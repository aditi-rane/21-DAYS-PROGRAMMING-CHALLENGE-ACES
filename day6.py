#date time function

import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)
print(x)

print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))

#JSON

import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

y = json.dumps(x)
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))

#Math functions
import math
x = min(4, 10, 25)
y = max(5, 50, 25)
print(x)
print(y)

x = abs(-4.75)
print(x)

x = pow(2, 3)
print(x)

x = math.sqrt(81)
print(x)

x = math.ceil(2.6)
y = math.floor(2.6)
print(x)
print(y)

x = math.pi
print(x)

