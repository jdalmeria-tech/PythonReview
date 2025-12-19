"""
This program will follow the iconic James Bond intro style
"Bond, James Bond."
It will print out the phrase in a stylized manner.
"""
# Get user input for first and last name
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = f"{first_name} {last_name}"
full_name = full_name.title()

# Display the iconic phrase
print(f"Your name is {last_name.title()}, {full_name}.")