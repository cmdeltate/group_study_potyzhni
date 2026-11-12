class Bike:
    def __init__(self, plate):
        self.plate = plate
    def kind(self):
        return "Звичайний"
    def fee_per_min(self):
        return 2
    def is_ready(self):
        return True
    
    
class ElectricBike(Bike):
    def __init__(self, plate, battery=100):
        super().__init__(plate)
        self.battery = battery
        self.minus_battery_per_min = 2
    def kind(self):
        return "Електро"
    def fee_per_min(self):
        return 5
    def is_ready(self):
        if self.battery > 20:
            return True
        return False
    def battery_persent(self):
        return self.battery
    def recharge(self):
        self.battery = 100
    
