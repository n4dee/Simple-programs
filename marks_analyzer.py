# Student Marks Analyzer

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)
    
total = sum(marks)
average = total / len(marks)
print("\n--- Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
