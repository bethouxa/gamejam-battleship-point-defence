import sys
import pygame
import os

# Methode permettant de charger une image
# et renvoie l'objet surface associee
def load_image(name):
    image = pygame.image.load(name)
    return image

# Init modules pygames
pygame.init()

# Charge l'image de fond
background_image = load_image("assets/sprites/background.jpg")
background_position = [0, 0]

# Affiche la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Lance la musique
pygame.mixer.music.load('assets/music/11023.mp3')
pygame.mixer.music.play()

# vaisseau alliÃ©
vaisseau = load_image("assets/sprites/vaisseau.png")
vaisseau_position = [220,280]

# vaisseau ennemie
speed = [1, 1]
vaisseau_ennemie = load_image("assets/sprites/ennemi.png")

# On charge le rectangle de vaisseau, correspondant a
# un tableau definissant sa position
vaisseau_rect = vaisseau_ennemie.get_rect()

# Boucle de jeu
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Deplacement de la position (cordonnees du rectangle) de l'invader
    # en fonction du tableau speed
	vaisseau_rect = vaisseau_rect.move(speed)

	# Test la position de ce rectangle pour savoir si il a touche
    # un mur : les attributs left, right, bottom, top correspondent
    # au cordonnees en x ou y du carre
	if vaisseau_rect.left < 0 or vaisseau_rect.right > width:
		speed[0] = -speed[0]

	if vaisseau_rect.top < 0 or vaisseau_rect.bottom > height:
		speed[1] = -speed[1]


	# Ajoute nos images a la file des affichages prevus
    # On ajoute le fond d'abord pour que notre invader soit "par dessus"
	screen.blit(background_image, background_position)
	screen.blit(vaisseau, vaisseau_position)
	screen.blit(vaisseau_ennemie, vaisseau_rect)

	# Affiche toute la file
	pygame.display.flip()
	screen.blit

	# Limite le nombre d'images par seconde
	pygame.time.wait(10)