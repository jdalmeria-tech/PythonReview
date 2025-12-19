"""
Author: Your Name
Purpose: Apply input handling and string methods to create a clever/funny story generator.
"""
# Collect user inputs for the story
print("Please provide the following details to create your story:\n")
adj = input("Adjective: ")
animal = input("Type of Animal: ")
first_verb = input("Verb: ")
exclamation = input("Exclamation: ")
second_verb = input("Verb: ")
third_verb = input("Verb: ")

# Generate and display the story
print(f"\nYour story is:\n")

print(f'The other day, I was really in trouble. It all started when I saw a very\n{adj.lower().strip()} {animal.lower().strip()} {first_verb.lower().strip()} down the hallway. "{exclamation.capitalize().strip()}!" I yelled. But all\nI could think to do was to {second_verb.lower().strip()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {third_verb.lower().strip()}\nright in front of my family.')