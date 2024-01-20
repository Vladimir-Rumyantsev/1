class Discipline:
    def __init__(self, name, semester, duration, total_hours, assessment, department):
        self.name = name
        self.semester = semester
        self.duration = duration
        self.total_hours = total_hours
        self.assessment = assessment
        self.department = department


def binary_search(arr, item, start, end, key):
    if start == end:
        if key(arr[start]) > key(item):
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if key(arr[mid]) < key(item):
        return binary_search(arr, item, mid + 1, end, key)
    elif key(arr[mid]) > key(item):
        return binary_search(arr, item, start, mid - 1, key)
    else:
        return mid


def binary_insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        item = arr[i]

        j = binary_search(arr, item, 0, i - 1, key)

        arr = arr[:j] + [item] + arr[j:i] + arr[i + 1:]
    return arr


def binary_insertion_sort_2(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        item = arr[i]
        index = i - 1
        while index >= 0 and key(item) < key(arr[index]):
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = item
    return arr


def add_discipline(database):
    name = str(input('\n————————————————————————————————————————————————————————————————\n\n'
                     'Вы зашли в функцию создания новой дисциплины\n'
                     'Введите "Выход или "0", чтобы выйти\n'
                     'Либо введите название новой дисциплины\nВаш ввод: '))
    if (name == '0') or (name.lower() == 'выход'):
        print(f'Возвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')
        return
    try:
        semester = int(input(f'\nОтлично, создаём новую дисциплину "{name}"\n'
                             f'С какого семестра читается эта дисциплина? Введите натуральное число\nВаш ввод: '))
    except:
        print(f'Вы ввели не натуральное число, поэтому дисциплина "{name}" не добавлена!\nВозвращаемся в главное меню'
              f'\n\n————————————————————————————————————————————————————————————————\n')
        return
    try:
        duration = int(input(f'\nТеперь введите продолжительность курса в семестрах по дисциплине "{name}" '
                             f'(натуральное число)\nВаш ввод: '))
    except:
        print(f'Вы ввели не натуральное число, поэтому дисциплина "{name}" не добавлена!\nВозвращаемся в главное меню'
              f'\n\n————————————————————————————————————————————————————————————————\n')
        return
    try:
        hours = int(input(f'\nДальше введите информацию об общем количестве часов по дисциплине "{name}" '
                          f'(натуральное число)\nВаш ввод: '))
    except:
        print(f'Вы ввели не натуральное число, поэтому дисциплина "{name}" не добавлена!\nВозвращаемся в главное меню'
              f'\n\n————————————————————————————————————————————————————————————————\n')
        return
    assessment = str(input(f'\nВыбор вида отчётности по дисциплине "{name}" ("Зачёт" или "Экзамен")\n'
                           f'Введите "1" или "Зачёт", чтобы выбрать вид отчётности "Зачёт"\n'
                           f'Введите "2" или "Экзамен", чтобы выбрать вид отчётности "Экзамен"\nВаш ввод: '))
    if (assessment == '1') or (assessment.lower() == 'зачёт'):
        assessment = 'Зачёт'
    elif (assessment == '2') or (assessment.lower() == 'экзамен'):
        assessment = 'Экзамен'
    else:
        print(f'Вы ввели некорректную информацию, поэтому дисциплина "{name}" не добавлена!\nВозвращаемся в главное '
              f'меню\n\n————————————————————————————————————————————————————————————————\n')
        return
    department = str(input(f'\nИ последнее - какая кафедра читает курс по дисциплине "{name}"?\nВаш ввод: '))
    database.append(Discipline(name, semester, duration, hours, assessment, department))
    print(f'\nНовая дисциплина "{name}" успешно добавлена в базу данных!\n'
          f'Возвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')


def remove_discipline(database):
    ln = len(database)
    if ln == 0:
        print('\n————————————————————————————————————————————————————————————————\n\n'
              'Вы зашли в функцию удаления дисциплины, но на данный момент в базе данных нет ни одной дисциплины\n'
              'Возвращаемся в главное меню\n'
              '\n————————————————————————————————————————————————————————————————\n')
        return
    name = str(input('\n————————————————————————————————————————————————————————————————\n\n'
                     'Вы зашли в функцию удаления дисциплины\n'
                     'Введите название дисциплины, которую вы хотите удалить\nВаш ввод: '))
    chek = 0
    for i in range(ln):
        if name.lower() == str(database[i].name).lower():
            print(f'Дисциплина "{database[i].name}" успешно удалена из базы данных!')
            database.pop(i)
            chek += 1
            break
    if chek == 0:
        print('Данная дисциплина не была обнаружена в базе данных. Возможно вы ошиблись при вводе её названия')
    print('\nВозвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')


def edit_discipline(database):
    ln = len(database)
    if ln == 0:
        print('\n————————————————————————————————————————————————————————————————\n\n'
              'Вы зашли в функцию редактирования дисциплин, но на данный момент в базе данных нет ни одной дисциплины'
              '\nВозвращаемся в главное меню\n'
              '\n————————————————————————————————————————————————————————————————\n')
        return
    name = str(input('\n————————————————————————————————————————————————————————————————\n\n'
                     'Вы зашли в функцию редактирования дисциплин\n'
                     'Введите название дисциплины, которую вы хотите изменить\n'
                     'Либо введите всё что угодно, что не является дисциплиной, чтобы вернуться в главное меню'
                     '\nВаш ввод: '))
    for i in range(ln):
        if name.lower() == str(database[i].name).lower():
            print(f'\nВ базе данных обнаружена дисциплина "{database[i].name}"')
            while True:
                a = str(input(f'Воспользуйтесь меню ниже для корректировки дисциплины "{database[i].name}"\n'
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
                              f'дисциплину "{database[i].name}"\n'
                              f'Введите всё что угодно кроме чисел от 1 до 6, чтобы вернуться на главный экран\n'
                              f'Ваш ввод: '))
                if a == '1':
                    database[i].name = str(input(f'\nВведите новое название название для '
                                                 f'дисциплины "{database[i].name}": '))
                    print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                elif a == '2':
                    try:
                        semester = int(input(f'\nВведите новую информацию о том, к какого семестра читается '
                                             f'дисциплина "{database[i].name}" (Натуральное число):\nВаш ввод: '))
                        database[i].semester = semester
                        print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                    except:
                        print(f'Вы ввели не натуральное число, поэтому данные о дисциплине '
                              f'"{database[i].name}" не изменены!\n'
                              f'Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                elif a == '3':
                    try:
                        duration = int(input(f'\nВведите новую информацию о количестве семестров по дисциплине '
                                             f'"{database[i].name}" (Натуральное число):\nВаш ввод: '))
                        database[i].duration = duration
                        print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                    except:
                        print(f'Вы ввели не натуральное число, поэтому данные о дисциплине '
                              f'"{database[i].name}" не изменены!\n'
                              f'Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                elif a == '4':
                    try:
                        hours = int(input(f'\nВведите новую информацию об общем количестве часов по дисциплине '
                                          f'"{database[i].name}" (Натуральное число):\nВаш ввод: '))
                        database[i].total_hours = hours
                        print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                    except:
                        print(f'Вы ввели не натуральное число, поэтому данные о дисциплине '
                              f'"{database[i].name}" не изменены!\n'
                              f'Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                elif a == '5':
                    assessment = str(input(f'\nВведите новую информацию о виде отчётности по дисциплине '
                                           f'"{database[i].name}" ("Зачёт" или "Экзамен")\n'
                                           f'Введите "1" или "Зачёт", чтобы выбрать вид отчётности "Зачёт"\n'
                                           f'Введите "2" или "Экзамен", чтобы выбрать вид отчётности "Экзамен"\n'
                                           f'Ваш ввод: '))
                    if (assessment == '1') or (assessment.lower() == 'зачёт'):
                        database[i].assessment = 'Зачёт'
                        print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                    elif (assessment == '2') or (assessment.lower() == 'экзамен'):
                        database[i].assessment = 'Экзамен'
                        print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                    else:
                        print(f'Вы ввели некорректную информацию, поэтому данные о дисциплине '
                              f'"{database[i].name}" не изменены!\n'
                              f'Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                elif a == '6':
                    database[i].department = str(input(f'Введите новую информацию о кафедре, которая читает '
                                                       f'дисциплину "{database[i].name}"\nВаш ввод: '))
                    print(f'Готово! Возвращаемся в меню корректировки дисциплины "{database[i].name}"\n')
                else:
                    print(f'\nВозвращаемся в главное меню'
                          f'\n\n————————————————————————————————————————————————————————————————\n')
                    return

    print(f'Данная дисциплина не была обнаружена в базе данных\nВозвращаемся в главное меню'
          f'\n\n————————————————————————————————————————————————————————————————\n')


def display_database(database):
    ln = len(database)
    if ln == 0:
        print('\n————————————————————————————————————————————————————————————————\n\n'
              'Вы зашли в функцию показа всех дисциплин имеющихся в базе данных, '
              'но в данный момент в базе данных нет ни одной дисциплины\nПеревожу вас в главное меню\n'
              '\n————————————————————————————————————————————————————————————————\n')
        return
    print('\n————————————————————————————————————————————————————————————————\n\n'
          'Вы зашли в функцию показа всех дисциплин имеющихся в базе данных\n'
          f'На данный момент у нас их {ln}\nВот все из них:\n')
    while True:
        for i in range(ln):
            print(f'{i + 1}. {database[i].name}')
        a = str(input('\nЧтобы узнать больше о какой либо дисциплине - введите её номер или название'
                      '\nЧтобы выйти из функции - введите "0" или "Выход"\nВаш ввод: '))
        if (a == '0') or (a.lower() == 'выход'):
            print(f'\nВозвращаемся в главное меню\n'
                  f'\n————————————————————————————————————————————————————————————————\n')
            return
        chek = 0
        for i in range(ln):
            if (a.lower() == (str(database[i].name)).lower()) or (a == str(i + 1)):
                print(f'\nПодробная информания о дисциплине "{database[i].name}":\n'
                      f'Название дисциплины - {database[i].name}\n'
                      f'Читается с - {database[i].semester} семестра\n'
                      f'Продолжительность курса - {database[i].duration} семестр(а/ов)\n'
                      f'Общее количество часов - {database[i].total_hours}\n'
                      f'Вид отчётности - {database[i].assessment}\n'
                      f'Читающая курс кафедра - {database[i].department}\n')
                chek += 1
        if chek == 0:
            print(f'\nТакая дисциплина не найдена, возможно вы ошиблись в её названии')
        input('Введите всё что угодно, чтобы вернуться к списку всех дисциплин\nВаш ввод: ')
        print()


def sort_by_semester_department_hours(database):
    try:
        sort = int(input('\n————————————————————————————————————————————————————————————————\n\n'
                         'Вы зашли в функцию сортировки дисциплин в базе данных\n'
                         'Введите "1" для сортировки базы данных по семестру с которого читается дисциплина '
                         '(по возрастанию)\n'
                         'Введите "2" для сортировки базы данных по читающей дисциплину кафедре (по алфавиту)\n'
                         'Введите "3" для сортировки базы данных по общему количеству часов чтения дисциплины '
                         '(по убыванию)\nЛюбой другой ввод выведет вас в главное меню\nВаш ввод: '))
        if not (1 <= sort <= 3):
            print(f'\nВозвращаемся в главное меню\n'
                  f'\n————————————————————————————————————————————————————————————————\n')
            return database
    except:
        print(f'\nВозвращаемся в главное меню\n'
              f'\n————————————————————————————————————————————————————————————————\n')
        return database

    if sort == 1:
        print(f'\nВот тут эта жесть\n\n'
              f'{sorted(database, key=lambda x: (x.semester, x.department, -x.total_hours))}\n\n')
        try:
            sorted_database = binary_insertion_sort(key=lambda x: (x.semester, x.department, -x.total_hours))
            print('\nКажется получилось!!!\n')
        except:
            sorted_database = sorted(database, key=lambda x: (x.semester, x.department, -x.total_hours))
    elif sort == 2:
        sorted_database = sorted(database, key=lambda x: (x.department, x.semester, -x.total_hours))
    elif sort == 3:
        sorted_database = sorted(database, key=lambda x: (-x.total_hours, x.semester, x.department))

    return sorted_database


def sort_by_assessment_duration_hours(database):
    try:
        assessment_type = input('\nВыберите вид отчётности ("Зачёт" или "Экзамен"): ').capitalize()

        sorted_database = [discipline for discipline in database if discipline.assessment == assessment_type]
        sorted_database = sorted(sorted_database, key=lambda x: (x.duration, -x.total_hours))

        return sorted_database
    except:
        print(f'\nВозвращаемся в главное меню\n'
              f'\n————————————————————————————————————————————————————————————————\n')
        return database


def sort_by_department_hours_range(database):
    try:
        N1, N2 = map(int, input('\n————————————————————————————————————————————————————————————————\n\n'
                                'Вы зашли в функцию для поиска дисциплин с общим количеством часов в заданном '
                                'промежутке\nЧтобы найти дисциплины, в которых общее количество часов чтения находится '
                                'в заданном диапазоне, введите два числа через пробел: Минимальное и Максимальное '
                                'количество часов чтения для соответствующей дисциплины\n'
                                'Чтобы выйти в главное меню - введите что угодно другое\n'
                                'Ваш ввод: ').split(" ", 1))
        result = [discipline for discipline in database if N1 <= discipline.total]
        return result
    except:
        print(f'\nВозвращаемся в главное меню\n'
              f'\n————————————————————————————————————————————————————————————————\n')
        return database


A = [
    Discipline('Химия', 4, 3, 200, "Экзамен", "Химический факультет"),
    Discipline('Введение в математику', 2, 4, 300, "Экзамен", "Механико-математический факультет"),
    Discipline("Языки программирования", 3, 3, 250, "Зачёт", "ИКНТ"),
    Discipline("Физика", 5, 1, 80, "Экзамен", "Физический факультет"),
    Discipline("Английский язык", 1, 1, 100, "Зачёт", "Кафедра иностранных языков"),
    Discipline("Дискретная математика", 1, 5, 400, "Зачёт", "Механико-математический факультет"),
    Discipline("Алгоритмы и структуры данных", 2, 4, 250, "Экзамен", "ИКНТ"),
    Discipline("Разработка", 5, 4, 400, "Экзамен", "ИКНТ"),
    Discipline("Физкультура", 1, 2, 50, "Зачёт", "Кафедра физической культуры"),
    Discipline("Экономика", 5, 2, 100, "Зачёт", "Экономический факультет")
]
print('\nДобро пожаловать в программу для работы с базой данных по дисциплинам!\n'
      'Надеюсь опыт пользования программой вам понравится!\n'
      'Переходим в главное меню программы...\n'
      '\n————————————————————————————————————————————————————————————————\n')
while True:
    try:
        a = str(input('Главное меню\n\n'
                      'Выберите функцию для работы с базой данных (для этого введите число от 1 до 7)\n'
                      '1. Добавить дисциплину\n'
                      '2. Удалить дисциплину\n'
                      '3. Редактировать дисциплину\n'
                      '4. Показать список всех дисциплин\n'
                      '5. Сортировка дисциплин\n'
                      '6. Сортировка по отчётности\n'
                      '7. Список дисциплин с общим количеством часов в заданном диапазоне\n'
                      'Ваш ввод: '))
        if a == '1':
            add_discipline(A)
        elif a == '2':
            remove_discipline(A)
        elif a == '3':
            edit_discipline(A)
        elif a == '4':
            display_database(A)
        elif a == '5':
            A = sort_by_semester_department_hours(A)
        elif a == '6':
            A = sort_by_assessment_duration_hours(A)
        elif a == '7':
            A = sort_by_department_hours_range(A)
        else:
            print('\nВы ввели не число от 1 до 7. Попробуйте ещё раз, у вас обязательно получится!\n'
                  '\n————————————————————————————————————————————————————————————————\n')
    except Exception as ex:
        print(f'\nК сожалению, во время работы программы произошла ошибка...\n{ex}\n'
              f'\n————————————————————————————————————————————————————————————————\n')


#
#
# def sort_by_semester_department_hours(database):
#     def sab(database, i, sort):
#         if sort == 1:
#             return database[i].semester
#         elif sort == 2:
#             return database[i].department
#         return database[i].total_hours
#
#     a = input('Вы зашли в функцию сортировки дисциплин в базе данных\n'
#               'Введите "1" для сортировки базы данных по семестру с которого читается дисциплина (по возрастанию)\n'
#               'Введите "2" для сортировки базы данных по читающей дисциплюну кафедре (по алфавиту)\n'
#               'Введите "3" для сортировки базы данных по общему количеству часов чтения дисциплины (по убыванию)\n'
#               'Любой другой ввод выведет вас в главное меню\n'
#               'Итак, ваш выбор: ')
#
#     sort = 3
#     if a == '1':
#         sort = 1
#     elif a == '2':
#         sort = 2
#     elif a != '3':
#         return database
#
#     arr = []
#     output = []
#     ln = len(database)
#     for i in range(ln):
#         try:
#             arr.append(sab(database, i, sort))
#         except:
#             print('Неправильный формат данных')
#     arr = binary_insertion_sort(arr)
#     for i in range(len(arr)):
#         for j in range(ln):
#             if arr[i] == sab(database, j, sort):
#                 output.append(database[j])
#     print('Готово!')
#     if a != '3':
#         return output
#     output.reverse()
#     return output
#
#
# def sort_by_assessment_duration_hours(database):
#     def sab(arr):
#         a = input('А теперь введите номер сортировки, которая устраивает вас больше:\n'
#                   '1. Продолжительность курса в семестрах (по возрастанию)\n'
#                   '2. Общее количество часов (по убыванию)\n'
#                   'Ваш ввод: ')
#         if a == '1':
#             arr = binary_insertion_sort(arr)
#             print('\nОтлично, вот дисциплины которые вы искали:')
#             for i in range(len(arr)):
#                 print(f'{i}. {arr[i]}')
#             return
#         elif a == '2':
#             arr = binary_insertion_sort(arr)
#             arr.reverse()
#             print('\nОтлично, вот дисциплины которые вы искали:')
#             for i in range(len(arr)):
#                 print(f'{i}. {arr[i]}')
#             return
#         else:
#             print('Кажется вы ввели не 1 и не 2. возвращаю вас на главный экран')
#             return
#
#     a = input('Вы зашли в функцию сортировки дисциплин в базе данных с заданным видом отчётности\n'
#               'Введите "1" или "Зачёт", чтобы выбрать группу дисциплин с видом отчётности "Зачёт"\n'
#               'Введите "2" или "Экзамен", чтобы выбрать группу дисциплин с видом отчётности "Экзамен"\n'
#               'Или введите что-нибудь другое чтобы вернуться в главное меню\n'
#               'Ваш ввод: ')
#     if (a == "1") or (a.lower() == "зачёт"):
#         arr = []
#         for i in range(len(database)):
#             if str(database[i].assessment).lower() == 'зачёт':
#                 arr.append(database[i].name)
#         sab(arr)
#         return
#     elif (a == "2") or (a.lower() == "экзамен"):
#         arr = []
#         for i in range(len(database)):
#             if str(database[i].assessment).lower() == 'экзамен':
#                 arr.append(database[i].name)
#         sab(arr)
#         return
#     else:
#         return
#
#
# def sort_by_department_hours_range(database):
#     N = input('Вы зашли в функцию для поиска дисциплин с общим количеством часов в заданном промежутке\n'
#               'Чтобы найти дисциплины, в которых общее количество часов чтения находится в заданном диапазоне, '
#               'введите два числа через пробел: Минимальное и Максимальное количество часов чтения для '
#               'соответствующей дисциплины\nЧтобы выйти в главное меню - введите что угодно другое\n'
#               'Ваш ввод: ')
#     try:
#         N1, N2 = int(map(N.split(" ", 1)))
#         arr1 = []
#         arr2 = []
#         for i in range(len(database)):
#             if N1 <= int(database[i].total_hours) <= N2:
#                 arr1.append(database[i].department)
#                 arr2.append(database[i].total_hours)
#         N = input('\nОтлично, а теперь выберите номер сортировки, которая вас больше устраивает\n'
#                   '1. Читающая кафедра (по алфавиту)\n'
#                   '2. Общее количество часов (по убыванию)\n'
#                   'Ваш ввод: ')
#         if N == '1':
#             print('Строка 264')
#         elif N == '2':
#             print('Строка 266')
#         else:
#             print('Вы ввели не 1 и не 2, перенаправляю вас в главное меню')
#             return
#
#     except:
#         print('\nВыход в главное меню')
#         return
