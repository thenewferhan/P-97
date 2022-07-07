import random

print("The Game")

number = random.randint(1,9)
chances = 0
print("Guess Number Between 1 and 9")
while chances < 5 :
    guess = int (input("Enter Your Guess : "))
    if guess == number:
        print("Congratulations You have Won")
        break
    elif guess < number : 
        print("Guess Is Lower Than Answer")
    else :
        print("Your Guess is too high")
    chances = chances+1
if not chances < 5 :
    print("You have Lost and The Number Is ",number)
