name = input("Enter student name: ");
score1 = float(input("Enter score 1: "));
score2 = float(input("Enter score 2: "));
score3 = float(input("Enter score 3: "));

total = score1 + score2 + score3;
average = total / 3;

print(name + " - Total: " + f"{total:.2f}" + ", Average: " + f"{average:.2f}");