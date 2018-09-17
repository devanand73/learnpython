# while loop is used to loop through a set of code till condition is true and exits loop when it turns false

# i = 0
# while i <= 10:
#     print(i)
#     # increments i by 1 i.e i=i+1
#     i += 1
#
# print('done with loop')

secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit :
        guess = input("enter your guess word: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
        print("Sorry!, you are out of gusses")
else:
        print("you win!")
