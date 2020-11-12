# AUTHORS:
# Tom McLaughlin - thomas.mclaughlin@temple.edu
# Stylianos Dimitriadis
#   Digital Forensics, Fall 2020 - Cyber in a Box Assignment
#   Nov 8 2020
import json
from leaderboard import Leaderboard
import random

# Control the number of questions asked
num_questions = 15

# Read in the questions for the game
question_list = []
answer_list = []
with open("questions.json") as questions:
    question_json = json.load(questions)
    for question in question_json:
        question_list.append(question)
        answer_list.append(question_json[question])


# Read in the School ASCII Art and print it to the screen
school_logo = ''
with open("Ascii.txt") as Ascii:
    school_logo = Ascii.read()
print(school_logo)

# Initialize the leaderboard and print the first 5 scores
l1 = Leaderboard()
top_5_scores = l1.build()
if top_5_scores:
    print("The top {} players on this machine are:\n".format(len(top_5_scores)))
    [print(player) for player in top_5_scores]
    print()
else:
    print("You are the first player on this machine!")

# Prompt for this user's username
username = input("Please enter your username: ")
score = 0

# Loop over the number of questions that the user wants to do
for i in range(num_questions):
    question_index = random.randint(0,len(question_list)-1)
    userAnswer = input(question_list[question_index] + "\n")
    if userAnswer.lower() == answer_list[question_index].lower():
        print("correct!\n")
        score += 1
    else:
        print("incorrect :(\n")

# At the end of the game update the local leaderboard
l1.update(username, score)
exit(0)