import random
import time

# COMPUTER RANDOMLY PIC A ONE NUMBER BETWEEN 1 TO 100

def gussing_game():

      print("🎯 Welcome To Number Guessing Game :-")
      print("I'M thinking of a number between 1 to 100 , can you guess it?")


      random.seed(85)

      random_number = random.randint(1 , 100)

      attempt = 0

      while True:
          guess = int(input("Enter Your Guess :-"))
          attempt += 1

          if guess < random_number:
              print(f"Computer Number :- You Choice Too Low Number! Try Again Higher Number  🔼" )

          elif guess > random_number:
              print(f"Computer Number :- You Choice Too High Number ! Try Again Lower Number  🔽")

          else:
              print(f"🎉 Congratulation ! You Guessed it in {"attempts"} {attempt}")
              break

gussing_game()