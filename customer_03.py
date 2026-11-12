class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance  # ініціалізація

    def ride(self, station_from, bike_type, time, station_to):
        if time <= 0:
            raise ValueError("Час має бути додатним")  # перевірка часу

        bike = station_from.take_bike(bike_type)  # забираємо байк зі станції
        if bike is None:
            raise ValueError("На станції немає вільного велосипеда такого типу")

        if not bike.is_ready():
            station_from.add_bike(bike)  # повертаємо, якщо низький заряд
            raise ValueError("Велосипед не готовий (низький заряд)")

        price = time * bike.fee_per_min()  # розрахунок вартості
        if price > self.balance:
            station_from.add_bike(bike)  # повертаємо, якщо недостатньо коштів
            raise ValueError("Недостатньо коштів на балансі")

        bike.ride(time)  # розряджаємо батарею
        station_to.add_bike(bike)  # ставимо байк на кінцеву станцію
        self.balance -= price  # списуємо гроші після поїздки

        return price

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self.balance += amount
        return self.balance
