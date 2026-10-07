import random

emojis = {"r": "rock 🪨", "p": "paper 📄", "s": "scissors ✂️"}
choices = ("r", "p", "s")

while True:

    hand = input("rock (r), paper (p), scissors (s), bitch: ").lower()

    if hand not in choices:
        print("Invalid choice! Try again.")
        continue
    
    com_hand = random.choice(choices)

    print(f"\nYou chose {emojis[hand]}")
    print(f"Computer chose {emojis[com_hand]}\n")

    if hand == com_hand:
        print("It's a tie! 👔")
    elif (
        (hand == "r" and com_hand == "s")
        or (hand == "s" and com_hand == "p")
        or (hand == "p" and com_hand == "r")
    ):
        print("You won! 🎉")
    else:
        print("You lost... 💀")

    continuess = input("\nWanna continue? (y/n): ").lower()
    if continuess == "n":
        print("Goodbye!")
        break