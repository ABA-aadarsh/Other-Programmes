import random
import time
hL=int(input("Enter the higher limit: "))
global the_num
the_num=random.randint(1,hL)
print(f"The number choosen is {the_num}")
def make_guess(l,h):
    guess=int((l+h)/2)
    return guess
def complement(guess):
    if guess>the_num:
        return "go lower"
    elif guess<the_num:
        return "go higher"
    else :
        return "correct guess"
counter=0 
guess="!" 
l=1
h=hL
while guess!=the_num:
    guess=make_guess(l,h)
    counter+=1
    c=complement(guess)
    print(f"Guess {counter} : {guess}, {c},l={l} and h={h}")
    if c=="go lower":
        if l!=guess:
            h=guess
        else:
            h=guess
            l=1
    elif c=="go higher":
        if h!=guess:
            l=guess
        else:
            l=guess
            h=hL
    else:
        break
    time.sleep(0.75)
print(f"The number was {the_num} and the computer guessed it in {counter} guesses.")
a=input("")
    
