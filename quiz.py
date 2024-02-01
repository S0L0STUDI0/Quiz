#   _  _    _____       _       _____ _             _ _       
# _| || |_ / ____|     | |     / ____| |           | (_)      
#|_  __  _| (___   ___ | | ___| (___ | |_ _   _  __| |_  ___  
# _| || |_ \___ \ / _ \| |/ _ \\___ \| __| | | |/ _` | |/ _ \ 
#|_  __  _|____) | (_) | | (_) |___) | |_| |_| | (_| | | (_) |
#  |_||_| |_____/ \___/|_|\___/_____/ \__|\__,_|\__,_|_|\___/  

import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def main():
    score = 0
    for _ in range(5):
        num1, num2 = generate_question()
        answer = int(input(f"What is the sum of {num1} + {num2}? "))
        if answer == num1 + num2:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"You scored {score} out of 5.")

if __name__ == "__main__":
    main()
    
#Developed in 2023 - SoloStudio
#SoloStudio
