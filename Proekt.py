class Discipline:
    def __init__(self, name, semester, duration, total_hours, assessment, department):
        self.name = name
        self.semester = semester
        self.duration = duration
        self.total_hours = total_hours
        self.assessment = assessment
        self.department = department


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
    department = str(input(f'И последнее - какая кафедра читает курс по дисциплине "{name}"?\nВаш ввод: '))
    database.append(Discipline(name, semester, duration, hours, assessment, department))
    print(f'Новая дисциплина "{name}" успешно добавлена в базу данных!\n'
          f'Возвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')


def remove_discipline(database):
    ln = len(database)
    if ln == 0:
        print('\nВы зашли в функцию удаления дисциплины, но на данный момент в базе данных нет ни одной дисциплины\n'
              'Возвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')
        return
    name = str(input('\nВы зашли в функцию удаления дисциплины\n'
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
        print('\nВы зашли в функцию редактирования дисциплин, но на данный момент в базе данных нет ни одной дисциплины'
              '\nВозвращаемся в главное меню\n\n————————————————————————————————————————————————————————————————\n')
        return
    name = str(input('\nВы зашли в функцию редактирования дисциплин\n'
                     'Введите название дисциплины, которую вы хотите изменить\n'
                     'Либо введите всё что угодно, что не является дисциплиной, чтобы вернуться в главное меню'
                     '\nВаш ввод: '))
    chek = 0
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
        print('В данный момент в базе данных нет ни одной дисциплины\nПеревожу вас в главное меню')
        return
    print('Вы зашли в функцию показа всех дисциплин имеющихся в базе данных\n'
          f'На данный момент у нас их {ln}\nВот все из них:')
    while 2 + 2 == 4:                                        # Простите, мне очень стыдно
        for i in range(ln):
            print(f'{i+1}. {database[i].name}')
        a = str(input('Чтобы узнать больше о какой либо дисциплине - введите её номер или название\n'
                      'Чтобы выйти из функции - введите "0" или "Выход"\nИтак, ваш выбор: '))
        if (a == '0') or (a.lower() == 'выход'):
            return
        chek = 0
        for i in range(ln):
            if (a == str(database[i].name)) or (a == str(i+1)):
                print(f'Подробная информания о дисциплине "{database[i].name}":\n'
                      f'Название дисциплины - {database[i].name}\n'
                      f'Читается с - {database[i].semester} семестра\n'
                      f'Продолжительность курса - {database[i].duration} семестр(а/ов)\n'
                      f'Общее количество часов - {database[i].total_hours}\n'
                      f'Вид отчётности - {database[i].assessment}\n'
                      f'Читающая курс кафедра - {database[i].department}\n'
                )
                chek += 1
        if chek == 0:
            print('Такая дисциплина не найдена, возможно вы ошиблись в её названии')
        input('Введите всё что угодно, чтобы вернуться к списку всех дисциплин: ')
        print()


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid
        for j in range(i, left, -1):
            arr[j] = arr[j-1]
        arr[left] = key
    return arr


def sort_by_semester_department_hours(database):
    def sab(database, i, sort):
        if sort == 1:
            return database[i].semester
        elif sort == 2:
            return database[i].department
        return database[i].total_hours

    a = input('Вы зашли в функцию сортировки дисциплин в базе данных\n'
              'Введите "1" для сортировки базы данных по семестру с которого читается дисциплина (по возрастанию)\n'
              'Введите "2" для сортировки базы данных по читающей дисциплюну кафедре (по алфавиту)\n'
              'Введите "3" для сортировки базы данных по общему количеству часов чтения дисциплины (по убыванию)\n'
              'Любой другой ввод выведет вас в главное меню\n'
              'Итак, ваш выбор: ')

    sort = 3
    if a == '1':
        sort = 1
    elif a == '2':
        sort = 2
    elif a != '3':
        return database

    arr = []
    output = []
    ln = len(database)
    for i in range(ln):
        try:
            arr.append(sab(database, i, sort))
        except:
            print('Неправильный формат данных')
    arr = binary_insertion_sort(arr)
    for i in range(len(arr)):
        for j in range(ln):
            if arr[i] == sab(database, j, sort):
                output.append(database[j])
    print('Готово!')
    if a != '3':
        return output
    output.reverse()
    return output


def sort_by_assessment_duration_hours(database):
    def sab(arr):
        a = input('А теперь введите номер сортировки, которая устраивает вас больше:\n'
                  '1. Продолжительность курса в семестрах (по возрастанию)\n'
                  '2. Общее количество часов (по убыванию)\n'
                  'Ваш ввод: ')
        if a == '1':
            arr = binary_insertion_sort(arr)
            print('\nОтлично, вот дисциплины которые вы искали:')
            for i in range(len(arr)):
                print(f'{i}. {arr[i]}')
            return
        elif a == '2':
            arr = binary_insertion_sort(arr)
            arr.reverse()
            print('\nОтлично, вот дисциплины которые вы искали:')
            for i in range(len(arr)):
                print(f'{i}. {arr[i]}')
            return
        else:
            print('Кажется вы ввели не 1 и не 2. возвращаю вас на главный экран')
            return

    a = input('Вы зашли в функцию сортировки дисциплин в базе данных с заданным видом отчётности\n'
              'Введите "1" или "Зачёт", чтобы выбрать группу дисциплин с видом отчётности "Зачёт"\n'
              'Введите "2" или "Экзамен", чтобы выбрать группу дисциплин с видом отчётности "Экзамен"\n'
              'Или введите что-нибудь другое чтобы вернуться в главное меню\n'
              'Ваш ввод: ')
    if (a == "1") or (a.lower() == "зачёт"):
        arr = []
        for i in range(len(database)):
            if str(database[i].assessment).lower() == 'зачёт':
                arr.append(database[i].name)
        sab(arr)
        return
    elif (a == "2") or (a.lower() == "экзамен"):
        arr = []
        for i in range(len(database)):
            if str(database[i].assessment).lower() == 'экзамен':
                arr.append(database[i].name)
        sab(arr)
        return
    else:
        return


def sort_by_department_hours_range(database):
    N = input('Вы зашли в функцию для поиска дисциплин с общим количеством часов в заданном промежутке\n'
              'Чтобы найти дисциплины, в которых общее количество часов чтения находится в заданном диапазоне, '
              'введите два числа через пробел: Минимальное и Максимальное количество часов чтения для '
              'соответствующей дисциплины\nЧтобы выйти в главное меню - введите что угодно другое\n'
              'Ваш ввод: ')
    try:
        N1, N2 = int(map(N.split(" ", 1)))
        arr1 = []
        arr2 = []
        for i in range(len(database)):
            if N1 <= int(database[i].total_hours) <= N2:
                arr1.append(database[i].department)
                arr2.append(database[i].total_hours)
        N = input('\nОтлично, а теперь выберите номер сортировки, которая вас больше устраивает\n'
                  '1. Читающая кафедра (по алфавиту)\n'
                  '2. Общее количество часов (по убыванию)\n'
                  'Ваш ввод: ')
        if N == '1':
            print('Строка 264')
        elif N == '2':
            print('Строка 266')
        else:
            print('Вы ввели не 1 и не 2, перенаправляю вас в главное меню')
            return

    except:
        print('\nВыход в главное меню')
        return


A = []
A.append(Discipline('Химия', 4, 3, 200, "Экзамен", "ХимFuck"))
A.append(Discipline('Матеша', 2, 4, 300, "Экзамен", "Мехмат"))
A.append(Discipline("ЯП", 3, 3, 250, "Зачёт", "ИКНТ"))
A.append(Discipline("Физикааааааа", 5, 1, 80, "Экзамен", "ФизFuck"))
A.append(Discipline("Английский", 1, 1, 100, "Зачёт", "Языки"))
A.append(Discipline("Дискретка", 1, 5, 400, "Зачёт", "Мехмат"))
A.append(Discipline("Алгаритмы", 2, 4, 250, "Экзамен", "ИКНТ"))
A.append(Discipline("Разработка", 5, 4, 400, "Экзамен", "ИКНТ"))
A.append(Discipline("Физкультура", 1, 2, 50, "Зачёт", "ФК"))
A.append(Discipline("Экономика", 5, 2, 100, "Зачёт", "Экономический"))
while True:
    try:
        a = int(input('Какая функция?\n'
                      '1. Добавить\n'
                      '2. Удалить\n'
                      '3. Редактировать\n'
                      '4. Показать массив\n'
                      '5. Сортировка\n'
                      '6. Сортировка по отчётности\n'
                      'Ваш ввод: '))

        if a == 1:
            add_discipline(A)
        elif a == 2:
            remove_discipline(A)
        elif a == 3:
            edit_discipline(A)
        elif a == 4:
            display_database(A)
        elif a == 5:
            A = sort_by_semester_department_hours(A)
        elif a == 6:
            sort_by_assessment_duration_hours(A)
    except Exception as ex:
        print(ex)
