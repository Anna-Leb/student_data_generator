import random
import datetime
import json
import sys

def generate_student_data():

    first_names = ["Анна", "Мария", "Екатерина", "Ольга", "Ирина"]
    last_names = ["Иванова", "Петрова", "Сидорова", "Лебедева", "Кузнецова"]
    subjects = ["Математика", "Физика", "Прикладное программирование", "Базы данных", "Компьютерные сети"]

    student = {
        "id": random.randint(1000, 9999),
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "age": random.randint(18, 25),
        "grade": round(random.uniform(3.0, 5.0), 2),
        "subject": random.choice(subjects),
        "timestamp": datetime.datetime.now().isoformat()
    }

    return student

def main():
    print("=" * 50)
    print("ГЕНЕРАТОР ДАННЫХ СТУДЕНТОВ")
    print("=" * 50)

    students = []
    for i in range(3):
        student = generate_student_data()
        students.append(student)
        print(f"Студент {i+1}:")
        print(f"  ID: {student['id']}")
        print(f"  Имя: {student['name']}")
        print(f"  Возраст: {student['age']}")
        print(f"  Средний балл: {student['grade']}")
        print(f"  Предмет: {student['subject']}")
        print("-" * 30)

    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    print(f"Данные сохранены в файл: students.json")
    print(f"Время генерации: {datetime.datetime.now().strftime('%H:%M:%S')}")

    return 0

if __name__ == "__main__":
    sys.exit(main())