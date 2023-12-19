#using for loop 

# Input a Python list of student heights
student_heights = input("Enter heights separated by space: ").split()

# Convert the heights to integers
student_heights = [int(height) for height in student_heights]

# Calculate total height, number of students, and average height
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students) if number_of_students > 0 else 0

# Output results
print(f"Total height = {total_height}")
print(f"Number of students = {number_of_students}")
print(f"Average height = {average_height}")
