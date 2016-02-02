# -*- encoding: utf-8 -*-

from Tourelle import Tourelle
from Projectile import Projectile

class Artillerie(Tourelle):
    def __init__(self,position):
        super().__init__(position)
        self.type_projectile = 'obus'
        self.vitesse_rotation = 75
        self.sprite = ""

    def tir(self):
        return Projectile(self.position,self.angle)
        #return Obus(self.position,self.angle)

def test():
    a = Artillerie((10,10))
    t = a.tir()

    print("Artillerie : "+str(vars(a)))
    print("Obus tiré : "+str(vars(t)))

if __name__ == '__main__':
    test()
