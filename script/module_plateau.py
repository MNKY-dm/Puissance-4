import random
from copy import deepcopy
import csv

class plateau():
    
    # Fonction pour initialiser la grille de jeu et l'historique des grille vide
    def __init__(self):
        
        self.grille = [
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
                      ]
        
        self.historique_grille = []      
        
    # Fonction pour afficher la grille
    def affiche(self):
        
        sephiroth = "+---+---+---+---+---+---+---+" #Cases de la grille
        print(sephiroth)
        
        #Parcourt chaque élément de la grille afin de l'afficher
        for l in range(len(self.grille )) : 
            print('|', end = '')
            
            for c in range(len(self.grille[l])) :
                if self.grille[l][c] == 0 :
                    print('   ', end = '|')
                elif self.grille[l][c] == 1 :
                    print(' X ', end = '|')
                elif self.grille[l][c] == 2 :
                    print(' O ', end = '|')
                    
            print()
            print(sephiroth)
                              
        
    # Fonction pour placer un jeton dans la colonne choisie
    def jeton(self, nJoueur):
        global jetonJ
        #Demande au joueur de placer un jeton dans une colonne choisie (-1 sert à sélctionner une colonne réel de la grille)
        jetonJ = int(input("Joueur choisissez une colonne du tableau : "))-1
        
        if jetonJ == -1: #Si le joueur veut retourner en arrière
            return 0 #Pour pouvoir quitter la fonction
            
            
        elif jetonJ == 99: #Si le joueur veut sauvegarder la partie
            return 0 #Pour pouvoir quitter la fonction
       
            
        while jetonJ > len(self.grille[0])-1 or jetonJ < 0 : #Si la colonne choisie n'est pas dans la grille recommencer
            jetonJ = int(input("La colonne choisie n'existe pas. Veuillez choisir une autre une colonne du tableau: "))-1    
        
        while self.grille[0][jetonJ]!= 0 : #Si la colonne choisie est pleine recommencer
            jetonJ = int(input("La colonne choisie est pleine. Veuillez en choisir une autre : "))-1
        
         
        #Ajoute le jeton dans la colonne choisie 
        for l in range(len(self.grille)):
            
            if self.grille[l][jetonJ] != 0: # S'il y a déjà un pion de placé dans la colonne 
                self.grille[l-1][jetonJ] = nJoueur # Alors on place le pion au dessus de celui-ci
                break
            
            elif l == 5 : #S'il n'y a pas de pion dans la colonne 
                self.grille[l][jetonJ] = nJoueur # Alors on place le pion dans la case du bas
                    
        return jetonJ
                
# =============================================================================
# Fonction qui choisit un coup (aléatoire) fait par l'IA
# =============================================================================
    def IA_random(self):
        
            
        jetonIA = random.randint(0, 6)
        print("L'IA a choisi la", jetonIA + 1, "ème colonne")

        for l in range(len(self.grille)):
            if self.grille[l][jetonIA] != 0: # S'il y a déjà un pion de placé dans la colonne 
                self.grille[l-1][jetonIA] = 2 # Alors on place le pion au dessus de celui-ci
                break
            elif l == 5 : # S'il n'y a pas de pion dans la colonne 
                self.grille[l][jetonIA] = 2
        
        
                    
    
    
# ================================================================================
# Fonction qui teste si le joueur peut gagner et pose un jeton pour l'empêcher de
# gagner    
# ================================================================================
    def IA_defensive(self): 
        alignement = False
        for c in range(len(self.grille[0])):
            for l in range(len(self.grille)):
                
                if l == 0 and self.grille[l][c] != 0:
                    break
                
                
                elif l == 5 and self.grille[l][c] == 0: # S'il n'y a pas de pion dans la colonne
                    
                    self.grille[l][c] = 1  # on pose le jeton en bas de la colonne pour tester si le joueur peut gagner
                    if self.parcours(self.grille, 1) == 4:  # Si le counter passe à 4, le joueur peut gagner
                        self.grille[l][c] = 2
                        alignement = True
                        return
                           # on laisse le jeton là où il a été posé
                    else:    # sinon
                        self.grille[l][c] = 0   # on le retire
                        break  # on passe à la colonne d'après


                elif self.grille[l][c] != 0: # S'il y a déjà un pion de placé dans la colonne

                    self.grille[l-1][c] = 1 # Alors on place le pion au dessus de celui-ci
                    
                    if self.parcours(self.grille, 1) == 4:  # Si le counter passe à 4, le joueur peut gagner
                        self.grille[l-1][c] = 2
                        alignement = True
                        return   # on laisse le jeton là où il a été posé
                    
                    else:    # sinon
                        self.grille[l-1][c] = 0   # on le retire
                        break  # on passe à la colonne d'après   
        if alignement == False:
            global défaite
            global défaite1
            
            défaite = False
            défaite1 = False
            return False

# ================================================================================
# Fonction qui teste si le bot peut gagner et pose un jeton pour lui permettre de
# gagner    
# ================================================================================
            
    def IA_offensive(self):  
        alignement = False
        for c in range(len(self.grille[0])):
            for l in range(len(self.grille)):
                
                if l == 0 and self.grille[l][c] != 0:
                    break

                
                if l == 5 and self.grille[l][c] == 0: # S'il n'y a pas de pion dans la colonne
                    self.grille[l][c] = 2  # on pose le jeton en bas de la colonne pour tester si le bot peut gagner
                    if self.parcours(self.grille, 2) == 4:  # Si le counter passe à 4, le bot peut gagner
                        self.grille[l][c] = 2
                        alignement = True 
                        return
                           # on laisse le jeton là où il a été posé
                    else:    # sinon
                        self.grille[l][c] = 0   # on le retire
                        break  # on passe à la colonne d'après


                elif self.grille[l][c] != 0: # S'il y a déjà un pion de placé dans la colonne

                    self.grille[l-1][c] = 2 # Alors on place le pion au dessus de celui-ci
                    
                    if self.parcours(self.grille, 2) == 4:  # Si le counter passe à 4, le bot peut gagner
                        self.grille[l-1][c] = 2
                        alignement = True
                        return   # on laisse le jeton là où il a été posé
                    
                    else:    # sinon
                        self.grille[l-1][c] = 0   # on le retire
                        break  # on passe à la colonne d'après   
        if alignement == False:
            global victoire
            victoire = False
            return False         
        
        
        
    # Fonction pour vérifier s’il y a un gagnant
    def parcours(self, t, nJoueur):
        
        
        
        
        counter = 0     # variable qui compte le nombre de jetons alignés horizontalement
        counterMax = 0  # variable qui enregistre la valeur la plus haute atteinte par counter
        
        for l in range(len(t)):
            counter = 0     # réinitialise le compteur lors du passage à une autre ligne
            for c in range(len(t[l])):
                if t[l][c] == nJoueur:
                    counter+=1
                    if counter > counterMax:
                        counterMax = counter
                else :
                    counter = 0


    # =============================================================================
    # Vérifie la victoire de manière verticale 
    # =============================================================================
                    
        # décompte réinitialisé        
        counter = 0  
        
        # Répertorie toutes les verticales à vérifier
        verticales = [
                [t[0][0], t[1][0], t[2][0], t[3][0], t[4][0], t[5][0]],
                [t[0][1], t[1][1], t[2][1], t[3][1], t[4][1], t[5][1]],
                [t[0][2], t[1][2], t[2][2], t[3][2], t[4][2], t[5][2]],
                [t[0][3], t[1][3], t[2][3], t[3][3], t[4][3], t[5][3]],
                [t[0][4], t[1][4], t[2][4], t[3][4], t[4][4], t[5][4]],
                [t[0][5], t[1][5], t[2][5], t[3][5], t[4][5], t[5][5]],
                [t[0][6], t[1][6], t[2][6], t[3][6], t[4][6], t[5][6]]
                     ]
        

        for l in range(len(verticales)):
            counter = 0
            for c in range(len(verticales[l])):
                if verticales[l][c] == nJoueur:
                    counter += 1
                    if counter > counterMax:
                        counterMax = counter
                else:
                    counter = 0



    # =============================================================================
    # Vérifient la victoire de manière diagonale 
    # =============================================================================
        

        # décompte réinitialisé
        counter = 0  
        
        # Répertorie toutes les diagonales en partant du haut gauche à vérifier
        diagonalesHaut = [
               [t[0][0], t[1][1], t[2][2], t[3][3], t[4][4], t[5][5]], 
               [t[0][1], t[1][2], t[2][3], t[3][4], t[4][5], t[5][6]],
               [t[0][2], t[1][3], t[2][4], t[3][5], t[4][6]],
               [t[0][3], t[1][4], t[2][5], t[3][6]],
               [t[1][0], t[2][1], t[3][2], t[4][3], t[5][4]],
               [t[2][0], t[3][1], t[4][2], t[5][3]]
                         ]
        
        
        for l in range(len(diagonalesHaut)):
            counter = 0
            for c in range(len(diagonalesHaut[l])):
                if diagonalesHaut[l][c] == nJoueur:
                    counter += 1
                    if counter > counterMax:
                        counterMax = counter
                else:
                    counter = 0


        # décompte réinitialisé
        counter = 0  
        
        # Répertorie toutes les diagonales en partant du bas gauche à vérifier
        diagonalesBas = [
               [t[3][0], t[2][1], t[1][2], t[3][0]],
               [t[4][0], t[3][1], t[2][2], t[1][3], t[0][4]], 
               [t[5][0], t[4][1], t[3][2], t[2][3], t[1][4], t[0][5]],
               [t[5][1], t[4][2], t[3][3], t[2][4], t[1][5], t[0][6]],
               [t[5][2], t[4][3], t[3][4], t[2][5], t[1][6]],
               [t[5][3], t[4][4], t[3][5], t[2][6]]
                        ]
        

        for l in range(len(diagonalesBas)):
            counter = 0
            for c in range(len(diagonalesBas[l])):
                if diagonalesBas[l][c] == nJoueur:
                    counter += 1
                    if counter > counterMax:
                        counterMax = counter
                else:
                    counter = 0
        return counterMax
        

                
             
                    
    #Fonction qui permet de faire une copie de la grille actuelle
    def copy(self):
        
        
        copy_grille = deepcopy(self.grille) #Copie la grille 
        return copy_grille
    
        """
        return [[self.grille[j][i] for i in range(len(self.grille[0]))] for j in range(len(self.grille))] #Renvoie la copie de la grille
        """

    #Fonction qui permet d'ajouter la copie de la grille dans un historique
    def historique(self):
          
        self.historique_grille.append(self.copy())
        return self.historique_grille
         

    def sauvegarder_partie(self):
        nom_fichier = input("Entrez le nom du fichier de sauvegarde : ")
        with open(nom_fichier + '.csv', 'w', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            for ligne in self.grille:
                writer.writerow(ligne)
        print("Partie sauvegardée avec succès.")
        

    def charger_partie(self, fichier):
        open(fichier, 'r')
        lines = fichier.readlines()
        for c in lines:
            c.split(',')
            
        
        fichier.close()
        self.affiche()
        
    #Fonction qui permet de jouer au puissance 4     
    def jouer_puissance4_vs_IA(self):
        
        diff = input("Choisissez la difficulté de l'IA (F/M/D/HARDCORE) : ")
        if diff == "F" :
            print("Vous avez choisi la difficulté Facile")
        
        if diff == "M" :
            print("Vous avez choisi la difficulté M")
        
        if diff == "D" :
            print("Vous avez choisi la difficulté D")
        
        if diff == "HARDCORE" :
            print("Vous avez choisi la difficulté HARDCORE")
        
        t = 0 #Nb de tour
    
        print('Vous pouvez jouer au puissance 4', end='')        
        print('Entrer la colonne "0" pour annuler votre dernier coup', end='')
        print('Entrer la colonne "100" pour sauvegarder votre partie')
        print("")
        
        self.affiche()
        
        
        
            
            
        while self.parcours(self.grille, 1) != 4 and self.parcours(self.grille, 2) != 4: #Tant qu'il n'y a pas de gagnant
            self.copy()
            self.historique()
            self.jeton(1)
            global jetonJ
            
            if self.parcours(self.grille, 1) == 4 :
                print("Bravo ! Tu as dominé l'ordi et gagné la partie!!!")
                return
            
            
            
            if jetonJ == -1: ##Si le joueur veut annulé le dernier tour 
                t -= 1 #Le nombre de tour diminue de 1
                if t < 0:
                    t = 0
                self.grille = self.historique_grille[t]
                self.historique_grille.pop()
                print("Vous avez annulé votre dernier coup")
                print("Vous restez au tour n°", t)   
                print('')
                
                print("Voici l'ancienne grille")
                self.affiche()
                 
                
            elif jetonJ == 99:  
                self.sauvegarder_partie() 
                return 0
                
            else:
                self.affiche()
                if diff == "F" :
                    self.IA_random()
                    
                elif diff == "M" :
                    if self.IA_defensive() == False: 
                        global défaite
                        if défaite == False : 
                            self.IA_random()
                                    
                elif diff == "D" :
                    if self.IA_offensive() == False:
                        global victoire
                        if victoire == False:
                            if self.IA_defensive() == False: 
                                global défaite1
                                if défaite1 == False : 
                                    self.IA_random()

                elif diff == "HARDCORE" :
                    print("Vous avez choisi la difficulté HARDCORE")
                    
                
                self.affiche()
                t += 1
                print("tour n°", t)
                
    
            if self.parcours(self.grille, 2) == 4 :
                print("Nulllll Germain !! Tu t'es fait battre par une IA qui joue aléatoirement")
        

        
        
    def jouer_puissance4_vs_Joueur(self,):
        
        t = 0 #Nb de tour
    
        print('Vous pouvez jouer au puissance 4', end='')        
        print('Entrer la colonne "0" pour annuler votre dernier coup', end='')
        print('Entrer la colonne "100" pour sauvegarder votre partie')
        print("")
        
        self.affiche()
    
        while self.parcours(self.grille, 1) != 4 and self.parcours(self.grille, 2) != 4: #Tant qu'il n'y a pas de gagnant
            self.copy()
            self.historique()
            self.jeton(1)
            global jetonJ
            
           
            
            if jetonJ == -1: ##Si le joueur veut annulé le dernier tour 
                t -= 1 #Le nombre de tour diminue de 1
                if t < 0:
                    t = 0
                self.grille = self.historique_grille[t]
                self.historique_grille.pop()
                print("Vous avez annulé votre dernier coup")
                print("Vous restez au tour n°", t)   
                print('')
                
                print("Voici l'ancienne grille")
                self.affiche()
                 
                
            elif jetonJ == 99:  
                self.sauvegarder_partie() 
                return 0
                
            elif self.parcours(self.grille, 1) == 4 :
                print("Bravo ! Tu as dominé le joueur n°2!!!")
                
                
            else:
                self.affiche()
                self.jeton(2)
                
                if jetonJ == -1: ##Si le joueur veut annulé le dernier tour 
                    t -= 1 #Le nombre de tour diminue de 1
                    if t < 0:
                        t = 0
                    self.grille = self.historique_grille[t]
                    self.historique_grille.pop()
                    print("Vous avez annulé votre dernier coup")
                    print("Vous restez au tour n°", t)   
                    print('')
                    
                    print("Voici l'ancienne grille")
                    self.affiche()
                    
                elif self.parcours(self.grille, 2) == 4 :
                    self.affiche()
                    print("Bravo ! Tu as dominé le joueur n°1!!!")
                    
                else : 
                    self.affiche()
                    t += 1
                    print("tour n°", t)
           
            
   
p = plateau()   
    
if __name__ == '__main__'  :               
    
    p.jouer_puissance4_vs_IA()  
    
    
