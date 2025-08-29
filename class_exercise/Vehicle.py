#CLASS VEHICLE
class Vechicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def accelerate(self):
        print('Accelerate!')

    def brake(self):
        print('Brake!')

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}'
        
#CLASS AUTO
class Auto(Vechicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def accelerate(self):
        return super().accelerate()
    
    def brake(self):
        return super().brake()
    
    def change_color(self, p_color):
        self.color = p_color

    def __str__(self):
        return super().__str__() + f', Color: {self.color}'

auto = Auto('Mercedes', 'Class G AMG', '2025', 'Black')
#STAMPA PRENDENDO IL METODO __str__ DELLA CLASSE
print(auto)
auto.accelerate()
auto.brake()
auto.change_color("Green")
print(auto)