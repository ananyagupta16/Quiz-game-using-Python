import random

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("Answer multiple-choice questions!")
    print("Let's see how much you know!\n")

def load_questions():
    # Add your own questions and answers here
    questions = [
        {"question": "What is the cube root of 27000?", "choices": ["A. 30", "B. 29", "C. 31"], "answer": "A"},
        {"question": "Who wrote 'Romeo and Juliet'?", "choices": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens"], "answer": "A"},
        {"question": "What is the largest mammal on Earth?", "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe"], "answer": "B"}
    ]
    return questions

def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Your answer: ").upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct! Well done!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")
        return 0

def play_quiz():
    display_welcome()
    questions = load_questions()
    score = 0

    for question in random.sample(questions, len(questions)):
        user_answer = ask_question(question)
        score += evaluate_answer(user_answer, question["answer"])

    print(f"Your final score: {score}/{len(questions)}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_quiz()
    else:
        print("Thank you for playing!")

# Start the quiz game
play_quiz()
