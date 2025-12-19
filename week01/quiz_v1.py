# quiz_v1

print("Welcome to your CS101 Quiz! 👨🏼‍💻")
print("Type your answer and press Enter. \n")

# 1st Questions stored in a list of dictionaries
questions = [
  {
    "question": "1. What does CPU stand for?",
    "answer": "central processing unit"
  },
  {
    "question":"2. In Python, what keyword is used to define a function?",
    "answer":"def"
  },
  {
    "question":"3. True or False: Python is a compiled language.",
    "answer":"false"
  },
]

while True: # adding this to allow retaking the quiz

  score = 0 # initialize score and keep track of correct answers

  # 2nd Loop thru each question
  for q in questions:
    print(q["question"])
    user_answer = input("Your answer: ")

    # 3rd normalize input (lowercase and strip spaces)
    normalized_user_answer = user_answer.strip().lower()
    normalized_correct_answer = q["answer"].strip().lower()

    # == means exact match changed to "in" which means is this contained inside
    if normalized_user_answer in normalized_correct_answer:
      print(" ✅ Correct!\n")
      score += 1
    else:
      print(f" ❌ Incorrect! The correct answer is: {q['answer']}\n")

  # 4th Final score display
  print("Quiz Complete!")
  print(f"You scored {score} out of {len(questions)}.")

  percentage = (score / len(questions)) * 100
  print(f"That's {percentage:.2f}%")

  # Ask if the user wants to retake the quiz
  play_again = input("\nDo you want to retake the game? (y/n): ").strip().lower()
  if play_again != 'y':
    print("Mahalo for playing and studying! Kitakits!")
    break