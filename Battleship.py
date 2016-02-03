# -*- encoding: utf-8 -*-

from Artillerie import Artillerie
#from AA import AA
import Constantes

class Battleship(object):
    def __init__(self):
        self.hp = 100
        self.artillerie = Artillerie((100,100)) # boom boom
        #self.aa = AA() # pewpewpew
        self.tourelle_active = self.artillerie

        self.sprite = "assets/sprites/bs.png"
