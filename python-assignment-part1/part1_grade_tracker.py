raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    name = student['name'].strip().title()
    roll = int(student['roll'])
    marks = [int(mark.strip()) for mark in student['marks_str'].split(',')]

    is_valid_name = all(word.isalpha() for word in name.split())
    validity = '✓ Valid name' if is_valid_name else '✗ Invalid name'

    cleaned = {
        'name': name,
        'roll': roll,
        'marks': marks,
    }
    cleaned_students.append(cleaned)

    print('================================')
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print(validity)
    print('================================')

student_103 = next((s for s in cleaned_students if s['roll'] == 103), None)
if student_103:
    print(f"\nStudent 103 in ALL CAPS : {student_103['name'].upper()}")
    print(f"Student 103 in lowercase : {student_103['name'].lower()}")

# Task 2 — Marks Analysis Using Loops & Conditionals#########

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"\nMarks analysis for {student_name}:")

for subject, mark in zip(subjects, marks):
    if 90 <= mark <= 100:
        grade = "A+"
    elif 80 <= mark <= 89:
        grade = "A"
    elif 70 <= mark <= 79:
        grade = "B"
    elif 60 <= mark <= 69:
        grade = "C"
    else:
        grade = "F"
    print(f"{subject} : {mark} ({grade})")

total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)
max_index = marks.index(max(marks))
min_index = marks.index(min(marks))

print(f"\nTotal marks   : {total_marks}")
print(f"Average marks : {average_marks}")
print(f"Highest scoring subject : {subjects[max_index]} ({marks[max_index]})")
print(f"Lowest scoring subject  : {subjects[min_index]} ({marks[min_index]})")

new_subjects_count = 0
print("\nEnter new subjects and marks. Type 'done' to finish.")
while True:
    subject_name = input("Subject name: ").strip()
    if subject_name.lower() == "done":
        break
    marks_input = input("Marks (0-100): ").strip()
    try:
        new_mark = int(marks_input)
        if new_mark < 0 or new_mark > 100:
            print("Invalid marks: please enter a number between 0 and 100.")
            continue
    except ValueError:
        print("Invalid marks: please enter a numeric value.")
        continue

    subjects.append(subject_name)
    marks.append(new_mark)
    new_subjects_count += 1
    print(f"Added {subject_name} with marks {new_mark}.\n")

if new_subjects_count > 0:
    updated_average = round(sum(marks) / len(marks), 2)
else:
    updated_average = average_marks

print(f"\nNew subjects added: {new_subjects_count}")
print(f"Updated average across all subjects: {updated_average}")

# Task 3 — Class Performance Summary
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

results = []
for name, scores in class_data:
    average = round(sum(scores) / len(scores), 2)
    status = "Pass" if average >= 60 else "Fail"
    results.append((name, average, status))
    print(f"{name:<17} | {average:6.2f} | {status}")

passed_count = sum(1 for _, _, status in results if status == "Pass")
failed_count = sum(1 for _, _, status in results if status == "Fail")

topper = max(results, key=lambda item: item[1])
class_average = round(sum(avg for _, avg, _ in results) / len(results), 2)

print(f"\nNumber of students passed: {passed_count}")
print(f"Number of students failed: {failed_count}")
print(f"Class topper: {topper[0]} ({topper[1]:.2f})")
print(f"Class average: {class_average:.2f}")

# Task 4 — String Manipulation Utility
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
clean_essay = essay.strip()
print(f"\nStep 1 - Clean essay: {clean_essay}")

title_case = clean_essay.title()
print(f"Step 2 - Title Case: {title_case}")

python_count = clean_essay.count("python")
print(f"Step 3 - 'python' count: {python_count}")

replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"Step 4 - Replaced essay: {replaced_essay}")

sentences = clean_essay.split(". ")
print(f"Step 5 - Sentences list: {sentences}")

print("Step 6 - Numbered sentences:")
for index, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{index}. {sentence}")
