#function id defined by key word def and can accept parameters and they return value to the caller using keyword return inside the function.
##code after return keyword don't get executed as function exits  once it encounter return statement

print("function to cube a number")

def cube(num):

    result=num*num*num
    return result
    print(result)

value=input("enter a number to be qubed: ")
num=int(value)
print(num)
result=cube(num)
print(result)

