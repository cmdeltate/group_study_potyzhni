import random


class Station:
    def __init__(self, name: str):
        """Ініціалізує станцію з назвою та порожнім списком велосипедів"""
        self.name = name
        self.bikes = []

    def add_bike(self, bike: Bike) -> None:
        """Додає велосипед на станцію"""
        self.bikes.append(bike)

    def take_bike(self, bike_type: str = None):
        """Забирає зі станції вільний велосипед потрібного типу і повертає його, а якщо немає - None"""
        if not self.bikes:
            return None
        if bike_type == None:
            return random.choice(self.bikes)
        for bike in self.bikes:
            if bike.bike_type == bike_type:
                self.bikes.remove(bike)
                return bike

    def bikes_count(self) -> int:
        """Повертає кількість велосипедів, які зараз на станції"""
        return len(self.bikes)
