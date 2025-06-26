class Car:
    model = str
    year = int
    available = bool = True

    def __init__(self,model, year):
        self.model = model
        self.year = year
        # self.available = available

    def rent_car(self):
        if self.available:
            self.available = False
            print("Car on Rent Successful")
        else:
            print("Car is not available")
    
    def return_car(self):
        self.available = True
        print("Car is Available for rent again.")
    

    def display_status(self):
        print(self.model)
        print(self.year)
        print(f"Car is available = {self.available}")

car1 = Car('Swift', 2019)
car1.rent_car()
car1.return_car()