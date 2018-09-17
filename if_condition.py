## if ---elseif---else conditions in python

is_male=False
is_tall=True

# if is_male:
#     print("you are a male")
# else:
#     print("you are not a male")

# if is_male or is_tall:
#         print("you are a male or you are tall or both")
# else:
#         print("you are neither male nor tall")

# if both conditions are true
if is_male and is_tall:
        print("you are a tall male")
#if one is true and other is false
elif is_male and not(is_tall):
        print("you are short male")
elif not(is_male) and is_tall:
        print("you are nota male but tall")

#if both conditions are false
else:
        print("you are either not male or tall or both")