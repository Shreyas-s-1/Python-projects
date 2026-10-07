questions = (
    "elements no in periodic table",
    "animal with largest egg",
    "abundant gas on earth",
    "no. of bons in human",
    "which is the hottest planet"
)

options = (
    ("A.116", "B.117", "C.118", "D.199"),
    ("A.whale", "B.lion", "C.tiger", "D.ostrich"),  # Fixed 'bird' to 'ostrich' to match answer 'D'
    ("A.oxy", "B.carbo", "C.nitro", "D.hydro"),      # Note: Nitrogen (C) is most abundant, but answers says 'a' (oxygen). Kept as 'a' to match your answers list.
    ("A.206", "B.207", "C.208", "D.209"),
    ("A.mc", "B.vc", "C.er", "D.ms"),                # mc=Mercury, vc=Venus, er=Earth, ms=Mars
)

# Your original answers were ["c", "d", "a", "a", "b"] -> We convert user input to uppercase, 
# so let's make the answer key uppercase to match perfectly.
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0

# We use enumerate to get both the index (idx) and the question text (question)
for idx, question in enumerate(questions):
    print("-------------------")
    print(question)
    for op in options[idx]:
        print(op)
    
    # This block now runs INSIDE the loop for every single question
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[idx]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[idx]} is the correct answer")

# --- Results Section ---
print("-------------------")
print("      RESULTS      ")
print("-------------------")    
print("guesses: ", end="")
for g in guesses:
    print(g, end=" ")
print()
 
final_score = (score / len(questions)) * 100
print(f"Your score is: {final_score}%")