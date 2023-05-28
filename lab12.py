def n1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Название ресторана: ", self.restaurant_name, "\nТип кухни: ", self.cuisine_type)

        def open_restaurant(self):
            print("\nРесторан открыт")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = ["ванильное", "шоколадное", "клубничное", "пломбир"]

        def display_flavors(self):
            print("\nВкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

    stand = IceCreamStand("Цех 85", "Кафе - Мороженое")
    stand.describe_restaurant()
    stand.display_flavors()
    stand.open_restaurant()
# n1()
def n2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print("Название ресторана: ", self.restaurant_name, "\nТип кухни:  ", self.cuisine_type)

        def open_restaurant(self):
            print("Ресторан открыт")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, location, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = ["ванильное", "шоколадное", "клубничное", "пломбир"]
            self.location = location
            self.time = time

        def display_flavors(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)

        def add_flavor(self, new_flavor):
            self.flavors.append(new_flavor)
            print("\nБыло добавлено в список вкусов мороженого - ", new_flavor)

        def remove_flavor(self, removed_flavor):
            self.flavors.remove(removed_flavor)
            print("Было удалено из списка вкусов мороженого - ", removed_flavor)

        def has_flavor(self, flavor):
            if flavor in self.flavors:
                print("\nРесторан -", self.restaurant_name, "имеет в ассортименте вкус:", flavor)
            else:
                print("Ресторан -", self.restaurant_name, "не имеет в ассортименте вкус:", flavor)

    class IceCreamOnStick(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, time, stick_type):
            super().__init__(restaurant_name, cuisine_type, location, time)
            self.stick_type = stick_type

        def display_stick_type(self):
            print("\nРесторан использует", self.stick_type, "палочки для мороженого на палочке")

        def change_stick_type(self, new_type):
            self.stick_type = new_type
            print("Ресторан использует новые", new_type, "палочки для мороженого на палочке")

    class SoftServeIceCream(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, hours, toppings):
            super().__init__(restaurant_name, cuisine_type, location, hours)
            self.toppings = toppings

        def display_toppings(self):
            print("\nТопинги: ")
            for topping in self.toppings:
                print(topping)

        def add_topping(self, new_topping):
            self.toppings.append(new_topping)
            print("\nБыл добавлен в список топингов - ", new_topping)

        def remove_topping(self, removed_topping):
            self.toppings.remove(removed_topping)
            print("Был удалён из списка топингов - ", removed_topping)

    my_ice_cream_stand = IceCreamStand("Цех 85", "Кафе - Мороженое", "Невский пр. д.52",
                                       "8:00 - 21:00 по будням, 9:00 - 22:00 по выходным")
    my_ice_cream_stand.display_flavors()
    my_ice_cream_stand.add_flavor("банановое")
    my_ice_cream_stand.remove_flavor("клубничное")
    my_ice_cream_stand.has_flavor("шоколадное")
    my_ice_cream_stand.has_flavor("алкогольное")

    my_ice_cream_on_stick = IceCreamOnStick("Цех 86", "Кафе - Мороженое", "Невский пр. д.52",
                                            "8:00 - 21:00 по будням, 9:00 - 22:00 по выходным", "деревянные")
    my_ice_cream_on_stick.display_stick_type()
    my_ice_cream_on_stick.change_stick_type("пластиковые")

    my_soft_serve = SoftServeIceCream("Цех 87", "Кафе - Мороженое", "Невский пр. д. 52",
                                      "8:00 - 21:00 по будням, 9:00 - 22:00 по выходным",
                                      ["посыпка", "шоколадная крошка", "карамель", "вишнёвый сироп"])
    my_soft_serve.display_toppings()
    my_soft_serve.add_topping("клубничный сироп")
    my_soft_serve.remove_topping("карамель")
# n2()
from tkinter import *
def n3():
    class IceCreamStand:
        def __init__(self, location, working_hours):
            self.location = location
            self.working_hours = working_hours
            self.flavors = []

        def add_flavor(self, flavor):
            self.flavors.append(flavor)

        def remove_flavor(self, flavor):
            self.flavors.remove(flavor)

        def check_flavor(self, flavor):
            return flavor in self.flavors

    class IceCreamApp:
        def __init__(self, ice_cream_stand):
            self.ice_cream_stand = ice_cream_stand

            self.root = Tk()
            self.root.title("Кафе - Мороженое")

            self.info_frame = Frame(self.root, padx=10, pady=5)
            self.info_frame.grid(row=0, column=0, sticky=W)

            self.flavors_label = Label(self.info_frame, text="Вкусы:")
            self.flavors_label.pack(anchor=W)
            self.flavors_var = StringVar()
            self.flavors_var.set(", ".join(self.ice_cream_stand.flavors))
            self.flavors_listbox = Listbox(self.info_frame, listvariable=self.flavors_var)
            self.flavors_listbox.pack(anchor=W)
            self.flavor_entry = Entry(self.info_frame, width=20)
            self.flavor_entry.pack(side=LEFT, padx=5)
            self.add_button = Button(self.info_frame, text="Добавить", command=self.add_flavor)
            self.add_button.pack(side=LEFT)
            self.remove_button = Button(self.info_frame, text="Удалить", command=self.remove_flavor)
            self.remove_button.pack(side=LEFT)

            self.info_frame2 = Frame(self.root, padx=10, pady=5)
            self.info_frame2.grid(row=0, column=1, sticky=E)

            self.location_label = Label(self.info_frame2, text="Местоположение: " + self.ice_cream_stand.location)
            self.location_label.pack(anchor=W)
            self.working_hours_label = Label(self.info_frame2,
                                             text="Часы работы: " + self.ice_cream_stand.working_hours)
            self.working_hours_label.pack(anchor=W)

            self.root.mainloop()

        def add_flavor(self):
            flavor = self.flavor_entry.get().strip()
            if flavor != "" and not self.ice_cream_stand.check_flavor(flavor):
                self.ice_cream_stand.add_flavor(flavor)
                self.flavors_var.set(", ".join(self.ice_cream_stand.flavors))

        def remove_flavor(self):
            flavor = self.flavors_listbox.get(ACTIVE)
            if flavor != "" and self.ice_cream_stand.check_flavor(flavor):
                self.ice_cream_stand.remove_flavor(flavor)
                self.flavors_var.set(", ".join(self.ice_cream_stand.flavors))

    ice_cream_stand = IceCreamStand("Невский пр. д.52", "8:00 - 21:00")
    ice_cream_stand.add_flavor("ванильное")
    ice_cream_stand.add_flavor("шоколадное")
    ice_cream_stand.add_flavor("клубничное")

    app = IceCreamApp(ice_cream_stand)
# n3()
