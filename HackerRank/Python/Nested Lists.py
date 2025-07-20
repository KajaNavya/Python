if __name__ == '__main__':
    students_data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_data.append([name, score])

    # Find unique sorted scores
    scores = sorted(list(set([student[1] for student in students_data])))
    second_lowest_score = scores[1]

    # Find names of students with the second lowest score
    second_lowest_students_names = []
    for student in students_data:
        if student[1] == second_lowest_score:
            second_lowest_students_names.append(student[0])

    # Print names alphabetically
    for name in sorted(second_lowest_students_names):
        print(name)
