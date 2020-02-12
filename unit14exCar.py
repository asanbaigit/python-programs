class CarBase:
    def __init__(self):
        self.n_of_tires = 4
        self.n_of_doors = 4
    
    def __str__(self):
        s = ''
        s = s + '# of tires = ' + str(self.n_of_tires) + '\n' 
        s = s + '# of doors = ' + str(self.n_of_doors) 
        return s

class CabrioCar(CarBase):
    def __init__(self):
        super().__init__()
        self.n_of_doors = 2
        self.roof_type = 'Custom'
    
    def __str__(self):
        s = super().__str__() + '\n'
        s = s + 'roof type = ' + str(self.roof_type)
        return s

c1 = CarBase()
print('----Car Base----')
print(c1)
c2 = CabrioCar()
print('----Cabrio car----')
print(c2)