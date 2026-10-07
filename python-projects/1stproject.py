import random

while True:
    choice = input("Enter your choice (y/n): ").lower()
    
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}.")
    elif choice == "n":  
        print("You chose no. Goodbye!")  
        break
    else:
        print("Invalid input.")