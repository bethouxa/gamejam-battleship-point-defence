#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
from pygame.locals import *
import os
from random import random

import Constantes

def afficher_menu(screen):
    try:
        smonoBig = pygame.font.Font("assets/polices/Simply Mono.ttf",35)
        smonoMedium = pygame.font.Font("assets/polices/Simply Mono.ttf",25)
    except Exception as e:
        print("La police de caractères du menu n'a pu être ouverte :")
        print(e)
    surfaces_texte = list()
    surfaces_menu = list()
    surfaces_texte.append(smonoBig.render("BATTLESHIP POINT DEFENCE",True,(255,255,255)))
    surfaces_menu.append((smonoMedium.render("Jouer",True,(255,255,255)),"Jouer"))
    surfaces_menu.append((smonoMedium.render("Credits",True,(255,255,255)),"Credits"))
    surfaces_menu.append((smonoMedium.render("Quitter",True,(255,255,255)),"Quitter"))

    i=1
    for surf in surfaces_texte:
        screen.blit(surf,(125,i*60))
        i+=1

    button_list = list()
    for surf in surfaces_menu:
        button_list.append((screen.blit(surf[0],(350,i*100)),surf[1]))
        i+=1

    pygame.display.flip()

    while 1:

        for event in pygame.event.get():
            if event.type == Constantes.MOUSEBUTTONUP:
                for r in button_list:
                    if r[0].collidepoint(event.pos):
                        return r[1]

def affiche_sequence_intro():
    pass

def spawn_ennemis(ennemis,sprites_a_refresh):
    if len(ennemis) < Constantes.max_ennemis:
        if random() < Constantes.chance_spawn_ennemi:
            ennemis.append(Ennemi(100,0.33,200))
            sprites_a_refresh.append()

def action_cannon():
    pass

def jouer(screen):
    from Battleship import Battleship
    affiche_sequence_intro()
    sprites_a_refresh = list() # (surface,rect)[,...]
    bs = Battleship()

    background = pygame.image.load("assets/sprites/background.png")

    bs.surface = pygame.image.load(bs.sprite).convert()
    bs.rect = bs.surface.get_rect()

    bs.artillerie.surface = pygame.image.load(bs.artillerie.sprite)
    bs.artillerie.surface = bs.artillerie.surface.convert()
    bs.artillerie.rect = bs.artillerie.surface.get_rect()

    sprites_a_refresh.append(bs.rect)
    sprites_a_refresh.append(bs.artillerie.rect)

    screen.blit(background,(0,0))
    screen.blit(bs.artillerie.surface, (Constantes.vaisseau_position_x,Constantes.vaisseau_position_y+50))
    screen.blit(bs.surface, (Constantes.vaisseau_position_x,Constantes.vaisseau_position_y))

    pygame.display.flip()
    pygame.mixer.music.load('assets/musique/11023.mp3')
    pygame.mixer.music.play()
    try:
        while 1:
            fpsClock = pygame.time.clock()
            pygame.event.post(USEREVENT) # Déclencher spawn ennemis à la 1re frame
            ennemis = list()
            obus = list()
            bombes = list()

            if pygame.event.peek(USEREVENT):
                spawn_ennemis(ennemis,sprites_a_refresh)
                pygame.time.set_timer(USEREVENT,1000)
            #action_canon(bs.tourelle_active,obus,sprites_a_refresh)
            #toucher_ennemis(obus,ennemis,sprites_a_refresh)
            #action_ennemis(ennemis,bombes,sprites_a_refresh)
            #toucher_bs(obus,bs,sprites_a_refresh)

            pygame.display.update(sprites_a_refresh)

            #if bs.hp <= 0:
            #    raise GameOver
            fpsClock.tick(Constantes.fps_cap)
    except GameOver:
        print("perdu")
    return 0






def main():

    # Init modules pygames
    pygame.init()

    # Charge l'image de fond
    background_image = pygame.image.load("assets/sprites/background.jpg")
    background_position = [0, 0]

    # Affiche la fenetre
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    #size = width, height = Constantes.largeur_ecran,Constantes.hauteur_ecran
    size = width, height = 1366,850
    screen = pygame.display.set_mode(size)

    pygame.font.init()

    screen.blit(background_image, background_position)

    action = afficher_menu(screen)

    screen.fill((0,0,0))
    pygame.display.flip()

    if action == "Jouer":
        jouer(screen)
    elif action == "Credits":
        credits()
    elif action == "Quitter":
        pygame.quit()

    return "ok"


if __name__ == '__main__':
    main()
