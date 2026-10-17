# argument data type does not bother
# a function can have unlimited no. of arguments
"""
Type 1: normal function with no return type and no parameters
Type 2: function with parameter and no return type
Type 3: function with parameter and return type
Type 4: function without parameter and return type
"""
def greet1(): # no parameter no return
    print("Hello")

def greet2(name): # with parameter no return
    print("Hi",name)
def greet3(name): # with parameter and returns
    return "Hello "+name
def greet4(): # no parameter and returns
    return "Hi"
greet1()
greet2("Sruti")
print(greet3("Khare"))
print(greet4())

