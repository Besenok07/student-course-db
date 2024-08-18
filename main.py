from database import add_student, add_course, enroll_student, list_students, list_courses, list_students_in_course

def main():
    while True:
        print("\n1. Додати нового студента")
        print("2. Додати новий курс")
        print("3. Показати список студентів")
        print("4. Показати список курсів")
        print("5. Зареєструвати студента на курс")
        print("6. Показати студентів на конкретному курсі")
        print("7. Вийти")

        choice = input("Оберіть опцію (1-7): ")

        if choice == "1":
            name = input("Введіть ім'я студента: ")
            age = int(input("Введіть вік студента: "))
            major = input("Введіть спеціальність студента: ")
            add_student(name, age, major)
            print("Студента додано!")

        elif choice == "2":
            course_name = input("Введіть назву курсу: ")
            instructor = input("Введіть ім'я викладача: ")
            add_course(course_name, instructor)
            print("Курс додано!")

        elif choice == "3":
            students = list_students()
            for student in students:
                print(student)

        elif choice == "4":
            courses = list_courses()
            for course in courses:
                print(course)

        elif choice == "5":
            student_id = int(input("Введіть ID студента: "))
            course_id = int(input("Введіть ID курсу: "))
            enroll_student(student_id, course_id)
            print("Студента зареєстровано на курс!")

        elif choice == "6":
            course_id = int(input("Введіть ID курсу: "))
            students = list_students_in_course(course_id)
            for student in students:
                print(student)

        elif choice == "7":
            break

        else:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")

if __name__ == "__main__":
    main()
