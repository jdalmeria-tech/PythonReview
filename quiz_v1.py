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

score = 0 # initialize score and keep track of correct answers

# 2nd Loop thru each question
for q in questions:
  print(q["question"])
  user_answer = input("Your answer: ")

  # 3rd normalize input (lowercase and strip spaces)
  normalized_user_answer = user_answer.strip().lower()
  normalized_correct_answer = q["answer"].strip().lower()

  if normalized_user_answer == normalized_correct_answer:
    print(" ✅ Correct!\n")
    score += 1
  else:
    print(f" ❌ Incorrect! The correct answer is: {q['answer']}\n")

# 4th Final score display
print("Quiz Complete!")
print(f"You scored {score} out of {len(questions)}.")

percentage = (score / len(questions)) * 100
print(f"That's {percentage:.2f}%")