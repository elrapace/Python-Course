#CLASS ANIMAL
class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    def emetti_suono(self):
        if self.specie == 'Cat':
            print('Miao!')
        elif self.specie == 'Dog':
            print("Bau!")
        else:
            print('Specie sconosciuta!')

cat = Animal("Ernesto", "Cat")
cat.emetti_suono()

dog = Animal("Franco", "Dog")
dog.emetti_suono()

bear = Animal('Aldo', 'Bear')
bear.emetti_suono()