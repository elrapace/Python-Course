#CLASS WAREHOUSEMANAGER
class WarehouseManager:
    def __init__(self, price_warehouse):
        self.products = {}
        self.price_warehouse = price_warehouse

    #METHOD ADD PRODUCT
    def add_product(self, product):
        self.products[product.name] = product 
    #METHOD REMOVE PRODUCT
    def remove_product(self, product_name):
        self.products.pop(product_name)