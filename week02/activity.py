"""
Author: Joseph Almeria
Purpose: Practice using mathematical expressions in Python.
"""

age = int(input("How old are you? "))
age_next_year = age + 1
print(f"On your next birthday, you will be {age_next_year} years old.\n")

egg_cartons = int(input("How many egg cartons do you have? "))
eggs_per_carton = 12
total_eggs = egg_cartons * eggs_per_carton
print(f"You have a total of {total_eggs} eggs.\n")

cookies = int(input("How many cookies do you have? "))
cookies_per_person = int(input("How many people are there? "))
cookies_shared = cookies / cookies_per_person
print(f"Each person gets {cookies_shared:.2f} cookies.")