from module_plateau import plateau


p = plateau()

if __name__ == '__main__':
     
    
    
    choix = input("Voulez-vous commencer une nouvelle partie ou charger une partie existante? (n/c): ")
    
    if choix == 'c':
        nom_fichier = input('Entrez le nom du fichier (Penser à préciser le type de fichier) : ')
        p.charger_partie(nom_fichier)
        
    elif choix == 'n':
        jeu = input("Souhaitez vous jouer contre une IA ou avec 2 joueurs ? (b/j) : ")
        
        if jeu == "b" :
            p.jouer_puissance4_vs_IA()
          
        elif jeu == "j" :
            
            p.jouer_puissance4_vs_Joueur()
            
        
            

            
    
        
        
    