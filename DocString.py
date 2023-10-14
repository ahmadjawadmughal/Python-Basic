def hello():
    """
My function display just Hello World
"""
    return "Hello World!"
print(hello())

print(hello.__doc__)

# built-in functions DocString is already available

print(print.__doc__)

# end Parameter
for var in range(11):

    print(var,end="              ")
