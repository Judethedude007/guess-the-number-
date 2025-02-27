import random
print("welcome to the number guessing game")
print("you have to guess the number between the given range")
print("you have 5 chances to guess the number")
a=int(input("enter the lower limit:"))
b=int(input("enter the upper limit:"))
guess_no=random.randint(a,b)
for i in range(5):
    guess=int(input("enter the number:"))
    if guess==guess_no:
        print(f"congratulations! you have guessed the number in {i+1} attempts")
        break
    elif guess<guess_no:
        print("you have entered a smaller number")
    else:
        print("you have entered a larger number")
if guess!=guess_no:        
    print(f"your chances are over the number was {guess_no}")
print("game over")