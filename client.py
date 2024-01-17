import server  # Импорт методов серверной части


class ShowMainMenu():


    def chooser(self, cmd=None):
        '''Метод позволяет пользователю просматривать выбирать пункты меню '''

        if cmd:
            self.main_menu(cmd)
        else:
            print("1. Посмотреть список всех фермерских рынков")
            print("2. Найти рынки по городу, штату или почтовому индексу")
            print("3. Выбор действия три")
            print("0. Выйти из программы")
            cmd = input("Добрый день! Выберите пункт меню: ")
            self.main_menu(cmd)
    def main_menu(self, cmd):
        if cmd == "1":
            print(print("Sample: Market"))
        elif cmd == "2":
            print("Sample: Market location")
        elif cmd == "3":
            print("Empty")
        elif cmd == "0":
            print("Exit")
        else:
            print("Sample: Вы ввели неправильное значение")
s = ShowMainMenu()
s.chooser()

