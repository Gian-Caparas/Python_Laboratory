# Task 1.1
name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

total = score1 + score2 + score3
average = total / 3

print(name + " - Total: " + f"{total:.2f}" + ", Average: " + f"{average:.2f}")


# Task 1.2 - Inspect the types
print(type(name))
print(type(score1))
print(type(score2))
print(type(score3))
print(type(total))
print(type(average))


# Task 1.3 - Predict, then run

print(7 / 2)
print(7 // 2)
print(7 * 2)
print(2 ** 3)
print("ab" * 3)