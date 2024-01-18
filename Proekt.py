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
                print(f'В базе данных обнаружена дисциплина "{database[i].name}".')
                while a != '0':
                    a = str(input(f'Воспользуйтесь меню ниже для корректировки дисциплины "{database[i].name}"\n'
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
                    elif a != '0':
                        print('Кажется вы ввели не цифру от 0 до 6. Попробуйте снова, у вас обязательно получится!\n')

                return

        if chek == 0:
            print('Данная дисциплина не была обнаружена в базе данных. Возможно вы ошиблись при вводе её названия')


def display_database(database):
    ln = len(database)
    if ln == 0:
        print('В данный момент в базе данных нет ни одной дисциплины\nПеревожу вас в главное меню')
        return
    print('Вы зашли в функцию показа всех дисциплин имеющихся в базе данных\n'
          f'На данный момент у нас их {ln}\nВот все из них:')
    while 2 + 2 == 4:                                        # Простите, мне очень стыдно
        for i in range(ln):
            print(f'{i+1}. {database[i].name}\n')
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
        

A = []
for i in range(3):
    A.append(Discipline(0, 0, 0, 0, 0, 0))
while True:
    try:
        a = int(input('1, 2 или 3? '))

        if a == 1:
            add_discipline(A)
        elif a == 2:
            remove_discipline(A)
        elif a == 3:
            edit_discipline(A)

        i = int(input('Время для i: '))
        print(
            A[i].name,
            A[i].semester,
            A[i].duration,
            A[i].total_hours,
            A[i].assessment,
            A[i].department
        )
    except Exception as ex:
        print(ex)
