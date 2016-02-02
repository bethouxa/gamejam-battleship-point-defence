# -*- encoding: utf-8 -*-

from random import randint
from math import cos,sin,radians
import Constantes

class Ennemi(object):
    def __init__(self, hp, freq_tir, vitesse, angle=randint(0,180), position=(Constantes.hauteur_ecran,randint(0,Constantes.largeur_ecran))):
        self.hp = hp
        self.freq_tir = freq_tir # proba de tir à chaque seconde
        self.vitesse = vitesse # en pixels seconde
        self.position = position
        self.angle = angle

    def deplacer(self):
        self.position = (self.position[0]-(self.vitesse*sin(radians(self.angle))),
                        self.position[1]+self.vitesse*cos(radians(self.angle)))

def test():
    e = Ennemi(100,0.33,100, -90)
    from utils import vardump
    vardump(e)
    for i in range(10):
        e.deplacer()
        print(e.angle)
        print(e.position)

if __name__ == '__main__':
    test()

