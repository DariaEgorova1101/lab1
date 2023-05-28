def n1():
    class Restaurant:
        def __init__(self, name):
            self.restaurant_name = name
            self.cuisine_type = type

        def describe_restaurant(self):
            print(" Название ресторана: ", self.restaurant_name, "\n Тип кухни:  ", self.cuisine_type)

        def open_restaurant(self):
            print(" Ресторан открыт")

    newRestaurant = Restaurant("Арням")
    newRestaurant.cuisine_type = " Армянская кухня "
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()
# n1()

def n2():
    class Restaurant:
        def __init__(self, name, type):
            self.restaurant_name = name
            self.cuisine_type = type

        def describe_restaurant(self):
            print(" Название ресторана: ", self.restaurant_name, "\n Тип кухни:  ", self.cuisine_type)

        def open_restaurant(self):
            print(" Ресторан открыт")

    r1 = Restaurant("Мама Рома", "Испанская")
    r2 = Restaurant("Ухань", "Китайская")
    r3 = Restaurant("Как дома", "Домашняя")

    r1.describe_restaurant()
    r2.describe_restaurant()
    r3.describe_restaurant()
# n2()
def n3():
    class Restaurant:
        def __init__(self, name, type, rating):
            self.restaurant_name = name
            self.cuisine_type = type
            self.rating = rating

        def describe_restaurant(self):
            print(" Название ресторана: ", self.restaurant_name, "\n Тип кухни:  ", self.cuisine_type)

        def open_restaurant(self):
            print(" Ресторан открыт")

        def new_rating_restaurant(self, new_rating):
            self.rating = new_rating
            print("Рейтинг ресторана ", self.restaurant_name, "обновлен до", self.rating,
                  "\nОбновлённый рейтинг ресторана - ", self.restaurant_name, "-", self.rating)

    r = Restaurant("Арням", "Армянская", 4)
    print("Изначальный рейтинг ресторана", r.restaurant_name, r.rating)
    r.new_rating_restaurant(5)
# n3()