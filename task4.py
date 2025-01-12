class Autobus:
    def __init__(self, start_point, end_point, route_number, travel_time):
        self.start_point = start_point
        self.end_point = end_point
        self.route_number = route_number
        self.travel_time = travel_time

    def __str__(self):
        return f"Маршрут №{self.route_number}: {self.start_point} -> {self.end_point}, Время поездки: {self.travel_time} мин"

    def set_start_point(self, start_point):
        self.start_point = start_point

    def get_start_point(self):
        return self.start_point

    def set_end_point(self, end_point):
        self.end_point = end_point

    def get_end_point(self):
        return self.end_point

    def set_route_number(self, route_number):
        self.route_number = route_number

    def get_route_number(self):
        return self.route_number

    def set_travel_time(self, travel_time):
        self.travel_time = travel_time

    def get_travel_time(self):
        return self.travel_time


def save_to_file(bus_list, filename):
    with open(filename, 'w') as file:
        for bus in bus_list:
            file.write(f"{bus.start_point},{bus.end_point},{bus.route_number},{bus.travel_time}\n")
    print(f"Список автобусов сохранен в файл '{filename}'.\n")


def read_from_file(filename):
    try:
        bus_list = []
        with open(filename, 'r') as file:
            for line in file:
                start_point, end_point, route_number, travel_time = line.strip().split(',')
                bus = Autobus(start_point, end_point, int(route_number), int(travel_time))
                bus_list.append(bus)
        print(f"Список автобусов загружен из файла '{filename}':\n")
        for bus in bus_list:
            print(bus)
        print()
        return bus_list
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.\n")
        return []


def sort_buses_by_route_number(bus_list):
    if not bus_list:
        print("Список автобусов пуст. Нечего сортировать.\n")
        return bus_list
    sorted_list = sorted(bus_list, key=lambda bus: bus.route_number, reverse=True)
    print("Список автобусов отсортирован по убыванию номера маршрута:\n")
    for bus in sorted_list:
        print(bus)
    print()
    return sorted_list


def search_buses_by_stop(bus_list, stop_name):
    if not bus_list:
        print("Список автобусов пуст. Нечего искать.\n")
        return []
    result = [
        bus for bus in bus_list
        if bus.start_point.lower() == stop_name.lower() or bus.end_point.lower() == stop_name.lower()
    ]
    if result:
        print(f"Автобусы, которые начинаются или заканчиваются на остановке '{stop_name}':\n")
        for bus in result:
            print(bus)
    else:
        print(f"Автобусы с остановкой '{stop_name}' не найдены.\n")
    print()
    return result


def create_autopark():
    buses = []
    while True:
        print("\nДобавление автобуса:")
        start_point = input("Введите начальный пункт: ").strip()
        while not start_point:
            print("Начальный пункт не может быть пустым. Попробуйте снова.")
            start_point = input("Введите начальный пункт: ").strip()

        end_point = input("Введите конечный пункт: ").strip()
        while not end_point:
            print("Конечный пункт не может быть пустым. Попробуйте снова.")
            end_point = input("Введите конечный пункт: ").strip()

        route_number = input("Введите номер маршрута (целое число): ").strip()
        while not route_number.isdigit():
            print("Номер маршрута должен быть целым числом. Попробуйте снова.")
            route_number = input("Введите номер маршрута (целое число): ").strip()
        route_number = int(route_number)

        travel_time = input("Введите время поездки (целое число в минутах): ").strip()
        while not travel_time.isdigit() or int(travel_time) <= 0:
            print("Время поездки должно быть положительным целым числом. Попробуйте снова.")
            travel_time = input("Введите время поездки (целое число в минутах): ").strip()
        travel_time = int(travel_time)

        buses.append(Autobus(start_point, end_point, route_number, travel_time))

        add_more = input("Добавить еще один автобус? (да/нет): ").strip().lower()
        while add_more not in ["да", "нет"]:
            print("Введите 'да' для продолжения или 'нет' для завершения.")
            add_more = input("Добавить еще один автобус? (да/нет): ").strip().lower()
        if add_more == "нет":
            break

    print("\nАвтопарк создан вручную:\n")
    for bus in buses:
        print(bus)
    print()
    return buses


def main():
    filename = "buses.txt"
    buses = []

    while True:
        print("Выберите способ создания списка автобусов:")
        print("1. Автоматически заполнить список")
        print("2. Ввести данные вручную")
        choice = input("Ваш выбор (1/2): ").strip()

        if choice == "1":
            buses = [
                Autobus("Москва", "Сочи", 101, 240),
                Autobus("Санкт-Петербург", "Воронеж", 202, 300),
                Autobus("Казань", "Омск", 305, 180),
                Autobus("Екатеринбург", "Тюмень", 106, 120),
            ]
            print("Список автобусов создан автоматически:\n")
            for bus in buses:
                print(bus)
            save_to_file(buses, filename)
            buses = read_from_file(filename)
            break
        elif choice == "2":
            buses = create_autopark()
            save_to_file(buses, filename)
            buses = read_from_file(filename)
            break
        else:
            print("Неверный выбор. Введите 1 или 2.")

    while True:
        print("\nМеню:")
        print("1. Отсортировать автобусы по убыванию номера маршрута")
        print("2. Найти автобусы по остановке")
        print("3. Вывести список автобусов")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            buses = sort_buses_by_route_number(buses)
            save_to_file(buses, filename)  
        elif choice == "2":
            if not buses:
                print("Список автобусов пуст. Выполните загрузку или создание списка.\n")
            else:
                stop_name = input("Введите название остановки для поиска: ").strip()
                while not stop_name:
                    print("Название остановки не может быть пустым. Попробуйте снова.")
                    stop_name = input("Введите название остановки для поиска: ").strip()
                search_buses_by_stop(buses, stop_name)
        elif choice == "3":
            if not buses:
                print("Список автобусов пуст.\n")
            else:
                print("\nСписок автобусов:\n")
                for bus in buses:
                    print(bus)
                print()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Введите число от 0 до 3.")


if __name__ == "__main__":
    main()