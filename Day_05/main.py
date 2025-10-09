import random

# Alphabets
alphabets = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# Numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Common Symbols
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=']

number_of_characters = int(input("How many characters do you want in your password? "))
number_of_numbers = int(input("How many numbers do you want in your password? "))
number_of_symbols = int(input("How many symbols do you want in your password? "))
if number_of_characters < number_of_numbers + number_of_symbols:
    print("You can't have more numbers and symbols than the number of characters")
    exit()
randomize_the_password = int(input("Do you want to randomize the password? \n 1- Yes \n 2- No \n"))

if randomize_the_password == 1 :
    password_list=[]
    for i in range(0,number_of_characters-number_of_numbers-number_of_symbols):
        password_list.append(random.choice(alphabets))
    for i in range(0,number_of_numbers):
        password_list.append(random.choice(numbers))
    for i in range(0,number_of_symbols):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    password = "".join(password_list)
    
elif randomize_the_password == 2:
    password = ""
    for i in range(0,number_of_characters-number_of_numbers-number_of_symbols):
        password = password + random.choice(alphabets)  
    for i in range(0,number_of_numbers):
        password = password + random.choice(numbers)
    for i in range(0,number_of_symbols):
        password = password + random.choice(symbols)
else:
    print("You must choose 1 or 2")
    exit()

print(password)



