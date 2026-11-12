class Customer:
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance   #ініціалізація
    def ride(self, station_from, bike_number, time, station_to):
        if time <= 0:
            raise ValueError("Час не може бути від'ємним")  #перевірка на від'ємний час

        bike = station_from.take_bike(bike_number)   #забираємо байк ці станції
        price = time * bike.fee_per_min()    #розрахунок вартості
        if price > self.balance:
            station_from.add_bike(bike)   #повернення байка на станцію,якщо недостатньо коштів
            raise ValueError("Недостатньо коштів на балансі")   #перевірка бплансу

        station_to.add_bike(bike)  #додавання байку до кінцевої станції
        self.balance -= price    #обчислення балансу після поїздки

        return price

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self.balance += amount
        return self.balance


