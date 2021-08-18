
import time
# this module allow me to separate the waiting time during the question
print("Welcome to my computer quizz!")

score = 0
print("Let's play !")
time.sleep(2)
print("Answer these question about World Capitals")


# Now i'll ask the question
answer = input("What is the capital of India ? ")
if answer.lower() == "new delhi":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)  # time.sleep make my game more fun
    print("The correct answer is : 'new delhi'")


answer = input("Who's the first President of USA ? ")
if answer.lower() == "george washington":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'george washington'")

print("Who write one piece ? ", end=" ")
answer = input()
if answer.lower() == "oda":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Oda'")

print("You got " + str(score) + " question correct!")
