class Bike: #створюємо Bike 
    def __init__(self, plate):
        self.plate = plate
    def kind(self):
        return "Звичайний" #тип велосипеда
    def fee_per_min(self): #скільки гривень за хвилину
        return 2
    def is_ready(self):  #чи готовий велосипед
        return True
    
    
class ElectricBike(Bike):
    def __init__(self, plate, battery=100): #додає батарею, якщо не вказано то 100
        super().__init__(plate) # в батьківського класу берем номер
        self.battery = battery
        self.minus_battery_per_min = 2
    def kind(self): #тип велосипеда
        return "Електро"
    def fee_per_min(self): #скільки гривень за хвилину
        return 5
    def is_ready(self):  #чи готовий велосипед, якщо заряд менше 20, то не можна
        if self.battery >= 20:
            return True
        return False
    def battery_persent(self): #процент батареї 
        return self.battery
    def recharge(self): #перезарядити велік
        self.battery = 100
    
