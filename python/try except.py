#catching errors in python
#value = 10/0
try:
    #value = 10 / 0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("divided by 0")
except ValueError:
    print("invalid input")

try:
    value = 10 / 0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError as err:
        print(err)
except ValueError :
        print("invalid input")


