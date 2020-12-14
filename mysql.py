import pymysql

db = pymysql.connect('localhost','root','panteley2_68','exams')

cursor = db.cursor()
while True:
        print('Выберите действие: Просмотреть-1, Добавить-2, Редактировать-3, Удалить-4, Выход-5')
        a = input(":")
        if a == '1':
                print("Выберите, что хотите посмотреть: 1 - таблица наименования предметов, 2 - список студентов")
                b = input("::")
                if b == '1':
                        cursor.execute("SELECT * FROM exams.subjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                elif b == '2':
                        cursor.execute("SELECT students.Id, students.SURNAME, students.NAME, subjects.SUBJECT FROM students INNER JOIN subjects ON students.SUBJECT1  = subjects.idsubjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
        elif a == '2':
                print('Выберите, куда хотите добавить данные: 1 - таблица наименования предметов, 2 - список студентов')
                c = input("::")
                if c == '2':
                        surname = input("Введите фамилию: ")
                        name = input("Введите имя: ")
                        cursor.execute("SELECT * FROM exams.subjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                        subject = int(input("Введите номер предмета: "))
                        cursor.execute("INSERT INTO exams.students (SURNAME, NAME, SUBJECT1) VALUE (%s, %s, %s);", (surname, name, subject))
                        cursor.execute("SELECT * FROM exams.students;")
                        db.commit()
                        print("Данные успешно добавлены")
                elif c == '1':
                        subj = input("Введите название предмета: ")
                        cursor.execute("INSERT INTO exams.subjects (SUBJECT) VALUE (%s);", (subj))
                        cursor.execute("SELECT * FROM exams.subjects;")
                        db.commit()
                        print("Данные успешно добавлены")
        elif a == '3':
                print('Выберите, где хотите редактировать данные: 1 - таблица наименования предметов, 2 - список студентов')
                d = input("::")
                if d == '1':
                        id = int(input("Введите номер предмета, который хотите изменить: "))
                        subj = input("Введите предмет: ")
                        sql = "UPDATE exams.subjects SET SUBJECT = '%s' WHERE (idsubjects = '%s');"% (subj, id)
                        cursor.execute(sql)
                        cursor.execute("SELECT * FROM exams.subjects;")
                        db.commit()
                        print("Изменеия сохранены")
                elif d == '2':
                        id = print("Введите номер студента, которого хотите заменить")
                        cursor.execute("SELECT students.Id, students.SURNAME, students.NAME, subjects.SUBJECT FROM students INNER JOIN subjects ON students.SUBJECT1  = subjects.idsubjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                        surname = input("Введите фамилию: ")
                        name = input("Введите имя: ")
                        cursor.execute("SELECT * FROM exams.subjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                        ids = int(input("Введите номер предмета: "))
                        sql = "UPDATE exams.students SET SURNAME = '%s', NAME = '%s, SUBJECT1 = '%s'  WHERE (Id = '%s');"% (surname,name,ids,id)
                        cursor.execute(sql)
                        cursor.execute("SELECT * FROM exams.subjects;")
                        db.commit()
                        print("Изменеия сохранены")
        elif a == '4':
                print("Выберите таблицу, в которой хотите удалить данные: 1 - таблица наименования предметов, 2 - список студентов")
                e = input("::")
                if e == '1':
                        cursor.execute("SELECT * FROM exams.subjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                        id = input("Введдите номер предмета, который хотите удалить: ")
                        sql = "DELETE FROM exams.subjects WHERE (idsubjects = '%s');"%(id)
                        cursor.execute(sql)
                        cursor.execute("SELECT * FROM exams.subjects;")
                        db.commit()
                        print("Удаление произвндено успешно")
                elif e == '2':
                        cursor.execute("SELECT students.Id, students.SURNAME, students.NAME, subjects.SUBJECT FROM students INNER JOIN subjects ON students.SUBJECT1  = subjects.idsubjects;")
                        rows = cursor.fetchall()
                        print(*rows, sep="\n")
                        id = input("Введите номер студента, которого хотите удалить:")
                        sql = "DELETE FROM exams.students WHERE (Id = '%s');"%(id)
                        cursor.execute(sql)
                        cursor.execute("SELECT * FROM exams.students;")
                        db.commit()
                        print("Удаление произвндено успешно")
        elif a =='5':
                break
db.close()
