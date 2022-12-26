"""Модуль взаимодействия с пользователем."""


import console_ui
import model

conn, curs = model.init('server.db')
cmd_list = {'list', 'find', 'details', 'show', 'write', 'end'}  # Список доступных команд, оформленный кортежем
cmd_line = []   # Список из 3-х аргументов, передаваемых в командах list', 'find', 'show', 'write'

"""
Будет реализовываться следующая функциональность:
list - Просматривать список всех фермерских рынков в стране (включая рецензии и рейтинги) (с разбивкой по страницам - потом);
find - Осуществлять поиск фермерского рынка по городу и штату, а также по почтовому индексу с возможностью ограничить
  зону поиска определенной дальностью (например, на удалении не более 30 миль);
- Переходить от результатов поиска к просмотру подробных данных о любом рынке, присутствующем в поисковой выдаче;
- Просматривать и оставлять рецензии на любой фермерский рынок, состоящие из необязательного текста рецензии
  и обязательного рейтинга (от 1 до 5 звезд);
- Создавать рецензии, привязанные к имени и фамилии пользователя;
- Распределять рынки по различным критериям (рейтингу, городу и штату, удаленности от определенной точки и т.п.)
  от минимального к максимальному значению или наоборот;
- Удалять требуемые записи и выходить из программы.
"""
# Предлагаемый список команд от пользователя:
# list              - выводит все рынки в стране
# list city ASC     - выводит города в алфавитном порядке по возрастанию
# find              - поиск рынков по критериям. Критерии(аргументы) вводятся после команды find
# find              - Troy New York
# find              - 12180 -> FMID - посмотреть details
# details            - подробная информация об одном рынке
# show review FMID  - показать отзывы о рынке по номеру/индексу
# write review FMID - написать отзыв
# end   - заканчивает цикл взаимодействия с пользователем и передает всю полученную инф-цию в модуль View


def process_command(line2cmd):  # функция валидации команды, передающейся через аргумент line2cmd - от пользователя
    #  list, find, т.к. они могут передаваться с дополнительными аргументами, поэтому здесь делаем доп. запрос пользователю
    #  Поэтому сначала проверяем — это команды с доп.аргументами или без.
    #  Результатом функции будем возвращать список с 3-мя аргументами p_command_list.
    #  Список для передачи в качестве результата обработки.
    p_command_list = []
    p_command_list.append(line2cmd)

    if line2cmd == 'list':
        # Для проверки добавляем аргумент в команду find. Надо добавить блок запроса/обработки аргументов.
        p_command_list.append('city')
        p_command_list.append('ASC')

    if line2cmd == 'find':
        # Для проверки добавляем аргумент в команду find. Надо добавить блок запроса/обработки аргументов.
        prompt = console_ui.get_arguments_prompt(line2cmd)  # Отображаем командную строку для ввода аргументов
        cmd = input(prompt)  # Получаем команду - command
        # p_command_list.append('Troy')

    if line2cmd == 'details':
        pass  # Пока заглушки
    if line2cmd == 'show':
        pass  # Пока заглушки — показать
    if line2cmd == 'write':
        pass  # Пока заглушки

    return p_command_list  #


def execute_command(c_line, db_curs):  # функция выполнения команды - c_line
    # db_conn - подключение к БД (Создаем соединение с нашей базой данных)
    # db_curs - Создаем курсор — это специальный объект который делает запросы и получает их результаты
    # c_line - список из 3-х аргументов -> 1.Команда, 2. Аргумент, 3. Критерий для аргумента.
    # Примеры cmd_line - list city ASC, show review FMID, write review FMID

    if c_line[0] == 'list':
        result = model.list_markets(db_curs)  # Лезем в БД за списком всех рынков в одном объекте - result
        console_ui.print_ui(c_line, result)   # Здесь обращаемся к модулю console_ui (команда VIEW) для отображения
    if c_line[0] == 'find':
        result = model.list_markets(db_curs)  # Лезем в БД за списком всех рынков в одном объекте - result
        console_ui.print_ui(c_line, result)  # Здесь обращаемся к модулю console_ui (команда VIEW) для отображения


def repl(db_conn, db_curs):
    command = ''
    while command != 'end':
        prompt = console_ui.get_command_prompt()  # Отображаем командную строку
        command = input(prompt)   # Получаем команду - command
        # Обработка команды — нужно описать каждую команду списком/словарем
        if command in cmd_list:  # Здесь надо добавить обработку ошибок/исключений TRY...
            processed_command = process_command(command)
            execute_command(processed_command, db_conn, db_curs)
        else:
            console_ui.print_ui(command, cmd_list)   # Печатаем команду и список доступных команд


def list_market():
    all_name = model.list_markets(curs)
    for i in all_name:
        print(i)


def list_city():
    all_city = model.all_cities(curs)
    for i in all_city:
        print(i)


def distance():
    la1 = input("enter the latitude 1 ==> ")
    lo1 = input("enter the longitude 1 ==> ")
    la2 = input("enter the latitude 2 ==> ")
    lo2 = input("enter the longitude 2 ==> ")
    dist = model.distance(float(la1), float(lo1), float(la2), float(lo2))
    print("distance between coordinates ==> {:.2f} miles".format(dist))


def name_by_zip(db_curs, zip_code):
    x = model.find_by_zip(db_curs, zip_code)
    j = 0
    for i in x:
        if j == 0:
            print(f'name of Markets ==> {i}')
        if j == 1:
            print(f'comments about market ==> {i}')
        if j == 2:
            print(f'rating of market ==>  {i}')
        j += 1


def name_by_city(db_curs, city, state):
    found_market = model.find_by_city(db_curs, city, state)
    print('found markets: ')
    for i in found_market:
        cnt = 0
        for j in i:
            if cnt == 0:
                print(f'name of Markets ==> {j}')
            if cnt == 1:
                print(f'comments about market ==> {j}')
            if cnt == 2:
                print(f'rating of market ==> {j}')
            cnt += 1


def details(db_curs, name):
    found_market = model.detailed_data(db_curs, name)
    for i in found_market:
        print(i)


# ПРИМЕРЫ КОМАНД НИЖЕ

# list_market()
# list_city()
# details(curs, "HAPI Fresh Farmers' Market")
# name_by_city(curs, 'Akron', 'Ohio')
# name_by_zip(curs, 5828)
# distance()

model.close(conn, curs)


# if __name__ == '__main__':
#     db_conn, db_curs = model.init('server2.db')
#     repl(db_conn, db_curs)  # Запускаем цикл обращения к БД, пока пользователь не ввел команду 'end'
#     model.close(db_conn, db_curs)  # Закрываем БД
