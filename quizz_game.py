
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
    print("The correct answer is : 'New Delhi'")


answer = input("What is the capital of Canada ? ")
if answer.lower() == "toronto":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Toronto'")


print("What is the capital of USA ? ", end=" ")
answer = input()
if answer.lower() == "washington dc":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Washington DC'")


answer = input("What is the capital of Brazil ? ")
if answer.lower() == "brasilia":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Brasilia'")


answer = input("What is the capital of Japan ? ")
if answer.lower() == "tokyo":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Tokyo'")


answer = input("What is the capital of Spain ?")
if answer.lower() == "manchester":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Manchester'")


answer = input("What is the capital of South Korea ? ")
if answer.lower() == "seoul":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Seoul'")


answer = input("What is the capital of China ? ")
if answer.lower() == "beijing":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Beijing'")


answer = input("What is the capital of Marroco ? ")
if answer.lower() == "rabat":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Rabat'")


answer = input("What is the capital of Senegal ? ")
if answer.lower() == "dakar":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)
    print("The correct answer is : 'Dakar'")


print("You got " + str(score) + " question correct!")
