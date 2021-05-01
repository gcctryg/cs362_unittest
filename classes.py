class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

car1 = Car("tesla model 3", 2017)
car2 = Car("honda", 1980)


# print(car1)
# print(car2.name)

class eletricCars(Car):
    pass

ec1 = eletricCars("Roadster", 2020)
print(ec1.name)

