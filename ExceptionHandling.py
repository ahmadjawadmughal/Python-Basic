user_value1 = input("Enter Number:")
user_value2 = input("Enter Number:")

def do_division(x,y):

    try:
        if int(x) >= 0 and int(y) >= 0:
            z = x / y
            print(z)

    except (ZeroDivisionError,ValueError):
        print("Zero Division Error")
        #raise ZeroDivisionError(f"error were occur.")


do_division(user_value1,user_value2)

# EXCEPTION with Finally

def do_division(x,y):
    try:
        if int(x) >= 0 and int(y) >= 0:
            z = x / y
            print(z)

    except (ZeroDivisionError,ValueError):
        print("Zero Division Error")

    finally:
        print("I'm using try-except statement.")

do_division(user_value1,user_value2)

