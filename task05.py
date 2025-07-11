class Product:
    def __init__(self, name, price, category, in_stock) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product01 = Product("Airpods", "$17", "electronics","True" )
product02 = Product("Pen", "1.999.99", "Stationery", "True")

print(f"{product01.name}-{product01.price}")
print(f"{product02.name}-{product02.price} so'm")
