#1
x = 5
y = "John"
print(x)
print(y)

#2
a = 4
A = "Sally"
#A will not overwrite a

#3
#legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#4
q = w = e = "orange"
print(q)
print(w)
print(e)

#5
z = "awesome"

def myfunc():
  z = "fantastic"
  print("Python is " + z)

myfunc()

print("Python is " + z)