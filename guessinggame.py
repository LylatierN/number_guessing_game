import random
import time

DIFFICULTY_CHANCE = {'1': 10, '2': 5, '3': 3,}
DIFFICULTY_NAME = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}

highscore = {'1': 0, '2': 0, '3': 0}
answer = 0
time_start = time.time()


def check_greater_lesser(number):
    if number > answer:
        return "less"
    if number < answer:
        return "greater"
    return None

def register_score(score, diff):
    if score > DIFFICULTY_CHANCE[diff]:
        return None
    if score == 0:
        return None
    if score >= highscore[diff] > 0:
        return None
    highscore[diff] = score
    return None

def display_highscore():
    print("HIGH SCORE:")
    for key, value in highscore.items():
        print(f"{DIFFICULTY_NAME[key]}: {value}")


def guesser(attempts):
    time_start = time.time()
    for a in range(1,attempts+1):
        guess = int(input(f"Attempt {a}: Enter your guess: "))
        if guess == answer:
            print(f"Congratulations, you guessed the correct number in {a} attempts and take only {time_takes():.2f} seconds!")
            return a
        print(f"Incorrect! The number is {check_greater_lesser(guess)} than {guess}.")

    print(f"Sorry you use all your attempts. The correct number is {answer}.")
    return attempts+1

def time_takes():
    return time.time()-time_start

def check_continue():
    ans = input("Would you like to continue (y/n)? ")
    if ans == "y" or ans == "Y" or ans == "Yes":
        return True
    return False

def main():
    global answer
    cont = True
    while cont:
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
        print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
        choice = input("Enter your choice(q for quit): ")
        while choice != 'q' and choice != 'quit' and choice not in DIFFICULTY_CHANCE:
            print(f"Sorry, the difficulty level {choice} is not available.")
            choice = input("Enter your choice(q for quit): ")
        if choice == 'q' or choice == 'quit':
            print("Thank you for playing!")
            break

        print(f"Great! You have selected the {DIFFICULTY_NAME[choice]} difficulty level.")
        print("Let's start the game!")
        answer = random.randint(1,100)
        scores = guesser(DIFFICULTY_CHANCE[choice])
        register_score(scores, choice)
        print("-"*20)
        display_highscore()
        cont = check_continue()
        print("-"*20)


if __name__ == '__main__':
    main()




