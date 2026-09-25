name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
dsa = float(input("Enter DSA marks: "))
java = float(input("Enter Java marks: "))
english = float(input("Enter English marks: "))

total = maths + python + dsa + java + english
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")