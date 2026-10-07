import random

num_guess = random.randint(1, 100)
c=0
while True:
    try:
        choice = int(input("Enter your guess between 1 and 100: "))
        c=c+1
        if choice < num_guess:
            print('Too low!')
        elif choice > num_guess:
            print('Too high!')
        else:
            print("Success! You got it.")
            print(f"you took {c} guesses")
            break
    except ValueError:
        print("Invalid input. Please enter a proper number.")
        print(c)