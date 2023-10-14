"""
user_value = int(input("Enter number:"))

def prime_check(user_value):
    for i in range(1,user_value):
        if i % 2 != 0 and i % 3 != 0 and i % i == 0:
            print("Prime number:",i)

        return False

    return True


prime_check(user_value)
"""

"""
print pattern
"""
# user = int(input("Enter number:"))
"""
for i in range(user):
    for j in range(user):
        print("*",end=" ")
    print(" ")
        
"""
"""
for i in range(user):
    for j in range(i):
        print("*",end=" ")
    print(" ")


"""
"""
for i in range(user):
    for j in range(user-i):
        print("*",end=" ")
    print(" ")
"""
"""
for pyramid pattern
"""
"""
a =1
for i in range(user):
    for j in range(user-i):
        print(" ",end=" ")
    for z in range(a):
        print("*",end=" ")
        print(" ",end=" ")

    a += 1
    print(" ")
"""

# Dictionary

dict1 = {"A":526,"B":70,"C":90,"D":100}
print(dict1.items())
for key,value in dict1.items():
    print(key)

# Copy dict1

my_dictionary= dict1.copy()
print(my_dictionary)

