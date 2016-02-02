# -*- encoding: utf-8 -*-

from math import cos,sin,radians
import Constantes

class Projectile(object):
    def __init__(self,position,angle):
        self.position = position
        self.vitesse = 20
        self.angle = angle
        self.degats = 150

    def deplacer(self):
        self.position = (self.position[0]-self.vitesse*sin(radians(self.angle))/Constantes.fps_cap,
                        self.position[1]+self.vitesse*cos(radians(self.angle))/Constantes.fps_cap)

def test():
    p = Projectile((20,50),30)
    for i in range(10):
        print(p.position)
        p.deplacer()
    p = Projectile((20,50),-90)
    for i in range(10):
        print(p.position)
        p.deplacer()

if __name__ == '__main__':
    test()
