def calculate_grade(average):
    if average >= 75:
        return 'A'
    elif 60 <= average < 75:
        return 'B'
    elif 40 <= average < 60:
        return 'C'
    else:
        return 'D'

marks = []
for i in range(1, 5):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
grade = calculate_grade(average)

print(f"Average Marks: {average}")
print(f"Grade: {grade}")
