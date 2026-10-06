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
            number_students = int(input("Enter number of students: "))

            if number_students > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    averages = []
    records = []

    for i in range(number_students):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")

        scores = []

        for j in range(3):
            while True:
                try:
                    score = float(input("Enter score " + str(j + 1) + ": "))

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
        record = (name, average, grade)
        records.append(record)

    highest, lowest, class_mean = get_stats(averages)
    sorted_avgs = sorted(averages, reverse=True)
    top3 = sorted_avgs[:3]

    print("\n===== CLASS REPORT =====")
    print(f"{'Name':<15}{'Average':<12}{'Grade':<8}")

    for name, avg, grade in records:
        print(f"{name:<15}{avg:<12.2f}{grade:<8}")

    print("------------------------------")

    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    print(f"Class mean: {class_mean:.2f}")

    print("\nNumber of students:", len(averages))
    print("Sum of averages:", f"{sum(averages):.2f}")
    print("Maximum average:", f"{max(averages):.2f}")
    print("Minimum average:", f"{min(averages):.2f}")

    print("\nTop 3 Students:")

    sorted_records = sorted(
        records,
        key=lambda student: student[1],
        reverse=True
    )

    for name, avg, grade in sorted_records[:3]:
        print(f"{name} - {avg:.2f} - {grade}")

if __name__ == "__main__":
    main()