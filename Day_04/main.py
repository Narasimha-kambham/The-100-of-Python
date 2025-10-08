import random

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock_art, paper_art, scissors_art]

# Game introduction
print("Welcome To Rock Paper Scissors Game")
print("Choose Your Move: 1 - Rock\n2 - Paper\n3 - Scissors")

# Get computer's choice
c = random.randint(0, 2) # Changed to 0-indexed for list

# Get player's choice
i = int(input("Enter Your Move: ")) - 1 # Changed to 0-indexed for list

# Display player's choice
print("You chose:")
if i >= 0 and i <= 2:
    print(game_images[i])
else:
    print("Invalid choice. You lose!")
    exit()

# Display computer's choice
print("Computer chose:")
print(game_images[c])

# Determine the winner
if i == c:
    print("It's a draw!")
elif (i == 0 and c == 2) or \
     (i == 1 and c == 0) or \
     (i == 2 and c == 1):
    print("You win!")
else:
    print("You lose!")
