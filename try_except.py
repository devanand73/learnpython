# error handling in python

try:
#    value = 9 / 0
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
      print("number divided by 0 ")
except ValueError:
      print("invalid input")


