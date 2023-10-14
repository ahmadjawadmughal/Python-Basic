# annotation is basically used for the help of coders.

def add(num1:int,num2:int)->int:
    return num1 + num2

x = add(9.9,6.8)
print(x)
print(type(x))
print(add.__annotations__)


# divide function

def divide(num1:int,num2:int)->int:
    return num1 / num2

value = divide(10,2)
print("Divide value is :",value)


# LAMDA Function

# with parameter

add = lambda num1,num2: num1 + num2
x = add(7,8)
print(x)

# without parameter

message = lambda : "Hello World"
print(message())

myName = lambda : "AJM"
print("My name is:",myName())

# cube

cube = lambda num : num * num * num
value = cube(2)
print("Cube of 2:",value)

# multiply

multiply = lambda num1,num2 : num1*num2
value = multiply(2,2)
print(value)


"""LIST Comprehension"""

numbers = [1,1,3,4,5,6,8]

new_number = [num**2 for num in numbers if num % 2 == 0]
print(new_number)

list = ["ahmad","jawad","harry"]
new_list = [name.upper() for name in list if name.startswith("a") or name.startswith("h")]
print(new_list)


# getting alphabet

data = ["apple","1243","grape","banana","979","orange"]
word_only = [words for words in data if words.isalpha()]
print(word_only)

# for getting numbers

num_only = [number if number.isdigit() else "NaN" for number in data]
print(num_only)


# check greatest number in the list

list = [1,1,3,4,7,8,9]
greatestNumber = max(list)
print("The greatest number is:",greatestNumber)

# annotations

def mult(x:int,y:int)->int:
    return x*y

a = mult(2,3)
print(a)
print(type(a))
print(mult.__annotations__)


def division(x:int,y:int)->int:
    return x/y

result = division(10,5)
print(result)
print(type(result))
print(division.__annotations__)
