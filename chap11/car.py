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