#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Блок Console_Controller отвечает за взаимодействие с пользователем
из командной строки — пункт 6 Задания№6
Основной цикл команд в виде функции REPL (Read/Evaluate/Print/Loop
на ввод от пользователя и отправка в блок отображения View:
"""

import model
import console_ui

"""
    Будет реализовываться следующая функциональность:
    list    - Просматривать список всех фермерских рынков в стране (включая рецензии и рейтинги) 
            (с разбивкой по страницам - потом);   
    find    - Осуществлять поиск фермерского рынка по городу и штату, а также по почтовому индексу 
            с возможностью ограничить зону поиска определенной дальностью 
            (например, на удалении не более 30 миль);
            - Распределять рынки по различным критериям (рейтингу, городу и штату, удаленности от 
            определенной точки и т.п.) от минимального к максимальному значению или наоборот;
    details - Переходить от результатов поиска к просмотру подробных данных о любом рынке, 
            присутствующем в поисковой выдаче;
    show 
    & write - Просматривать и оставлять рецензии на любой фермерский рынок, состоящие из 
            необязательного текста рецензии и обязательного рейтинга (от 1 до 5 звезд);
    write   - Создавать рецензии, привязанные к имени и фамилии пользователя;
    delete  - Удалять требуемые записи и выходить из программы.
    
    Предлагаемый список команд от пользователя:
    list              - выводит все рынки в стране
    list city ASC     - выводит города в алфавитном порядке по возрастанию
    find              - поиск рынков по критериям. Критерии(аргументы) вводятся после команды find
    find              - Troy New York
    find              - 12180 -> FMID - посмотреть details
    details            - подробная информация об одном рынке
    show review FMID  - показать отзывы о рынке по номеру/индексу
    write review FMID - написать отзыв
    end   - заканчивает цикл взаимодействия с пользователем 
            и передает всю полученную инф-цию в модуль View
"""

cmd_list = ('list', 'find', 'details', 'show', 'write', 'delete', 'end')
cmd_list = sorted(cmd_list)
# Список доступных команд, оформленный кортежем
def get_find_command_arg(arg_case):
    # Определяем значение 1-го аргумента к команде find.
    if arg_case == 0:
        return 'Default'
    if arg_case == 1:
        return 'State'
    if arg_case == 2:
        return 'City'
    if arg_case == 3:
        return 'ZIP'
    if arg_case == 4:
        return 'Rating'
    if arg_case == 5:
        return 'Distance'
    else: return 'error'

# функция валидации команды, передающейся через аргумент line2cmd - от пользователя
# list, find, т.к. они могут передаваться с дополнительными аргументами, поэтому здесь
# делаем доп. запрос пользователю
# Поэтому сначала проверяем — это команды с доп.аргументами или без.
# Результатом функции будем возвращать список с 3-мя аргументами p_command_list.
# Список для передачи в качестве результата обработки.

def process_command(line2cmd):
    #  Локальный список, который формируется внутри и передается как результат функции
    line_cmd = line2cmd
    p_command_list = []
    p_command_list.append(line_cmd)
    cmd_arg = None  # Переменная для организации цикла получения аргументов от пользователя

    if line_cmd == 'find':
        # По условию задания поиск может осуществляться нескольким критериям:
        # 1 - по штату, 2 - городу, 3 - индексу, 4 - рейтингу и
        # 5 - радиусу от местонахождения пользователя.
        # Отображаем командную строку для ввода аргумента поиска от 1 до 5.
        #   cmd_arg = None
        while cmd_arg is None:
        # Выводим список доступных аргументов для find и ждем выбора пользователя
            prompt = console_ui.get_arguments_prompt(
                    line_cmd + ":\n1 - by State\n2 - by City\n3 - by ZIP\n"
                               "4 - by Rating\n5 - by Distance in Miles")
            cmd_arg = input(prompt)
        # Включаем обработку исключения при неправильном вводе аргумента поиска (один из 5)
        try:
            cmd_arg = int(cmd_arg)
        except:
            cmd_arg = 6  # 6 - не входит в допустимый диапазон, поэтому опрашиваем заново
        if cmd_arg != 6:
            p_command_list.append(get_find_command_arg(cmd_arg))
        else: cmd_arg = None

        # Аргумент команды find получили, теперь надо получить его значение
        # Добавили обработку исключений для аргументов команды find:
        # для State/City - тип строка, для ZIP/Rating/Distance - число
        # Запускаем цикл опроса и проверки 3-го аргумента функции find
        # - уже в переменной p_command_list[2]
        cmd_arg = None
        p_command_list.append('')  # Забиваем место в списке под значение
        while cmd_arg is None:
            prompt = console_ui.get_arguments_prompt(line_cmd + '-> ' + p_command_list[1])
            p_command_list[2] = input(prompt)  # Получаем значение выбранного аргумента
            if (p_command_list[1] == 'State') or (p_command_list[1] == 'City'):
                cmd_arg = 1
            else:  #  Для аргументов 3 - 5
                # Если аргументы - не строковые - запускаем проверку на числа
                try:
                    cmd_arg = int(p_command_list[2])
                except:
                    cmd_arg = None  # Если не число - цикл ввода повторяется

    if line_cmd == 'list':
        # Для проверки добавляем аргумент в команду list.
        # Добавляем блок запроса/обработки аргументов.
        while cmd_arg is None:
            # Выводим список доступных аргументов для list и ждем выбора пользователя
            prompt = console_ui.get_arguments_prompt(
                          line_cmd + ":\n0 - by Default\n1 - by State\n2 - by City\n"
                                     "3 - by ZIP\n4 - by Rating\n5 - by Distance in Miles")
            cmd_arg = input(prompt)
            # Включаем обработку исключения при неправильном вводе аргумента для списка
            try:
                cmd_arg = int(cmd_arg)
            except:
                cmd_arg = 6  # 6 - не входит в допустимый диапазон, поэтому опрашиваем заново
            if cmd_arg != 6:
                p_command_list.append(get_find_command_arg(cmd_arg))
            else:
                cmd_arg = None

    # Аргумент команды list получили, теперь надо получить его значение
    # Добавили обработку исключений для аргументов команды list:
    # Определяем порядок вывода списка - Ascending/Descending (по возрастанию/по убыванию)
    # Запускаем цикл опроса и проверки 3-го аргумента функции list - уже в переменной p_command_list[2]
        cmd_arg = None
        # если команда list без параметров - оставляем одну команду в списке
        if p_command_list[1] == 'Default':
            p_command_list.remove('Default')
        # p_command_list.append('')  # Забиваем место в списке под значение
        while (cmd_arg is None) and (len(p_command_list) > 1):
            prompt = console_ui.get_arguments_prompt(
            line_cmd + '-> ' + p_command_list[1] + " :\n1 - Ascending\n2 - Descending")
            cmd_arg = input(prompt)
            # Включаем обработку исключения при неправильном вводе второго аргумента для списка
            try:
                cmd_arg = int(cmd_arg)
            # 3 - не входит в допустимый диапазон из 2-х параметров, поэтому опрашиваем заново
            except:
                cmd_arg = None
            if cmd_arg == 1:
                p_command_list.append('ASC')
            if cmd_arg == 2:
                p_command_list.append('DES')
            if (cmd_arg < 1) or (cmd_arg > 2):
                cmd_arg = None

    if line_cmd == 'details':
        pass  # Пока заглушки
    if line_cmd == 'show':
        pass  # Пока заглушки — показать
    if line_cmd == 'write':
        pass  # Пока заглушки
    # Возвращаем список с командой и 2-мя аргументами
    return p_command_list

def execute_command(c_line, db_conn, db_curs):
    # функция выполнения команды - c_line
    # db_conn - подключение к БД (Создаем соединение с нашей базой данных)
    # db_curs - Создаем курсор — это специальный объект который делает запросы и получает их результаты
    # c_line - список из 3-х аргументов -> 1.Команда, 2. Аргумент, 3. Критерий для аргумента.
    # Примеры c_line - list city ASC, show review FMID, write review FMID
    # Список из 3-х аргументов, передаваемых в командах list', 'find', 'show', 'write'

    if c_line[0] == 'list':
        # Лезем в БД за списком всех рынков в одном объекте - result
        result = model.list_markets(db_curs, c_line)
        # Здесь обращаемся к модулю console_ui (команда VIEW) для отображения
        console_ui.print_ui(c_line, result)
    if c_line[0] == 'find':
        result = model.find_market(db_curs, c_line)  # Ищем в БД рынок с критериями из c_line
        # Здесь обращаемся к модулю console_ui (команда VIEW) для отображения
        console_ui.print_ui(c_line, result)

def repl(db_conn, db_curs):
    command = ''
    while command != 'end':
      prompt = console_ui.get_command_prompt()  # Отображаем командную строку
      command = input(prompt)   # Получаем команду - command
        # Обработка команды — нужно описать каждую команду списком/словарем
      if command in cmd_list:
        # Здесь надо добавить обработку ошибок/исключений TRY...
         p_command = process_command(command)
         execute_command(p_command, db_conn, db_curs)
      else:
         command = 'error'
         console_ui.print_ui(command, cmd_list)   # Печатаем команду и список доступных команд


if __name__ == '__main__':
    db_conn, db_curs = model.init()
    repl(db_conn, db_curs)  # Запускаем цикл обращения к БД, пока пользователь не ввел команду 'end'
    model.close(db_conn, db_curs)  # Закрываем БД
