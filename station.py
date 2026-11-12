class Station:
    def __init__(self, name: str):
        """Ініціалізує станцію з назвою та порожнім списком велосипедів"""
        pass

    def add_bike(self, bike: Bike) -> None:
        """Додає велосипед на станцію"""
        pass

    def take_bike(self, bike_type: str = None):
        """Забирає зі станції вільний велосипед потрібного типу і повертає його, а якщо немає - None"""
        pass

    def bikes_count(self) -> int:
        """Повертає кількість велосипедів, які зараз на станції"""
        pass
