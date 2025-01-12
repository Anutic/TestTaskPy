def show_all(students_dict):
    for student in sorted(students_dict.keys(), reverse=True):
        subjects = ', '.join(students_dict[student])
        print(f"{student}: {subjects}")

def student_for_sub(students_dict, student_name):
    return students_dict.get(student_name, f"Ученик '{student_name}' не найден.")

def sub_for_students(students_dict, subject):
    students = [student for student, subjects in students_dict.items() if subject in subjects]
    return students

def get_students_data():
    try:
        n = int(input("Введите количество учеников в классе: "))
        if n <= 0:
            print("Количество учеников должно быть положительным числом. Повторите ввод.")
            return None
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        return None

    print(f"Вы должны ввести данные для {n} учеников.")
    students_dict = {}
    current_count = 0

    while current_count < n:
        name = input(f"Введите имя {current_count + 1}-го ученика: ").strip()
        if not name:
            print("Имя не может быть пустым. Повторите ввод.")
            return None  

        subjects_input = input(f"Введите предметы {current_count + 1}-го ученика через пробел: ").strip()
        subjects = subjects_input.split()
        if not subjects:
            print("Вы не ввели ни одного предмета. Повторите ввод.")
            return None 

        students_dict[name] = subjects
        current_count += 1
        print(f"Ученик {name} добавлен. Осталось ввести: {n - current_count} учеников.")

    return students_dict

def main():
    while True:
        students_dict = get_students_data()
        if students_dict is not None:
            break  

    while True:
        print("\nВыберите действие:")
        print("1. Показать всех учеников и их предметы (show_all)")
        print("2. Узнать предметы ученика (student_for_sub)")
        print("3. Узнать учеников по предмету (sub_for_students)")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            show_all(students_dict)
        elif choice == '2':
            student_name = input("Введите имя ученика: ")
            result = student_for_sub(students_dict, student_name)
            if isinstance(result, list):
                print(f"Предметы ученика {student_name}: {', '.join(result)}")
            else:
                print(result)
        elif choice == '3':
            subject = input("Введите название предмета: ")
            students = sub_for_students(students_dict, subject)
            if students:
                print(f"Ученики, изучающие {subject}: {', '.join(students)}")
            else:
                print(f"Ни один ученик не изучает предмет '{subject}'.")
        elif choice == '4':
            print("Завершение программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
