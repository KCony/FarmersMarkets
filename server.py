import csv


class Database:
    filename = 'Export.csv'

    def show_filtered_markets(self, list_reader, tuple_filter):
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
        Метод фильтраует данные таблицы по заданному city и state
        :param list_reader: принимает объет DictReader, когда у класса будет атрибут DictReader этот параметр надо будет
                            убрать!
        :param city: задает значение столбца city
        :param state: задает значение столбца state
        :return: list отфильтрованных данных
        """
        filtered_markets_state = self.show_filtered_markets(list_reader, ('State', state))
        filtered_markets_city_state = self.show_filtered_markets(filtered_markets_state, ('city', city))
        return list(filtered_markets_city_state)


if __name__ == '__main__':
    with open(Database.filename, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        database = Database()
        for i in database.show_filtered_markets_city_state(reader, 'Highlands', 'New Jersey'):
            print(i.get('MarketName'))
