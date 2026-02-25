password = 12
attempts = 3
score = 0
questions = [
    "1. What is the capital of France? ",
    "2. How many days are there in a week? ",
    "3. What is 5 + 7? ",
    "4. Which planet is known as the Red Planet? ",
    "5. What is the largest mammal?"]
answers = ["paris", "7", "12", "mars", "blue whale"]
for attempt in range(attempts, 0, -1):
    user_pass = int(input(f"Enter password: "))
    
    if user_pass == password:
        print("\nLogin successful! Starting quiz...\n")
        
        for i in range(len(questions)):
            print(questions[i])
            user_answer = input("Your answer: ").lower().strip(" ")
            
            if user_answer == answers[i]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! Correct answer is {answers[i]}\n")
            
            print(f"Your Score: {score}/{len(questions)}")

        print("YOUR RESULTS")
        print(f"Total Questions: {len(questions)}")
        print(f"Percentage: {(score/len(questions))*100:}%")
        break
    else:
        if attempt>=0:
            print(" Wrong password. Try again.\n")
            print(f'{attempt-1} attempt left')
        else:
            print(" Access denied. Too many failed attempts.")

print("\nGame ended.")