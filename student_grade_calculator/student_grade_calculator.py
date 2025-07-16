name=input("Hey, friend! What is your name?")
print(f"Nice to meet you, {name}.")
sub_number=5
scores=[]

def score_input(number):
    for i in range(number):
        while True:
            try:
                score=int(input(f"Please, enter your score in the {i+1} subject:"))
                if  0<=score<=100:
                    scores.append(score)
                    break
                else:
                    print("Out of grading scale! Scores must be 0-100.")
            except ValueError:
                print("Please enter a valid number.")

score_input(sub_number)
arg_score=int(sum(scores)/len(scores))
print(f"Your average score: {arg_score}")
if arg_score<60:
    grade="F"
    message="Raise it!"
elif 60<=arg_score<70:
    grade="D"
    message="There is still room for growth."
elif 70<=arg_score<80:
    grade="C"
    message="Not bad. Keep improving!"
elif 80<=arg_score<90:
    grade="B"
    message="Good work!"
else:
    grade="A"
    message="Well done!"
print(f"Your avarage score is {grade}. {message}")


