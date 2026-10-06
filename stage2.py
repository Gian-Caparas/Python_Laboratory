number_students = int(input("How many students are there? "))

for i in range(number_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    while True:
        try:
            score1 = float(input("Enter score 1 (0-100): "))

            if 0 <= score1 <= 100:
                break
            else:
                print("Invalid. Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            score2 = float(input("Enter score 2 (0-100): "))

            if 0 <= score2 <= 100:
                break
            else:
                print("Invalid. Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            score3 = float(input("Enter score 3 (0-100): "))

            if 0 <= score3 <= 100:
                break
            else:
                print("Invalid. Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    total = score1 + score2 + score3
    average = total / 3

    # Task 2.1 - Grade classifier
    if average < 0 or average > 100:
        grade = "Invalid average"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print(
        name
        + " - Total: "
        + f"{total:.2f}"
        + ", Average: "
        + f"{average:.2f}"
        + ", Grade: "
        + grade
    )


# Task 2.4 - Mini challenge

print("\nMultiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 13):
    product = number * i
    if product % 5 == 0:
        continue
    if product > 100:
        break

    print(f"{number} x {i} = {product}")