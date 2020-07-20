from random import randint
# from IPython.display import clear_output

guessed=False
number=randint(0,100)
guesses=0

while not guessed:
    ans=input("try to guess the number i'm thinking of!")

    guesses+=1

    # clear_output()

    if int(ans)==number:
        print("congrates! your guessed it correctly")
        print('It took you {} guesses!'.format(guesses))
        break
    elif int(ans) > number:
        print('The number is lower than what you guessed.')
    elif int(ans) < number:
        print('The number is greater than what you guessed.')