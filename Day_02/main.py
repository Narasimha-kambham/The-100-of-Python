# Welcome message for the Bill Splitter application
print("Welcome to The Bill Splitter with Tip !")

# Get user inputs for bill amount, tip percentage, and number of people
bill_amount = float(input("Enter the total Bill Amount: $ "))
tip_percentage = float(input("Enter the Tip Percentage(10,15,20 e.t.c.,) : \n"))
number_of_people = int(input("Enter the Number of People to Split the Bill: \n"))

# Calculate tip amount and total bill
tip_amount = (tip_percentage /100)* bill_amount
total_amount = bill_amount + tip_amount
# Calculate and round the amount each person should pay
amount_per_person = total_amount / number_of_people
amount_per_person = round(amount_per_person,2)

# Display the final amount each person should pay
print(f"Each person should pay: ${amount_per_person}")

