class Product:
    def __init__(self, name, price, category, in_stock) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self) -> str:
        if self.in_stock:
            return f"{self.name} omborda mavjud."
        else:
            return f"{self.name} omborda mavjud emas!"

product01 = Product("Airpods", 17, "electronics", True)
product02 = Product("iPhone", 450, "electronics", False)

print(product01.check_stock())
print(product02.check_stock())
