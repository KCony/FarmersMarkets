import server as s


class ShowMainMenu:

    def __init__(self):
        self.show_list = []
        self.database = s.Database()
        if not self.database.open_database("Export.csv"):
            pass

    def chooser(self, cmd=None):
        '''Метод позволяет пользователю просматривать выбирать пункты меню '''

        if cmd:
            self.main_menu(cmd)
        else:
            cmd = input("Добрый день! Выберите пункт меню: ")
            self.main_menu(cmd)

    def menu_display(self):
        self.menu = {"1": "1. Посмотреть список всех фермерских рынков",
                     "2": "2. Найти рынки по городу, штату или почтовому индексу",
                     "3": "3. Выбор действия три", "0": "0. Выйти из программы"}

        print(*self.menu.values(), sep="\n")

    def main_menu(self, cmd):
        if cmd == "1":
            print("pass")

        elif cmd == "2":
            city =  input("Введите город: ")
            state =  input("Введите штат: ")
            self.show_list = self.database.show_filtered_markets_city_state(self.database.data, city, state)
            viewer = Viewer(self)
            viewer.show_city_state()
        elif cmd == "3":
            print("Empty")

        elif cmd == "0":
            print("Exit")

        else:
            print("Sample: Вы ввели неправильное значение")



class Viewer:

     def __init__(self, showmainmenu):
         self.show = showmainmenu

     def show_city_state(self):
         res_list = []
         for i, n in enumerate(self.show.show_list):
             li = dict(n).get("MarketName")
             res_list.append(li)
         print(res_list)

if __name__ == '__main__':
 show_main = ShowMainMenu()
 show_main.menu_display()
 show_main.chooser()
