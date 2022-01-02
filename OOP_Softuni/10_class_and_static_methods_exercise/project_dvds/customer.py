class Customer:

    def __init__(self, name, age, id_customer):
        self.name = name
        self.age = age
        self.id = id_customer
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} \
rented DVD's ({' ,'.join(x.name for x in self.rented_dvds)})"
