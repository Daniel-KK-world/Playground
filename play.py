def quiz_game():
    print("Welcome to the Quiz Game!")
    questions = {
        "What is the capital of France? ": "Paris",
        "What is 2 + 2? ": "4",
        "What is the largest planet in our solar system? ": "Jupiter"
    }
    
    score = 0
    
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.")
    
    print(f"Your final score is {score} out of {len(questions)}.")

# Call the function to actually run the game
quiz_game()