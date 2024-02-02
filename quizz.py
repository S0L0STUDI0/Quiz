#   _  _    _____       _       _____ _             _ _       
# _| || |_ / ____|     | |     / ____| |           | (_)      
#|_  __  _| (___   ___ | | ___| (___ | |_ _   _  __| |_  ___  
# _| || |_ \___ \ / _ \| |/ _ \\___ \| __| | | |/ _` | |/ _ \ 
#|_  __  _|____) | (_) | | (_) |___) | |_| |_| | (_| | | (_) |
#  |_||_| |_____/ \___/|_|\___/_____/ \__|\__,_|\__,_|_|\___/  

import random

def generate_equation():
    var = random.choice(['x', 'y', 'z'])
    coeff = random.randint(1, 10)
    c = random.randint(-10, 10)
    operator = random.choice(['+', '-'])
    rhs = random.randint(1, 10)
    if operator == '+':
        lhs = coeff * rhs - c
    else:
        lhs = coeff * rhs + c
    equation = f"{coeff}{var} {operator} {c} = {lhs}"
    return equation, rhs

def main():
    print("Welcome to Algebra Quiz.")
    print("Solve for the variable in the following equation:")

    equation, correct_answer = generate_equation()

    print(equation)

    user_answer = input("Your answer for the variable: ")

    try:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
#Developed in 2024 - SoloStudio, GPT3.5
#SoloStudio
