class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        return f'{self.year} {self.brand} {self.model}'

    def update_odometer(self, kilometers):
        if kilometers >= self.odometer:
            self.odometer = kilometers

    def read_odometer(self):
        print(f'{self.odometer} kilometers')

    def increment_odometer(self, kilometers):
        self.odometer += kilometers

class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()

    
    
    def get_descriptive_name(self):
        super().get_descriptive_name()
        self.battery.describe_battery()

class Battery():
    def __init__(self):
        self.battery_size = 75

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge.')

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    