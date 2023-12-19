# Input a list of student scores
student_scores = input("Enter scores separated by space: ").split()

# Convert the scores to integers
student_scores = [int(score) for score in student_scores]

# Initialize highest_score to the first score in the list
highest_score = 0

# Find the highest score
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Output the highest score
print(f"The highest score in the class is: {highest_score}")
