# -*- encoding: utf-8 -*-

#Utilitaires :
def vardump(thing):
    print(str(thing.__class__.__name__) + " : " + str(vars(thing)))
