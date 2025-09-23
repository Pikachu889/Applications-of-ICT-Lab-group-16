marks = int(input("Enter your marks: "))
if marks >= 90:
    grade="A"
elif marks >=70 and marks <=90:
    grade="B"
elif marks >=50 and marks <=70:
    grade="C"
elif marks <=50:
    grade="F"
else:
    print("Invalid input!")
print("Your grade is:", grade)