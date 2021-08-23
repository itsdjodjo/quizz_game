
import time
# this module allow me to separate the waiting time during the question
print("Welcome to my computer quizz!")

score = 0
print("Let's play !")
time.sleep(1)
print("Answer these question about World Capitals")

questions = ["What is the capital of UK ? ", "What is the capital of Canada ? ", "What is the capital of Portugal ? ",
             "What is the capital of Brazil ? ", "What is the capital of Japan ? ", "What is the capital of Spain ? ",
             "What is the capital of South Korea ? ", "What is the capital of China ? ", "What is the capital of Morroco ? ",
             "What is the capital of France ? "]

answers = ["london", "toronto", "lisbonne", "brasilia",
           "tokyo", "manchester", "seoul", "beijing", "rabat", "paris"]

a = 0
b = 0
for question in questions:
    answer = input(questions[a])
    if answer.lower() == answers[b]:
        score += 1
        print("True")
    else:
        print("False")
        time.sleep(1)
        print("The correct answer is : " + answers[b].capitalize())
    a += 1
    b += 1
    
see = input("Do you want to see yout score ? ")
if see.lower() == "yes":
    print("You got " + str(score) + " /", len(questions), " correct answer")
else:
    quit()
