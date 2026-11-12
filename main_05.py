from bikes_01 import Bike, ElectricBike
from station_02 import Station
from customer_03 import Customer
from rantal_04 import Rental_Network


def main():
    """Що робить: цикл роботи прокату велосипедів
    Що повертає: нічого
    """
    # система обліку мережі
    network = Rental_Network()

    # №1 Створити 2 станції
    station_1 = Station("Історичний музей")
    station_2 = Station("Наукова")
    network.add_station(station_1)
    network.add_station(station_2)

    # №2 Створити 4 велосипеди (звичайні й електричні) та поставити їх на станції
    bike1 = Bike("A-123")
    bike2 = Bike("A-456")
    bike3 = ElectricBike("B-789")
    bike4 = ElectricBike("B-025")

    station_1.add_bike(bike1)
    station_1.add_bike(bike2)
    station_2.add_bike(bike3)
    station_2.add_bike(bike4)

    # №3 Створити 2 клієнтів з різним балансом
    customer1 = Customer("Стася", 800)
    customer2 = Customer("Даша", 550)

    # №4 Провести 3 поїздки між станціями
    try:
        cost1 = customer1.ride(station_1, "Звичайний", 15, station_2)
        network.register_payment(cost1)
        print(f"Стася поїхала на звичайному велосипеді. Вартість: {cost1} грн.")

        cost2 = customer2.ride(station_2, "Електро", 10, station_1)
        network.register_payment(cost2)
        print(f"Даша поїхала на електричному велосипеді. Вартість: {cost2} грн.")

        cost3 = customer1.ride(station_2, "Електро", 20, station_1)
        network.register_payment(cost3)
        print(f"Стася поїхала на велосипеді вдруге. Вартість: {cost3} грн.")
    except ValueError as error:
        print(f"Помилка під час поїздки: {error}")

    # №5 Спробувати взяти велосипед, якого немає, і показати зрозуміле повідомлення
    failed = station_1.take_bike("Неіснуючий тип")
    if failed is None:
        print("На станції немає такого велосипеда")

    # №6 Показати баланс клієнтів після поїздок
    print(f"Баланс клієнта {customer1.name}: {customer1.balance} грн")
    print(f"Баланс клієнта {customer2.name}: {customer2.balance} грн")

    # №7 Звіт адміністратора
    info = network.bikes_per_station()
    for station_name, count in info.items():
        print(f"Станція '{station_name}': {count} велосипедів")
    print(f"Виручка мережі: {network.total_revenue()} грн")


if name == "main":
    main()
