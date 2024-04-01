#Steven Velez
#03/29/2024
#P4HW1

#Tell the user to enter their scores.

num_scores = int(input("Hi! Enter the number of scores or grades you want to enter: "))

#Start to initialize empty list for scores.

scores_list = []

#Do the loop to collect scores.

for i in range(num_scores):
    score = float(input(f"Enter your score {i+1}: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input(f"Enter your score {i+1}: "))
    scores_list.append(score)
print(scores_list)

#Look for the lowest secore.

lowest_score = min(scores_list)

#Delete the lowest score from the list.

scores_list.remove(lowest_score)

#Calculate the average score>

average_score = sum(scores_list) / len(scores_list)

#Now lets determine the letter grade.

letter_grade = None
if average_score >= 90:
    letter_grade = "A"

elif average_score >= 80:
    letter_grade = "B"

elif average_score >= 70:
    letter_grade = "C"

elif average_score >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"

#last but no least is to display the results.

print("----------------------------Results-------------------------------------")

print(f"Lowest score is: {lowest_score}")

print(f"Modified List: {scores_list}")

print(f"Scores Average: {average_score:.2f}")

print(f"Grade : {letter_grade}")

print("---------------------------------------------------------")
