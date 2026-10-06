def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def get_stats(avg_list):
    highest = max(avg_list)
    lowest = min(avg_list)
    mean = sum(avg_list) / len(avg_list)

    return highest, lowest, mean


def main():
    while True:
        try:
            student_count = int(input("How many students are there? "))

            if student_count > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    records = []
    averages = []

    for i in range(student_count):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")

        scores = []

        for j in range(3):
            while True:
                try:
                    score = float(
                        input(f"Enter score {j + 1} (0-100): ")
                    )

                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")

                except ValueError:
                    print("Invalid input. Enter a number.")

        average = calculate_average(scores)
        grade = get_grade(average)

        averages.append(average)

        records.append((name, average, grade))

    highest, lowest, class_mean = get_stats(averages)

    sorted_records = sorted(
        records,
        key=lambda student: student[1],
        reverse=True
    )

    top3 = sorted_records[:3]

    print("\n===== CLASS REPORT =====")
    print(f"{'Name':<15}{'Average':<12}{'Grade':<8}")

    for name, average, grade in records:
        print(f"{name:<15}{average:<12.2f}{grade:<8}")

    print("-------------------------------")

    print(
        f"Highest: {highest:.2f}   "
        f"Lowest: {lowest:.2f}   "
        f"Class mean: {class_mean:.2f}"
    )

    print("Top 3:", end=" ")

    for i in range(len(top3)):
        print(top3[i][0], end="")

        if i < len(top3) - 1:
            print(", ", end="")

    print()


if __name__ == "__main__":
    main()