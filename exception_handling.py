user = input("Enter number:")
user1 = input("Enter number:")

def do_division(x,y):

    try:
        if int(x) >= 0 and int(y) >= 0:
            z = x/y
            print(z)

    except ZeroDivisionError:
        print("Denominator should not be zero.")

    except TypeError:
        print("Type Error")

    except ValueError:
        print("Value Error")

    finally:
        print("You are trying to divide the number.")

do_division(user,user1)









