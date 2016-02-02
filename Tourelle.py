# -*- encoding: utf-8 -*-

from Projectile import Projectile
import Constantes

class Tourelle(object):
    def __init__(self, position):
        self.position = position
        self.angle = 90
        self.vitesse_rotation = 90
        self.type_projectile = ''

        self.sprite = ""

    def tir(self): # Virtual
        pass

    def mouvement(self,sens):
        delta = self.vitesse_rotation/Constantes.fps_cap
        if sens == 'gauche':
            self.angle = min(self.angle+delta,180) # bloque une fois arrivé à l'horizontale
        elif sens == 'droite':
            self.angle = max(self.angle-delta,0)



def test():
    import utils
    t = Tourelle((10,15))
    utils.vardump(t)
    t.mouvement('gauche')
    print(t.angle)
    for i in range(50):
        t.mouvement('droite')
        print(t.angle)
    t.mouvement('gauche')
    print(t.angle)
    t.mouvement('gauche')
    print(t.angle)

if __name__ == '__main__':
    test()
