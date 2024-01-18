class Discipline:
    def __init__(self, name, semester, duration, total_hours, assessment, department):
        self.name = name
        self.semester = semester
        self.duration = duration
        self.total_hours = total_hours
        self.assessment = assessment
        self.department = department


def add_discipline(database):
    ln = len(database)
    database.append(None)
    print('Вы зашли в функцию создания новой дисциплины')
    a = str(input('Пожалуйста, введите название новой дисциплины: '))
    database[ln] = Discipline(
        a,
        str(input(f'Отлично; а теперь введите информацию о том, с какого семестра читается дисциплина "{a}": ')),
        str(input(f'Теперь введите продолжительность курса в семестрах по дисциплине "{a}": ')),
        str(input(f'Дальше информацию об общем количестве часов по дисциплине "{a}": ')),
        str(input(f'А вид отчётности по дисциплине "{a}" ("зачёт" или "экзамен")?: ')),
        str(input(f'И последнее - какая кафедра читает курс по дисциплине "{a}"?: '))
    )


def remove_discipline(database):
    ln = len(database)
    if ln == 0:
        print('Вы зашли в функцию удаления дисциплины, '
              'но на данный момент в базе данных нет ни одной дисциплины, '
              'поэтому вы будете возвращены в главное меню')
    else:
        sab = str(input('Вы зашли в функцию удаления дисциплины\n'
                        'Введите название дисциплины, которую вы хотите удалить: '))
        chek = 0
        for i in range(ln):
            if sab.lower() == str(database[i].name).lower():
                print(f'Дисциплина "{database[i].name}" успешно удалена из базы данных!')
                database.pop(i)
                chek += 1
                break
        if chek == 0:
            print('Данная дисциплина не была обнаружена в базе данных. Возможно вы ошиблись при вводе её названия')


def edit_discipline(database):
    ln = len(database)
    if ln == 0:
        print('Вы зашли в функцию редактирования дисциплин, '
              'но на данный момент в базе данных нет ни одной дисциплины, '
              'поэтому вы будете возвращены в главное меню')
    else:
        sab = str(input('Вы зашли в функцию редактирования дисциплин\n'
                        'Введите название дисциплины, которую вы хотите изменить: '))
        chek = 0
        for i in range(ln):
            if sab.lower() == str(database[i].name).lower():
                a = 'Тут может быть написано всё что угодно'
                print(f'В базе данный обнаружена дисциплина "{database[i].name}".')
                while a != '0':
                    a = str(input(f'Воспользуйтесь меню ниже для корректировки дисциплинs "{database[i].name}"\n'
                                  f'Введите "0" для возвращения в главное меню\n'
                                  f'Введите "1" для изменения названия дисциплины "{database[i].name}"\n'
                                  f'Введите "2" для изменения семестра, с которого начинается чтение '
                                  f'дисциплины "{database[i].name}"\n'
                                  f'Введите "3" для изменения информации о продолжительности курса (в семестрах) '
                                  f'по дисциплине "{database[i].name}"\n'
                                  f'Введите "4" для изменения информации об общем количестве часов '
                                  f'по дисциплине "{database[i].name}"\n'
                                  f'Введите "5" для изменения информации об виде отчётности (зачёт, экзамен) '
                                  f'по дисциплине "{database[i].name}"\n'
                                  f'Введите "6" для изменения информации об кафедре, которая читает '
                                  f'дисциплину "{database[i].name}"\n\n'
                                  f'Итак, ваш выбор: '))
                    if a == '1':
                        database[i].name = str(input(f'Введите новое название название для '
                                                     f'дисциплины "{database[i].name}": '))
                        print('Готово!\n')
                    elif a == '2':
                        database[i].semester = str(input(f'Введите новую информацию о том, к какого семестра читается'
                                                         f' дисциплина "{database[i].name}": '))
                        print('Готово!\n')
                    elif a == '3':
                        database[i].duration = str(input(f'Введите новую информацию о продолжительности курса '
                                                     f'(в семестрах) по дисциплине "{database[i].name}": '))
                        print('Готово!\n')
                    elif a == '4':
                        database[i].total_hours = str(input(f'Введите новую информацию об общем количестве часов '
                                                     f'по дисциплине "{database[i].name}": '))
                        print('Готово!\n')
                    elif a == '5':
                        database[i].assessment = str(input(f'Введите новую информацию о виде отчётности (зачёт, экзамен) '
                                                     f'по дисциплине "{database[i].name}": '))
                        print('Готово!\n')
                    elif a == '6':
                        database[i].department = str(input(f'Введите новую информацию о кафедре, которая читает '
                                                     f'дисциплину "{database[i].name}"'))
                        print('Готово!\n')
                    else:
                        print('Кажется вы ввели не цифру от 0 до 6. Попробуйте снова, у вас обязательно получится!\n')

                return

        if chek == 0:
            print('Данная дисциплина не была обнаружена в базе данных. Возможно вы ошиблись при вводе её названия')


A = []
for i in range(3):
    A[i] = Discipline(0, 0, 0, 0, 0, 0)
while True:
    a = int(input('1 или 2? '))

    if a == 1:
        add_discipline(A)
    elif a == 2:
        remove_discipline(A)

    i = int(input('Время для i: '))
    print(
        A[i].name,
        A[i].semester,
        A[i].duration,
        A[i].total_hours,
        A[i].assessment,
        A[i].department
    )

#
#
#
# def display_database(database):
#     """
#     Функция для вывода на экран всей базы дисциплин
#     """
#     pass
#
# def sort_by_semester_department_hours(database):
#     """
#     Функция для создания полного списка всех дисциплин с сортировкой по семестру, кафедре и общему количеству часов
#     """
#     pass
#
# def sort_by_assessment_duration_hours(database, assessment_type):
#     """
#     Функция для создания списка дисциплин с заданным видом отчётности и сортировкой по продолжительности курса и общему количеству часов
#     """
#     pass
#
# def sort_by_department_hours_range(database, min_hours, max_hours):
#     """
#     Функция для создания списка дисциплин с общим количеством часов в заданном диапазоне с сортировкой по кафедре и общему количеству часов
#     """
#     pass
#
# def binary_insertion_sort(data, key):
#     """
#     Функция для сортировки данных методом бинарной вставки по указанному ключу
#     """
#     pass
#
# def user_interface():
#     """
#     Функция для создания дружественного интерфейса пользователя
#     """
#     pass
#
# # Пример использования функций
# database = []  # инициализация базы данных
#
# # добавление новых дисциплин
# discipline1 = Discipline("Название1", 3, 2, 120, "экзамен", "Кафедра1")
# add_discipline(database, discipline1)
#
# discipline2 = Discipline("Название2", 2, 4, 90, "зачёт", "Кафедра2")
# add_discipline(database, discipline2)
#
# # вывод базы дисциплин
# display_database(database)
#
# # создание списка дисциплин с сортировкой по семестру, кафедре и общему количеству часов
# sorted_disciplines = sort_by_semester_department_hours(database)
#
# # отображение списка
# for discipline in sorted_disciplines:
#     print(discipline.name, discipline.semester, discipline.department, discipline.total_hours)
