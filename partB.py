print("Enter student name: ");
name = input()

print("Enter score 1: ");
score1 = float(input())

print("Enter score 2: ");
score2 = float(input())

print("Enter score 3: ");
score3 = float(input())

total = score1 + score2 + score3;
average = total / 3;

print(name + " - Total: " + f"{total:.2f}" + ", Average: " + f"{average:.2f}");