class Product:
    """
    Dataclass to represent a product that can be found on ProductListPage
    """
    def __init__(self, title: str, description: str, price: str):
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product<{self.title, self.description[:20], self.price}>"
