class Discipline:
    def __init__(self, name, semester, duration, total_hours, assessment, department):
        self.name = name
        self.semester = semester
        self.duration = duration
        self.total_hours = total_hours
        self.assessment = assessment
        self.department = department


def binary_insertion_sort(arr, lam=lambda x: x):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if lam(arr[mid]) < lam(key):
                left = mid + 1
            else:
                right = mid
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
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


def sort(database):
    print('\n————————————————————————————————————————————————————————————————\n\nВы зашли в функцию "Учебный план"!')
    while True:
        try:
            srt = int(input('Выберите номер отчёта, который вы хотите создать:\n'
                            'Введите "1" для сортировки дисциплин по: семестру начала чтения (по возрастанию) + '
                            'читающей кафедре (по возрастанию) + общему количеству часов (по убыванию)\n'
                            'Введите "2" для сортировки дисциплин по: заданному виду отчётности + '
                            'продолжительности курса (по возрастанию) + общему количеству часов (по убыванию)\n'
                            'Введите "3" для сортировки дисциплин по: общему количеству часов в определённом диапозоне '
                            '+ читающей кафедре (по возрастанию) + общему количеству часов (по убыванию)\n'
                            'Любой другой ввод выведет вас в главное меню\nВаш ввод: '))
            if not (1 <= srt <= 3):
                print(f'\nВозвращаемся в главное меню\n'
                      f'\n————————————————————————————————————————————————————————————————\n')
                return
        except:
            print(f'\nВозвращаемся в главное меню\n'
                  f'\n————————————————————————————————————————————————————————————————\n')
            return

        if srt == 1:
            arr = binary_insertion_sort(binary_insertion_sort((binary_insertion_sort(database.copy(),
                                        lambda x: -x.total_hours)), lambda x: x.department), lambda x: x.semester)
            print(f'\nДисциплины отсортированные по вашему запросу:')
            for i in range(len(arr)):
                print(f'{i+1}. {arr[i].name}')
            srt = str(input('\nВведите "0" или "Выход", чтобы вернуться в гланое меню'
                            '\nВведите всё что угодно другое, чтобы перейти к меню функции "Учебный план"'
                            '\nВаш ввод: '))
            if srt == '0' or srt.lower() == 'выход':
                print(f'\nВозвращаемся в главное меню\n'
                      f'\n————————————————————————————————————————————————————————————————\n')
                return
            print()

        elif srt == 2:
            srt = input('\nВыберите вид отчётности, по которому нужно выдать выборку дисциплин\n'
                        'Введите "1" или "Зачёт", чтобы выбрать вид отчётности "Зачёт"\n'
                        'Введите "2" или "Экзамен", чтобы выбрать вид отчётности "Экзамен"\n'
                        'Ваш ввод:')
            arr = database.copy()
            if srt == '1' or srt.lower() == 'зачёт':
                for i in range(len(arr)):
                    if str(arr[i].assessment).lower() != 'зачёт':
                        arr.pop(i)
            elif srt == '2' or srt.lower() == 'экзамен':
                for i in range(len(arr)):
                    if str(arr[i].assessment).lower() != 'экзамен':
                        arr.pop(i)

            arr = binary_insertion_sort((binary_insertion_sort(arr, lambda x: -x.total_hours)), lambda x: x.duration)
            print(f'\nДисциплины отсортированные по вашему запросу:')
            for i in range(len(arr)):
                print(f'{i + 1}. {arr[i].name}')
            srt = str(input('\nВведите "0" или "Выход", чтобы вернуться в гланое меню'
                            '\nВведите всё что угодно другое, чтобы перейти к меню функции "Учебный план"'
                            '\nВаш ввод: '))
            if srt == '0' or srt.lower() == 'выход':
                print(f'\nВозвращаемся в главное меню\n'
                      f'\n————————————————————————————————————————————————————————————————\n')
                return
            print()
        elif srt == 3:
            try:
                n1, n2 = map(int, input('\nЧтобы подготовить выборку дисциплин, в которой общее количество часов '
                                        'чтения находится в заданном диапазоне, введите два числа через пробел: '
                                        'Минимальное и Максимальное количество часов чтения для дисциплин\n'
                                        'Чтобы выйти в главное меню - введите что угодно другое\n'
                                        'Ваш ввод: ').split(" ", 1))
            except:
                print(f'\nВозвращаемся в главное меню\n'
                      f'\n————————————————————————————————————————————————————————————————\n')
                return 
            
            arr = database.copy()
            for i in range(len(arr)):
                if not (n1 <= int(arr[i].total_hours) <= n2):
                    arr.pop(i)
            
            arr = binary_insertion_sort((binary_insertion_sort(arr, lambda x: -x.total_hours)), lambda x: x.department)
            print(f'\nДисциплины отсортированные по вашему запросу:')
            for i in range(len(arr)):
                print(f'{i + 1}. {arr[i].name}')
            srt = str(input('\nВведите "0" или "Выход", чтобы вернуться в гланое меню'
                            '\nВведите всё что угодно другое, чтобы перейти к меню функции "Учебный план"'
                            '\nВаш ввод: '))
            if srt == '0' or srt.lower() == 'выход':
                print(f'\nВозвращаемся в главное меню\n'
                      f'\n————————————————————————————————————————————————————————————————\n')
                return
            print()


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
    Discipline("Экономика", 5, 2, 100, "Зачёт", "Экономический факультет"),
    Discipline('1', 4, 3, 400, "Экзамен", "Химический факультет"),
    Discipline('2', 2, 4, 600, "Экзамен", "Механико-математический факультет"),
    Discipline("3", 3, 3, 850, "Зачёт", "ИКНТ"),
    Discipline("4", 5, 1, 830, "Экзамен", "Физический факультет"),
    Discipline("5", 1, 1, 30, "Зачёт", "Кафедра иностранных языков"),
    Discipline("6", 1, 5, 40, "Зачёт", "Механико-математический факультет"),
    Discipline("7", 2, 4, 353245250, "Экзамен", "Другая"),
    Discipline("8", 5, 4, 40034, "Экзамен", "ИКНТ"),
    Discipline("9", 1, 2, 5063, "Зачёт", "Кафедра физической культуры"),
    Discipline("10", 5, 2, 1002, "Зачёт", "Экономический факультет")
]

print('\nДобро пожаловать в программу для работы с базой данных по дисциплинам!\n'
      'Надеюсь опыт пользования программой вам понравится!\n'
      'Переходим в главное меню программы...\n'
      '\n————————————————————————————————————————————————————————————————\n')
while True:
    try:
        a = str(input('Главное меню\n\n'
                      'Выберите функцию для работы с базой данных (для этого введите число от 1 до 5)\n'
                      '1. Добавить дисциплину\n'
                      '2. Удалить дисциплину\n'
                      '3. Редактировать дисциплину\n'
                      '4. Показать список всех дисциплин\n'
                      '5. Учебный план (создать отчёт)\n'
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
            sort(A)
        else:
            print('\nВы ввели не число от 1 до 5. Попробуйте ещё раз, у вас обязательно получится!\n'
                  '\n————————————————————————————————————————————————————————————————\n')
    except Exception as ex:
        print(f'\nК сожалению, во время работы программы произошла ошибка...\n{ex}\n'
              f'\n————————————————————————————————————————————————————————————————\n')
