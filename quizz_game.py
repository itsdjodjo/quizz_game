
import time
# this module allow me to separate the waiting time during the question
print("Welcome to my computer quizz!")

print("Let's play !")
time.sleep(2)
print("Answer these question about World Capitals")


# i need to put question in a list
# and answer in a list too
questions = ["What is the capital of India ? ", "What is the capital of Canada ? ", "What is the capital of USA ? ",
            "What is the capital of Brazil ? ", "What is the capital of Japan ? ", "What is the capital of Spain ?",
            "What is the capital of South Korea ? ", "What is the capital of China ? ",
            "What is the capital of Marroco ? ", "What is the capital of France ? "]

answers = ["new delhi", "toronto", "washington dc", "brasilia",
           "tokyo", "manchester", "seoul", "beijing", "rabat", "paris"]

# now i have to creat a loop
i = 0
a = 0
score = 0
for question in questions:
    answer = input(questions[i])
    if answer.lower() == answers[a]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        time.sleep(1)
        print("the correct answer is " + answers[a])
    i += 1
    a += 1

time.sleep(2)
see = input("Do you want to see your score ? ")
if see.lower() == "yes":
    print("You got " + str(score) + " /", len(questions), " question correct!")
else:
    quit()
