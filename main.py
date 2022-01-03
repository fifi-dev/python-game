import pygame


module_charge = pygame.init ()
print (module_charge)

ecran = pygame.display.set_mode((500,500))
pygame.display.set_caption("Le jeu du pendu")
#image = pygame.image.load("logo.png").convert()
pygame.display.set_icon("logo.jpeg")

#print (image)



#vide le cache
pygame.quit()