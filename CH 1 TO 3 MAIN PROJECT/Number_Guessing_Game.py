import random

# COMPUTER RANDOMLY PIC A ONE NUMBER BETWEEN 1 TO 100

random_number = random.randint(1 , 100)

print("🎯 Welcome To Number Guessing Game :-")
print("I'M thinking of a number between 1 to 100 , can you guess it?")


attempt = 0

while True:
    guess = int(input("Enter Your Guess :-"))
    attempt += 1

    if guess < random_number:
        print(f"Computer Number :- {random_number} You Choice Too Low Number! Try Again Higher Number  🔼" )

    elif guess > random_number:
        print(f"Computer Number :- {random_number} You Choice Too High Number ! Try Again Lower Number  🔽")

    else:
        print(f"🎉 Congratulation ! You Guessed it in {"attempts"} {attempt}")
        break