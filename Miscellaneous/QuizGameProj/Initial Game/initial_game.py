print("Welcome to the computer quiz")

playing = input("Type yes to play: ")

if playing.lower().strip() != "yes":
    quit()

print("Let's Begin ")

score = 0
questions_asked = 0


Q = input("What is the capital of France? ")
questions_asked += 1 
if Q.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
   

Q = input("What is the capital of Spain? ")
questions_asked += 1 
if Q.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
   

Q = input("What is the capital of Greece? ")
questions_asked += 1 
if Q.lower() == "athens":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


Q = input("What is the capital of Russia? ")
questions_asked += 1
if Q.lower() == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

score_perc = (score / questions_asked) * 100


print("You Got " + str(score) + " Questions Correct!")
print("Thats: " + str(score_perc) + "%")

input("To review missed questions type yes:")

#if playing.lower().strip() == "yes":
    # Display incorrect answers
#else:
# quit()


