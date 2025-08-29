from Product import Product
from WarehouseManager import WarehouseManager

#CREATE INSTANCES
warehouse = WarehouseManager(30000)
product1 = Product('Iphone', '1200', '5000')
product2 = Product('Samsung', '1000', '7000')
warehouse.add_product(product1)
warehouse.add_product(product2)

# PRINT PRODUCTS IN WAREHOUSE
for product_name, product in warehouse.products.items():
    print(f"Nome: {product.name}, Prezzo: {product.price}, Stock: {product.stock}")