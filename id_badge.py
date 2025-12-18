# simple id badge generator

print("Please enter the following information to generate your ID badge.")

first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
job_title = input("Job Title: ")
id_number = input("ID Number: ")

print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last_name.upper().strip()}, {first_name.title().strip()}")
print(f"{job_title.title().strip()}")
print(f"ID: {id_number.strip()}\n")
print(f"{email.lower().strip()}")
print(f"{phone.strip()}")
print("----------------------------------------")