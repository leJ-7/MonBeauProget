import pygame
import random
from game import Game

#initialisation de pygame
pygame.init()


fenetre = pygame.display.set_mode((1920,1080))

game = Game()      


#création d'une fenêtre de 640x480 pixel


#largeur = fenetre.get_width()
#largeur = fenetre.get_width()/largeur

#chargement et lancement de la music de jeu

#définit les musiques du jeu
son1 = pygame.mixer.Sound("son1.ogg")
son2 = pygame.mixer.Sound("son2.ogg")
son3 = pygame.mixer.Sound("son3.ogg")

#joue la première musique
son1.play(30,0,50000)

#joue la deuxième music et la met sur pause


#chargement de toute les images du jeu

#images de fond 
imageFond1 = pygame.image.load("fond11.jpg").convert()    
imageFond2 = pygame.image.load("fond14.jpg").convert() 
imageFond3 = pygame.image.load("fond15.jpg").convert() 



#image pluie
imagePluie1 = pygame.image.load("pluie3.png").convert_alpha()
imagePluie2 = pygame.image.load("pluie2.png").convert_alpha()


#images mobiles
imagePerso = pygame.image.load("guts1.png").convert_alpha() 
imageballe1 = pygame.image.load("gost.png").convert_alpha() 
imageBonus1 = pygame.image.load("bonus1.png").convert_alpha() 

#images paramètres
imagePlay = pygame.image.load("play1.png").convert_alpha() 
imagePlay2 = pygame.image.load("play2.png").convert_alpha()
imagePause = pygame.image.load("pause.png").convert_alpha() 
imagePlayB = pygame.image.load("playb.png").convert_alpha() 
imageRestar = pygame.image.load("restar1.png").convert_alpha() 

#images info
imageVie = pygame.image.load("vie.png").convert_alpha() 

##image texte 

#texte affichant le nombre de vie
fontTextVie = pygame.font.Font(None, 34)
imageTextVie = fontTextVie.render("0", True, (0, 0, 0))

#texte affichant le score
fontScore = pygame.font.Font(None, 34)
imageScore = fontScore.render("Score : 0", True, (255, 255, 15))

#création des rectangles pour les images statiques

#rectangle Fond1
rectFond1 = imageFond1.get_rect()
rectFond1.x = 0
rectFond1.y = 0

#rectangle Fond2
rectFond2 = imageFond2.get_rect()
rectFond2.x = 0
rectFond2.y = 0

#rectangle Fond3
rectFond3 = imageFond3.get_rect()
rectFond3.x = 0
rectFond3.y = 0

#rectangle pluie2
rectPluie1 = imagePluie1.get_rect()
rectPluie1.x = 0
rectPluie1.y = 0

#rectangle pluie2
rectPluie2 = imagePluie2.get_rect()
rectPluie2.x = 0
rectPluie2.y = 0



#rectangle play
rectPlay = imagePlay.get_rect()
rectPlay.x = rectFond1.size[0]/2-rectPlay.size[0]/2

rectPlay.y = rectFond1.size[1]-300
#rectangle play2
rectPlay2 = imagePlay2.get_rect()
rectPlay2.x = rectFond1.size[0]/2-rectPlay2.size[0]/2
rectPlay2.y = rectFond1.size[1]-300

#rectangle pause
rectPause = imagePause.get_rect()
rectPause.x = 10
rectPause.y = 10

#rectangle playb    
rectPlayB = imagePlayB.get_rect()
rectPlayB.x = 10
rectPlayB.y = 10

#rectangle restar
rectRestar = imageRestar.get_rect()
rectRestar.x = rectFond1.size[0]/2-rectRestar.size[0]/2
rectRestar.y = rectFond1.size[1]-300

#rectangle vie    
rectVie = imageVie.get_rect()
rectVie.x = rectFond1.size[0] - rectVie.size[0]
rectVie.y = 5

#rectange texte textvie
rectTextVie = imageTextVie.get_rect()
rectTextVie.x = rectFond1.size[0] - rectVie.size[0] - rectTextVie.size[0]
rectTextVie.y = 15

#rectangle texte score
rectScore = imageScore.get_rect()
rectScore.x = rectFond1.size[0]-190
rectScore.y = rectFond1.size[1]-90


#variable pour les différentes étapes du jeu 
continuer = 1 

# Boucle permettant de réinitialiser les différents composant du jeu et de pouvoir le recommencer
while continuer != 4 :
    
    
    #récupere le meilleur score dans un ficher de sauvegarde
    mscore = open("sauv.txt", "r")
    bestScore = int(mscore.read())
    mscore.close()

    #créer une image et un rectangle pour afficher le meilleur score
    fontScore2 = pygame.font.Font(None, 34)
    imageScore2 = fontScore2.render("BestScore : "+str(bestScore), True, (255, 0, 0))
    rectScore2 = imageScore2.get_rect()
    rectScore2.x = rectFond1.size[0]-190
    rectScore2.y = rectFond1.size[1]-55

    #permet regler l'horloge du jeu
    horloge = pygame.time.Clock()

    #variable de la collision entre avec la souris et le play
    colMousePlay = 0  

    #boucle permettant de demander le commencement du jeu
    while continuer == 1 :
        print(rectFond1.size[0])
        print(rectFond1.size[1])
        #réglage de la boucle à 30 tours par seconde
        horloge.tick(30)
    
        #affichage du fond1

        #affiche le score et le meilleurs score
        fenetre.blit(imageScore, rectScore)
        fenetre.blit(imageScore2, rectScore2)

        #affiche un play éclairé si la souris passe sur play
        if colMousePlay == 1:
            fenetre.blit(imagePlay2, rectPlay2)
        else:
            fenetre.blit(imagePlay, rectPlay)
   
        #rafraichissement
        pygame.display.flip()
        
        #parcours de la liste des evenements
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:     #ferme le programme si l'on appuie sur la croie de la fenêtre
                continuer = 4
            if event.type == pygame.MOUSEMOTION:            
                A=event.pos
                if rectPlay.collidepoint(A[0],A[1]) : #vérifie la colision entre la souris et le point
                    colMousePlay=1        
                else :
                    colMousePlay=0                                
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1 and  rectPlay.collidepoint(A[0],A[1]) :   #début le jeu en passant à l'étape suivant si l'on clique sur play
                    continuer = 2

            #fenetre.blit(imageFond1, rectFond1)
            fenetre.blit(imageFond1, rectFond1)
            
                
            


    #création des rectangles pour les images mobiles

    #rectangle personnage
    rectPerso = imagePerso.get_rect()
    rectPerso.x = rectFond1.size[0]/2 - (rectPerso.size[0]//2)  #met le perso le plus au centre que possible
    rectPerso.y = rectFond1.size[1]/2 - (rectPerso.size[1]//2)  #met le perso le plus au centre que possible

    #rectangle balle1
    rectballe1 = imageballe1.get_rect()
    rectballe1.x = random.randint(0,(rectFond1.size[0] - rectballe1.size[0]))  # donne un position aléatoire en x 
    rectballe1.y = rectFond1.size[1] - (rectballe1.size[1])                    # fait la balle première balle partir du bas

    #rectangle bonus1
    rectBonus1 = imageBonus1.get_rect()
    rectBonus1.x = random.randint(0,(rectFond1.size[0]- rectBonus1.size[0])) # donne un position aléatoire en x 
    rectBonus1.y = rectFond1.size[1]                                           # fait la balle première balle partir du bas


    #créer 2 liste permettant de créer les images et les rectangles des balles rajoutés ajoutés
    imageballe = []
    rectballe = []

    #variables de jeu  
    compteur = 0 #compte le nombre de boucle effectuer et permet de compte le temps pour le score  
    seconde = 0 #compte le nombre de seconde ainsi que le score
    bon1=0 #permet au bonus d'apparaître 
    P6=1 #permet au bonus de rebondir sur les bors
    P1=random.randint(1,3) #fait rebondir la balle sur les rebord ainsi que lui donner un vitesse et direction aléatoire
    P2=random.randint(1,3) #fait rebondir la balle sur les rebord ainsi que lui donner un vitesse et direction aléatoire
    Px=[] #fait rebondir les balles sur les rebord ainsi que les donner une vitesse et direction aléatoire
    Py=[] #fait rebondir les balles sur les rebord ainsi que les donner une vitesse et direction aléatoire
    vies = 1 #permet de compter le nombre de vie
    debcomp3s = 0 #permet de débuter le comptage des 3s
    comp3s = 0 #compte 3s
    comp5s=0 #compte 5 sec
    nbBalle = 0 #permet de compter le nombre de balle
    A=(0,0)
    inverseur = 1 #permet au balle d'apparaître un fois en haut un fois en bas
    immunité = 0 #permet de mettre l'huminité au joueur
    perso1 = 1 #permet d'afficher le perso 
    comp05s=0 
    P05 = 1
    para = 1 #variable pluie
    
    #arrête la première music 
    son1.stop()
    son2.play(20,0,150000)
    
    #boucle permettant de mettre le jeu sur pause sans réinitialiser tous les éléments
    while continuer == 2 or continuer == 5 :
        #joue la deuxième music
        
        #boucle de jeu 
        while continuer == 2 :
            
            #réglage de la boucle à 30 tours par seconde
            horloge.tick(30)
            
            #cacule le score
            compteur = compteur+1
            seconde = int(compteur/30)

            #permet de changer dans l'affichage le score et les vies
            Score ="Score : " +str(seconde)
            imageScore = fontScore.render(Score, True, (255, 255, 15))
            imageTextVie = fontTextVie.render(str(vies), True, (0, 0, 0))
    
            # on recupere l'etat du clavier
            touches = pygame.key.get_pressed()

            #permet finir la partie
            if touches[pygame.K_ESCAPE] :
                continuer=3

            #mouvement joueur
            if touches[pygame.K_LEFT]:
                game.perso1.mouv_left()
            if touches[pygame.K_RIGHT] :    
                game.perso1.mouv_right()
            if touches[pygame.K_UP]:
                game.perso1.mouv_up()
            if touches[pygame.K_DOWN] :    
                game.perso1.mouv_down()
    
            #empêche le perso de sorti du cadre
            if rectPerso.x <= 0 :
                rectPerso.x = 0    
            if rectPerso.x >= (rectFond1.size[0] -(rectPerso.size[0])) :
                rectPerso.x = rectFond1.size[0] -(rectPerso.size[0])
            if rectPerso.y <= 0 :
                rectPerso.y = 0
            if rectPerso.y >= rectFond1.size[1]-(rectPerso.size[1]) :
                rectPerso.y = rectFond1.size[1] -(rectPerso.size[1])

            #permet de faire apparaitre le bonus ainsi que de le faire bouger
            if bon1 == 0 or bon1 >= 2150 :                    
                rectBonus1.x = random.randint(0,(rectFond1.size[0] - rectBonus1.size[0])) 
                rectBonus1.y= rectFond1.size[1]
                bon1= 0

            bon1= bon1 + 1
            if rectBonus1.x <= 0 or (rectBonus1.x >= rectFond1.size[0]- (rectBonus1.size[0])) : 
                P6=-P6 
            
            if bon1 >= 450 :        
                rectBonus1.y = rectBonus1.y - 1
                rectBonus1.x = rectBonus1.x + random.randint(1,7)*((-1)**random.randint(1,10)) #permet au bonus de bouger comme une abeille
            
            if rectBonus1.x <= 0 :
                rectBonus1.x = 0    
            if rectBonus1.x >= (rectFond1.size[0] -(rectBonus1.size[0])) :
                rectBonus1.x = rectFond1.size[0] -(rectBonus1.size[0])

            
            #fait rebondir la balle sur les rebord
            if rectballe1.x < 0 or (rectballe1.x > rectFond1.size[0] - (rectballe1.size[0])) :
                P1=-P1
            if rectballe1.y < 0 or (rectballe1.y > rectFond1.size[1] - (rectballe1.size[1])) :
                P2=-P2

            #permet à la balle de se déplacer
            rectballe1.y = rectballe1.y + P2*1
            rectballe1.x = rectballe1.x + P1*1
            
            #rajoute un vie au perso quand il touche le bonus et active comp3S
            if rectPerso.colliderect(rectBonus1) :
                vies = vies + 1
                bon1=0
                debcomp3s = 1               
            
            #retire un vie au perso et active debcomp3s
            if rectPerso.colliderect(rectballe1) and vies > 1 and immunité ==0  :
                vies = vies - 1
                debcomp3s = 1
            for z in range(nbBalle):            
                if rectPerso.colliderect(rectballe[z])  and vies > 1 and immunité == 0 :
                    vies = vies - 1
                    debcomp3s = 1

            #débute l'imminuté
            if debcomp3s == 1 :
                comp3s = comp3s + 1
                immunité = 1
                comp05s = comp05s + 1
            
            #permet faire clignoté le perso pendant l'immunité
            if comp05s == 3 :
                P05=-P05
                comp05s = 0
            if P05 == 1 :
                perso1 = 1
            else:
                perso1 = 0
            
            #désactive l'immunité après 3 seconde
            if comp3s >= 90 :
                debcomp3s = 0                
                immunité = 0
                comp3s = 0
                P05=1

            #arrête le jeu si le joueur n'a plus de vies et n'a plus l'immunité
           # if rectPerso.colliderect(rectballe1) and vies <= 1 and immunité == 0 :
            #    continuer = 3    
            #for z in range(nbBalle):            
             #   if rectPerso.colliderect(rectballe[z])  and vies <= 1 and immunité == 0 :
               #     continuer = 3
            
            #donne une image aléatoire au fantome
            Jack = random.randint(1,3)
            if Jack == 1 :
                fantome = "gost.png"
            elif Jack == 2 :
                fantome = "gost2.png"
            else:
                fantome = "gost3.png"
            #rajoute une balle toutes les 5 secondes
            comp5s = comp5s + 1
            if comp5s >= 200 :
                nbBalle = nbBalle + 1 
                imageballe.append(pygame.image.load(fantome).convert_alpha())
                rectballe.append(imageballe[nbBalle-1].get_rect())
                Px.append(random.randint(1,3))
                Py.append(random.randint(1,3))
                rectballe[nbBalle-1].x = random.randint(0,rectFond1.size[0] - rectballe[nbBalle-1].size[0])
                if inverseur == 1 :
                    rectballe[nbBalle-1].y = 0
                    inverseur = 2
                else:
                    rectballe[nbBalle-1].y = rectFond1.size[1] - rectballe[nbBalle-1].size[1]
                    inverseur = 1
                comp5s = 0
    
            ##affiche toutes les images

            fenetre.blit(imageFond2, rectFond2)
            fenetre.blit(imageballe1, rectballe1)
            fenetre.blit(imageBonus1, rectBonus1)            

            if nbBalle >= 0 :
                for G in range(nbBalle):            
                    fenetre.blit(imageballe[G], rectballe[G])

                    #fait rebondir les balles
                    if rectballe[G].x < 0 or rectballe[G].x > (rectFond1.size[0] - (rectballe1.size[0])) :  
                        Px[G]=-Px[G]
                    if rectballe[G].y < 0 or rectballe[G].y > (rectFond1.size[1] - (rectballe1.size[1])) :     
                        Py[G]=-Py[G]

                    #permet le déplacement des balles
                    rectballe[G].y = rectballe[G].y + Py[G]
                    rectballe[G].x = rectballe[G].x + Px[G]

            if perso1 == 1 : #permet de faire clignoté le perso en cas d'immunité
                fenetre.blit(game.perso1.image, game.perso1.rect)

            fenetre.blit(imagePause, rectPause)
            fenetre.blit(imageTextVie, rectTextVie)    
            fenetre.blit(imageVie, rectVie)
            fenetre.blit(imageScore, rectScore)            
            fenetre.blit(imageScore2, rectScore2)

          #  para = para + 1
          #  if para == 3 :
              #  fenetre.blit(imagePluie1, rectPluie1)
          #  if para == 7 :   
              #  fenetre.blit(imagePluie2, rectPluie2)
           # if para == 8 :
               ## para = 0  

           # print(para)
            # rafraichissement
            pygame.display.flip()


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:     
                    continuer = 4	   
                if event.type == pygame.MOUSEMOTION:
                    A=event.pos

                #permet de mettre pause 
                if event.type == pygame.MOUSEBUTTONUP :
                    if event.button == 1 and  rectPause.collidepoint(A[0],A[1]) :
                        pygame.mixer.pause()
                        continuer = 5

        #boucle de pause
        while continuer == 5 :
            #réglage de la boucle à 30 tours par seconde
            horloge.tick(30)

            seconde=int(compteur/30)
            Score ="Score : " +str(seconde)
            imageScore = fontScore.render(Score, True, (255, 255, 15))

            fenetre.blit(imageFond2, rectFond2)
            fenetre.blit(imagePerso, rectPerso)
            fenetre.blit(imageBonus1, rectBonus1)
            fenetre.blit(imageScore, rectScore)
            fenetre.blit(imageScore2, rectScore2) 
            fenetre.blit(imageballe1, rectballe1)
            fenetre.blit(imagePlayB, rectPlayB)
            if nbBalle >= 0 :
                for G in range(nbBalle):
                    fenetre.blit(imageballe[G], rectballe[G])

            pygame.display.flip()

            for event in pygame.event.get():   # parcours de la liste des evenements recus
                if event.type == pygame.QUIT:     #Si un de ces evenements est de type QUIT
                    continuer = 4	   # On arrete la boucle
                if event.type == pygame.MOUSEMOTION:
                    A=event.pos
                
                #permet de retiré sur pause
                if event.type == pygame.MOUSEBUTTONUP :
                    if event.button == 1 and  rectPlayB.collidepoint(A[0],A[1]) :
                        pygame.mixer.unpause()
                        continuer = 2


    #permet de modifier le meilleur score
    if seconde > int(bestScore) :
        bestScore = seconde
        mscore = open("sauv.txt", "w")    
        mscore.write(str(bestScore))
        mscore.close()

    fontScore2 = pygame.font.Font(None, 34)
    imageScore2 = fontScore2.render("BestScore : "+str(bestScore), True, (255, 0, 0))

    # creation d'un rectangle pour positioner l'image du texte
    rectScore2 = imageScore2.get_rect()
    rectScore2.x = rectFond1.size[0]-190
    rectScore2.y = rectFond1.size[1]-55
    son2.stop()
    son3.play(20,0,50000)
    #permet d'afficher la fin de la parite
    while continuer == 3 :
        
        #réglage de la boucle à 30 tours par seconde
        horloge.tick(30)

        # Affichage du fond
        fenetre.blit(imageScore2, rectScore2) 
        fenetre.blit(imageFond3, rectFond3)
        fenetre.blit(imageScore, rectScore) 
        fenetre.blit(imageScore2, rectScore2) 
        fenetre.blit(imageRestar, rectRestar)

        pygame.display.flip()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:     
                continuer = 4
            if event.type == pygame.MOUSEMOTION:
                A=event.pos

            #permet de recommencer le jeu
            if event.type == pygame.MOUSEBUTTONUP :
                if event.button == 1 and  rectRestar.collidepoint(A[0],A[1]) :
                    son2.play(20,0,150000)
                    son3.stop()
                    continuer = 2
# fin du programme principal...
pygame.quit()
