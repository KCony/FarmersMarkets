import csv
import math
import grid_class


class Database:
    # filename = 'Export.csv'

    def __init__(self):
        self.sheet = {}  # Атрибут для хранения содержимого страницы (метод show_sheet)
        self.sheet_size = 10  # Атрибут для задания величины страницы
        self.data = {}  # Атрибут содержит в себе преобразованные данные из csv

    def show_filtered(self, list_reader, tuple_filter):
        """
        Метод фильтрует данные таблицы по одному заданному одному параметру
        :param list_reader: передается либо объект DictReader, либо список - результат предыдущей фильтрации
        :param tuple_filter: key - наименование столбца, value - значение, по которому фильтруем
        :return: list отфильтрованных магазинов(dict)
        """
        key, value = tuple_filter

        def filter_function(dict_filter):
            """
            Метод задает функцию для фильтрации магазинов
            :param dict_filter: данные магазина в виде dict
            :return: Bool
            """
            return dict_filter.get(key) == value

        result_generator = filter(filter_function, list_reader)
        return list(result_generator)

    def show_filtered_markets_city_state(self, list_reader, city, state):
        """
        Метод фильтрует данные таблицы по заданному city и state
        :param list_reader: принимает объет DictReader, когда у класса будет атрибут DictReader этот параметр надо будет
                            убрать!
        :param city: задает значение столбца city
        :param state: задает значение столбца state
        :return: list отфильтрованных данных
        """
        filtered_markets_state = self.show_filtered(list_reader, ('State', state))
        filtered_markets_city_state = self.show_filtered(filtered_markets_state, ('city', city))
        return list(filtered_markets_city_state)

    def show_filtered_markets_city_state_xy(self, list_reader, city, state, distance, zip_code=''):
        """
        Метод фильтрует данные таблицы по заданному city и state, если нет zip_code, если zip_code есть - ищет
        координаты, по ним находит магазины со значением distance <= заданному в функции
        :param list_reader: пока принимает объет DictReader
        :param city: задает значение столбца city
        :param state: задает значение столбца state
        :param distance: задает расстояние до выбранного пользователем магазина
        :param zip_code: почтовый индекс от которого ищутся близжайшие магазины
        :return: list отфильтрованных данных
        """
        if zip_code == '':
            filtered_city_state = self.show_filtered_markets_city_state(list_reader, city, state)
            return filtered_city_state
        else:
            filtered_zip = self.show_filtered(list_reader, ('zip', zip_code))
            print((filtered_zip[0].get('x'), filtered_zip[0].get('y')))
            coord = (float(filtered_zip[0].get('x')), float(filtered_zip[0].get('y')))
            srch = grid_class.grid_search(list_reader)
            srch.map_builder()
            res = srch.search(coord)

            def filter_function_dist(pair):
                key, value = pair
                coordinates, dist = value
                if dist <= distance:
                    return True

            def filter_function_markets(dictionary):
                filter_func_dist = list(filter(filter_function_dist, res.items()))

                id_list = []
                for i in filter_func_dist:
                    ident, coord_dist = i
                    id_list.append(ident)

                if dictionary.get('FMID') in id_list:
                    return True

            result_generator = filter(filter_function_markets, list_reader)

            return list(result_generator)


    def show_sheet(self, sheet_number):
        """
        Метод разбивает массив данных на страницы и возвращает
        данные с указанной пользователем страницы. Размер страницы
        по умолчанию составляет 10 строк.
        :param sheet_number: задаёт значение страницы для вывода
        :return: list данных, если страница существует, и False, если её нет
        Для изменения размера страницы используйте атрибут sheet_size
        """
        self.num_of_sheets = math.ceil(len(self.data) / self.sheet_size)  # Вычисляем общее количество страниц
        if sheet_number != 0 and sheet_number < self.num_of_sheets:  # Если введённая страница входит в диапазон
            self.start_index = (sheet_number - 1) * self.sheet_size  # Вычисляем стартовый индекс страницы
            self.end_index = min(sheet_number * self.sheet_size, len(self.data))  # Вычисляем конечный индекс страницы
            self.sheet = self.data[
                         self.start_index:self.end_index]  # Выполняем срез списка, чтобы получить содержимое страницы
            return self.sheet  # Возвращаем срез
        else:
            return False

    def open_database(self, filename):
        """
        Метод открывает базу данных, хранящуюся в .csv файле
        :param filename: принимает имя файла для открытия
        :return: True, если файл открыт успешно, или False, если открыть файл не удалось
        """
        try:
            with open(filename, 'r', encoding='UTF-8') as self.file:  # Открытие файла
                self.reader = csv.DictReader(self.file)  # Читаем данные в виде списка
                self.data = list(self.reader)  # Преобразуем данные в список
                return True  # Возвращаем True
        except FileNotFoundError:  # Если ошибка
            return False  # Возвращаем False

    def return_frame(self):
        """
        Возвращаем все данные
        """
        return self.data

    def return_headers(self):
        """
        Возвращаем заголовки
        """
        return self.data[0].keys()

    def market_show_info(self, market_position: int):  # Функция вывода полной информации о рынке.
        '''Метод возвращает подробную информацию о рынке, находящююся
           в базе данных в виде словаря. Обратиться к записи можно через её
           порядковый номер.
           Пример использования:
           market = market_show_info(5) - обращение к рынку под пятым номером.'''
        # Предполагается, что у названий рынков, независимо от способа их вывода в консоль (всё разом, или постранично)
        # будет нумерация от 1 и до конца списка.
        if market_position == 0 or market_position > int(
                len(self.data)):  # Если введённое число равно 0 или больше размера базы
            return False  # Выводим ошибку
        else:  # Иначе
            market_position -= 1  # Вычисляем реальный размер позиции (начало нумерации позиций в базе начинается с 0)
            return self.data[market_position]


if __name__ == '__main__':
    sheet_number = 1  # Номер просматриваемой страницы
    row_count = 1  # Счётчик строк
    database = Database()
    if database.open_database('Export.csv'):
        print("База данных открыта успешно.")
        # print("Выполняем поиск по городу и штату:")
        # for i in database.show_filtered_markets_city_state(database.data, 'Highlands', 'New Jersey'):
        #    print(i.get('MarketName'))
        print("Содержимое страницы " + str(sheet_number))
        sheet = database.show_sheet(sheet_number)
        for i in sheet:  # Цикл, где мы считываем исключительно названия рынков
            print(str(row_count) + '. ' + i['MarketName'])  # Выводим названия рынков с нумерацией
            row_count += 1
        pointer = int(input("Введите номер строки: "))  # Предлагаем пользователю получить более подробную информацию
        market = database.market_show_info(pointer)  # Считываем словарь
        print(market)  # Выводим его в консоль
        print(database.show_filtered_markets_city_state_xy(database.data, 'Danville', 'Vermont', 0.5, '05828'))
    else:
        print("Базу данных открыть не удалось.")



