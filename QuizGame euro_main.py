import random 
from euro_questions import euro_questions




print("Welcome to the computer quiz")

playing = input("Type yes to play: ")

if playing.lower().strip() != "yes":
    quit()

print("Let's Begin ")

# Turn the countrys into a list
countrylist = list(euro_questions.keys())

# Shuffle list of countries 
random.shuffle(countrylist)

incorrect_answers = []

score = 0 
current_index = 0


while len(countrylist) > current_index:
    current_country = countrylist[current_index]
    correct_answer = euro_questions[current_country]
    
    answer = input("What is the capital city of " + str(current_country) + " ")

    current_index += 1 

    if answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        incorrect_answers.append(current_country)



print("Game Over")

final_score = (score / (current_index )) * 100
print("Final Score " + str(final_score) + "%")


'''
The game is now over
Either the player got every question correct, in that case the game ends
If the player missed questions then we will give them the option to see the correct answer or try the missed questions again
'''

if len(incorrect_answers) == 0:
    print("You got every answer correct")
    print("WELL DONE!!!")
    exit() 


if final_score != 100:
    print("You missed " + str(len(incorrect_answers)) + " out of " + str(current_index) + " questions")


see_incorrect = input("To review missed questions type yes, if not type no: ")

if see_incorrect.lower().strip() == "yes":
    print("Incorrect Answers:")
    for items in incorrect_answers:
        print(items)
else:
    exit()


print("To see the correct answers type 'answers' ")
print("If you would like to re-attempt the missed questions type 'review' ")

review = input("Your choice: ")


# need to finish display of correct answers
if review.lower().strip() == "answers":
    print("Correct Answers")
    for items in incorrect_answers:
        correct_capital = euro_questions[items].capitalize()
        print("The Capital city of " + items + " is " + correct_capital)
       

'''
If the user chooses to try again at the review questions they continue below
The game only cycles through the questions the user got incorrect
'''

if review.lower().strip() == "review":

    random.shuffle(incorrect_answers)
    review_index = 0
    review_score = 0
    incorrect_review_answers = []

    while review_index < len(incorrect_answers):
        current_review_country = incorrect_answers[review_index]
        correct_review_answer = euro_questions[current_review_country]

        review_question = input("What is the capital city of " + str(current_review_country) + " ")
        review_index += 1

        if review_question.lower().strip() == correct_review_answer.lower():
            print("Correct!")
            review_score += 1
        else:
            print("Incorrect")
            incorrect_review_answers.append(current_review_country)

    print("Review Over")

    final_review_score = (review_score / (review_index )) * 100
    print("Review Score " + str(final_review_score) + "%")
    

    if final_review_score == 100:
        print("Second times the charm! Well Done!")
        exit()
    else:
        print("You missed " + str(len(incorrect_review_answers)) + " out of " + str(review_index) + " questions")
        print("Correct Answers")
        for i in incorrect_review_answers:
            correct_review_capital = euro_questions[i].capitalize()
            print("The Capital city of " + i + " is " + correct_review_capital)






