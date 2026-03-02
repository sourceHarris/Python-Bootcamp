# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for score in student_scores:
    if student_scores[score] > 90 and student_scores[score] <= 100:
        student_grades[score] = "Outstanding"
    elif student_scores[score] > 80 and student_scores[score] <= 90:
        student_grades[score] = "Exceeds Expectations"
    elif student_scores[score] > 70 and student_scores[score] <= 80:
        student_grades[score] = "Acceptable"
    elif student_scores[score] <= 70 and student_scores[score] < 70:
        student_grades[score] = "Fail"

for student in student_grades:
    print(f"{student} : {student_grades[student]}")

