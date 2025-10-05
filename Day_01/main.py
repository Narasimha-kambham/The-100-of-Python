# This is a simple print statement to welcome the user.
print("Welcome to Band Name Generator")
# Prompt the user to enter the city they grew up in and store it in the 'city' variable.
city = input("What city did you grow up in?\n").capitalize()
# Prompt the user to enter their pet's name and store it in the 'pet' variable.
pet = input("What is your pet's name?\n").capitalize()
# Combine the city and pet's name to generate a band name and print it to the console.
print("Your band name could be " + city + " " + pet)
