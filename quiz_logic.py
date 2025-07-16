import random

def play_quiz(questions):
    random.shuffle(questions)
    score = 0
    for i, q in enumerate(questions):
        print(f"Question #{i + 1}: {q['Q']}")
        user_input = input("Enter your answer (1-4): ")
        if user_input == q["correct"]:
            score += 10000
            print("\n🎉 Woppie!! Correct Answer!!")
            print(f"💰 Your money is: {score}\n")
        else:
            print("\n❌ Oops!! Wrong Answer....Better luck next time!!")
            print(f"💸 Your total money is: {score}")
            return
