import random
n=random.randint(1,100)
a=-1
guesses=1
while a!=n:
    a=int(input("Enter the guess number:"))
    if a>n:
        print("Guess was too high...enter lower number")
        guesses = guesses + 1
    elif a<n:
        print("Guess was too low...enter upper number")
        guesses = guesses + 1
print(f"You guessed {guesses} times")
print("The number is :",n)
print("Thank you for playing")