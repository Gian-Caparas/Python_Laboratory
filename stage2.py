name = input("Enter student name: ");
score1 = float(input("Enter score 1: "));
score2 = float(input("Enter score 2: "));
score3 = float(input("Enter score 3: "));

total = score1 + score2 + score3;
average = total / 3;

print(name + " - Total: " + f"{total:.2f}" + ", Average: " + f"{average:.2f}");

if average >= 80:
    print("A")
elif average >= 70:
    print("B")
elif average >= 60:
    print("C")
elif average >= 50:
    print("D")
elif average < 0 & average > 100:
    print("Invalid Input")
else:
    print("F")