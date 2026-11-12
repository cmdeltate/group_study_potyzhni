class Rental_Network():
    def __init__(self):
        # Створює порожній список станцій і лічильник заробітку revenue = 0.
        self.stations = []
        self.revenue = 0
    def add_station(self, station):
        # Додає об'єкт Station до списку станцій мережі.
        self.stations.append(station)


    def register_payment(self, amount):
        # Збільшує загальний заробіток мережі на суму amount (вартість поїздки).
        self.revenue += amount

    def bikes_per_station(self):
        # Повертає словник: назва станції ==> кількість велосипедів на ній.
        # Кількість бере через station.bike_count().
        return {station_name: station.bikes_count() for station in self.stations}

    def total_revenue(self):
        # Повертає накопичений загальний заробіток.
        return self.revenue

