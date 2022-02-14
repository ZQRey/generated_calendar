import datetime

# Задаем константы
DAYS = ('Воскресение', 'Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота")
MONTHS = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
          "Декабрь")

print('Генерация календаря. Created ZQRey')

# Узнаем какой год нужен
while True:
    print('Введите год календаря')
    responce = input('> ')

    if responce.isdecimal() and int(responce) > 0:
        year = int(responce)
        break

    print('Пожалуйста введите год цифрами, например 2022...')
    continue

# Запрашиваем необходимый месяц
while True:
    print('Введите нужный месяц цифрой от 1 до 12 включительно')
    responce = input('> ')

    if not responce.isdecimal():
        print('Пожалуйста введите месяц цифрой, например 1 это будет Январь')
        continue

    month = int(responce)
    if 1 <= month <= 12:
        break
    print('Выход за пределы диапазона месяцев (1-12)')

def getCalendarFor(year, month):
    calText = '' # Содержит строковое значение с календарем

    # Размещаем месяц и год сверху календаря:
    calText += (' ' * 34) + MONTHS[month -1] + ' ' + str(year) + '\n'

    # Добавлем метки дней недели
    calText += 'Воскресение|Понедельни|.Вторник..|..Среда...|.Четверг..|.Пятница..|..Суббота.|\n'
    # Горизонтальная линия - разделитель недель:
    weekSeparator = ('+----------' * 7) + '+\n'
    # Пустые строки содержат по десять пробелов между разделителям дней
    blankRow = ('|          ' * 7) + '|\n'
    # Получаем первую дату месяца
    currentDate = datetime.date(year, month, 1)

    # Отнимает от currentDate по дню, пока не дойдем до воскресенья. weekday() возвращает для воскресения 6, а не 0
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    # Переходим в цикле по всем неделям в месяце
    while True:
        calText += weekSeparator
        # dayNumberRow строка с метками номеров дней
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' *8)
            currentDate += datetime.timedelta(days=1) # Переходим ко следующем дню
        dayNumberRow += '|\n' # Добавляем вертикальную линию после субботы
        # Добавляем в текст календаря строку с номерами дней и 3 пустые строки
        calText += dayNumberRow
        for i in range(3): # (!)
            calText += blankRow
        # Проверяем закончили ли мы обработку месяца
        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)
calendarFilename = f' calendar_{year}_{month}.txt'
with open(calendarFilename, 'w') as file:
    file.write(calText)
print('Сохранено под названием ' + calendarFilename)