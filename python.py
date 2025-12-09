

FILE_NAME = "students.txt"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write(student + "\n")

def add_student(students):
    name = input("Öğrencinin adı: ")
    number = input("Öğrencinin numarası: ")
    students.append(f"{number} - {name}")
    print("→ Öğrenci eklendi.")

def delete_student(students):
    number = input("Silmek istediğiniz öğrenci numarası: ")
    for student in students:
        if student.startswith(number):
            students.remove(student)
            print("→ Öğrenci silindi.")
            return
    print("→ Böyle bir öğrenci bulunamadı.")

def list_students(students):
    if not students:
        print("Henüz öğrenci yok.")
        return
    print("\n--- Öğrenciler ---")
    for student in students:
        print(student)

def main():
    students = load_students()
    while True:
        print("\n1) Öğrenci Ekle")
        print("2) Öğrenci Sil")
        print("3) Öğrenci Listele")
        print("4) Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            delete_student(students)
            save_students(students)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            print("Programdan çıkılıyor…")
            break
        else:
            print("Hatalı seçim.")

if __name__ == "__main__":
    main()