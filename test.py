import pygame

pygame.init()

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

continuer = True

while continuer:
    # ici on crée un rectangle de couleur rose, en x=0, y=0 et de taille 300 sur 200
    # nous verrons plus tard comment faire plus en détail :)
    pygame.draw.rect(ecran, (180, 20, 150), (0, 0, 300, 200))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    # ici on actualise l'écran, car on a affiché un rectangle rose, et on veut qu'il soit
    # visible. Si l'on avait pas mit cette instruction, on n'aurait jamais vu le rectangle !
    pygame.display.flip()

pygame.quit()