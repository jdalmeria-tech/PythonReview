"""
Author: Your Name
Purpose: Apply input handling and string methods to create a clever/funny story generator.
"""
# helper function that notices vowels
def get_article(word):
  """
  Returns 'an' if the word starts with a vowel, otherwise 'a'.
  """
  first_letter = word.strip().lower()[0]

  if first_letter in "aeiou":
    return "an"
  else:
    return "a"

# Collect user inputs for the story
print("Please provide the following details to create your story:\n")
adj = input("Adjective: ")
animal = input("Type of Animal: ")
first_verb = input("Verb: ")
exclamation = input("Exclamation: ")
second_verb = input("Verb: ")
third_verb = input("Verb: ")

# watches adjectives for vowel starts
adj_clean = adj.strip().lower()
article = get_article(adj_clean)

# Generate and display the story
print(f"\nYour story is:\n")

print(f'The other day, I was really in trouble. It all started when I saw a very\n{adj.lower().strip()} {animal.lower().strip()} {first_verb.lower().strip()} down the hallway. "{exclamation.capitalize().strip()}!" I yelled. But all\nI could think to do was to {second_verb.lower().strip()} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {third_verb.lower().strip()}\nright in front of my family.')
# additional functionality to add creativity
print(f"\nIt was {article} {adj_clean} moment that I will never forget!")