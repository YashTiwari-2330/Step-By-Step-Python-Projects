import random

# Define the questions by difficulty
questions_easy = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 6"],
        "answer": "B"
    }
]

questions_medium = [
    {
        "question": "Which language runs in a browser?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What is the result of 3 ** 2?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "C"
    }
]

questions_hard = [
    {
        "question": "Who developed Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Linus Torvalds"],
        "answer": "B"
    },
    {
        "question": "Which year was Python first released?",
        "options": ["A. 1991", "B. 1989", "C. 2000", "D. 1995"],
        "answer": "A"
    }
]

# Get difficulty from user
def get_questions_by_difficulty():
    print("Select Difficulty Level: ")
    print("1. Easy\n2. Medium\n3. Hard")
    level = input("Enter 1/2/3: ")

    if level == "1":
        return random.sample(questions_easy, len(questions_easy))
    elif level == "2":
        return random.sample(questions_medium, len(questions_medium))
    elif level == "3":
        return random.sample(questions_hard, len(questions_hard))
    else:
        print("Invalid choice. Defaulting to Easy.")
        return random.sample(questions_easy, len(questions_easy))

# Function to calculate grade
def get_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"

# Function to run quiz
def run_quiz():
    questions = get_questions_by_difficulty()
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your Answer (A/B/C/D): ").upper()

        if user_ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {q['answer']}")

    total = len(questions)
    grade = get_grade(score, total)
    print(f"\n🎉 Quiz Completed!")
    print(f"Your Score: {score}/{total}")
    print(f"Percentage: {score / total * 100:.2f}%")
    print(f"Grade: {grade}")

# Start the Quiz
run_quiz()
