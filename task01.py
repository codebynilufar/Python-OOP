class Car:
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year


car = Car("BMW","BMW X5", 2022 )
print(f"Brand : {car.brand}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")


