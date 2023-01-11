"""
view
tkinter
"""
from tkinter import Tk, Listbox, Scrollbar, RIGHT, Y, END, Button, Entry, RAISED
import class_model as cm


class Model:
    """commands to model"""
    def __init__(self, f_name):
        """init"""
        self.markets = cm.Model(f_name)

    def list_market(self):
        """show list of markets"""
        fm_list = self.markets.list_markets()
        win_list = Tk()
        win_list.title("List Farmers Markets")
        win_list.geometry("500x800")
        win_list.resizable(width=False, height=False)
        list_box = Listbox(win_list, height=500, width=800)
        scrollbar = Scrollbar(win_list, orient="vertical", command=list_box.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        list_box["yscrollcommand"] = scrollbar.set
        for i in fm_list:
            list_box.insert(END, i)
        list_box.pack()

    def all_cities(self):
        """show all cities"""
        cities_list = self.markets.all_cities()
        win_list = Tk()
        win_list.title("List All Cities")
        win_list.geometry("200x800")
        win_list.resizable(width=False, height=False)
        list_box = Listbox(win_list, height=200, width=800)
        scrollbar = Scrollbar(win_list, orient="vertical", command=list_box.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        list_box["yscrollcommand"] = scrollbar.set
        for i in cities_list:
            list_box.insert(END, i)
        list_box.pack()

    def find_by_zip(self):
        """find markets by ZIP CODE"""
        found_value.delete(0, END)
        zip_code = entry_find_by_zip.get()
        value = self.markets.find_by_zip(zip_code)
        if zip_code:
            for i in value:
                found_value.insert(END, i)

    def find_by_city(self):
        """find markets by ZIP CODE"""
        found_value.delete(0, END)
        city = entry_find_by_city.get()
        state = entry_find_by_state.get()
        markets = self.markets.find_by_city(city, state)
        if city:
            for i in markets:
                found_value.insert(END, i[0])

    def details_fm(self):
        """show details about markets"""
        found_value.delete(0, END)
        market = entry_details_fm.get()
        details = self.markets.detailed_data(market)
        show = []
        if len(details) > 1:
            show.append(f"Found {len(details)} markets")
            for found_market in details:
                show.append(f'ID: {found_market[7]}')
                show.append(f'Street of market: {found_market[0]}')
                show.append(f'City: {found_market[9]}')
                show.append(f'County: {found_market[10]}')
                show.append(f'State: {found_market[11]}')
                show.append(f'ZIP CODE: {found_market[4]}')
                show.append('Media:')
                for i in found_market[11:16]:
                    if len(i) > 0:
                        show.append(i)
                show.append(f'coordinates Y: {found_market[5]},  X: {found_market[6]}')
        elif len(details) == 1:
            show.append(f"Found {len(details)} markets")
            show.append(f'ID: {details[0][7]}')
            show.append(f'Street of market: {details[0][0]}')
            show.append(f'City: {details[0][9]}')
            show.append(f'County: {details[0][10]}')
            show.append(f'State: {details[0][11]}')
            show.append(f'ZIP CODE: {details[0][4]}')
            show.append('Media:')
            for i in details[0][11:16]:
                if len(i) > 0:
                    show.append(i)
            show.append(f'coordinates Y: {details[0][5]},  X: {details[0][6]}')
        if market:
            for i in show:
                found_value.insert(END, i)


fm_database = Model('server.db')
win = Tk()
win.title("Farmers Markets")
win.geometry("600x400")
win.resizable(width=False, height=False)
btn_fm_list = Button(win, text="List Farmers Markets", bd=3, command=fm_database.list_market)
btn_all_cities = Button(win, text="All Cities", bd=3, command=fm_database.all_cities)
btn_find_by_zip = Button(win, text="Find Markets by ZIP", bd=3, command=fm_database.find_by_zip)
entry_find_by_zip = Entry(win, relief=RAISED, bd=3)
btn_find_by_city = Button(win, text="Find Markets by City and State", bd=3,
                          command=fm_database.find_by_city)
entry_find_by_city = Entry(win, relief=RAISED, bd=3)
entry_find_by_state = Entry(win, relief=RAISED, bd=3)
btn_details_fm = Button(win, text="Show Details about Markets", bd=3,
                        command=fm_database.details_fm)
entry_details_fm = Entry(win, relief=RAISED, bd=3)


found_value = Listbox(win, bg='white', relief=RAISED, height=18)


btn_fm_list.grid(row=0, column=0, stick='we')
btn_all_cities.grid(row=0, column=1, stick='we', columnspan=2)
btn_find_by_zip.grid(row=1, column=0, stick='we')
entry_find_by_zip.grid(row=1, column=1, stick='we', columnspan=2)
btn_find_by_city.grid(row=3, column=0, stick='we')
entry_find_by_city.grid(row=3, column=1, stick='we')
entry_find_by_state.grid(row=3, column=2, stick='we')
btn_details_fm.grid(row=4, column=0, stick='we')
entry_details_fm.grid(row=4, column=1, stick='we', columnspan=2)

found_value.grid(row=7, column=0, stick='we', columnspan=3)
win.grid_columnconfigure(0, minsize=300)
win.grid_columnconfigure(1, minsize=150)
win.grid_columnconfigure(2, minsize=150)

win.mainloop()
