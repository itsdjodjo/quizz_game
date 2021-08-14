
import time
# this module allow me to separate the waiting time during the question
print("Welcome to my computer quizz!")

playing = input("Do you want to play? ")
score = 0  # we need to count the player's score

# here i have to use a method that allow the player answer to be true if he write "Yes" or "YES"
# so i'll use yhe method .lower()
if playing.lower() != "yes":
    quit()

print("Let's play !")
time.sleep(2)
print("Answer these question about general culture")


# Now i'll ask the question
answer = input("What CPU stand fo ? ")
if answer.lower() == "central processing unit":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)  # time.sleep make my game more fun
    print("The correct answer is : 'central processing unit'")


answer = input("Who's the first President of USA ? ")
if answer.lower() == "george washington":
    score += 1
    print("Correct")
else:
    print("Incorrect")

    time.sleep(2)  # time.sleep make my game more fun
    print("The correct answer is : 'george washington'")

print("Your Score is", score)
