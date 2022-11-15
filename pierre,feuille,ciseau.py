from random import randint

#DEBUT 
#On admet une fonction random qui retourne un chiffre aléatoire entre 0 et 2
#On admet une fonction input qui recupere le saisi d'un joueur lors de son execution
#On définit une fonction PierreFeuilleCiseau qui ne prend pas d'argument
def pierreFeuilleCiseau():
    #On assigne a nombreDePartiePourGagner le retour de l'execution de la fonction input
    nombreDePartiePourGagner = int(input("combien de manche pour gagner ? : "))
    #On initialise la variable scoreOrdinateur à 0
    scoreOrdinateur = 0
    #On initialise la variable scoreJoueur à 0
    scoreJoueur = 0
    #Tant que scoreOrdinateur OU scoreJoueur est différent de nombrePartiePourGagner
    while scoreOrdinateur != nombreDePartiePourGagner and scoreJoueur != nombreDePartiePourGagner:
        #Alors on assigne a choixOrdinateur le retour de l'execution de la fonction random
        choixOrdinateur = randint(0,2)
        #Alors on assigne a choixJoueur le retour de l'execution de la fonction input (avec la question "feuille, pierre ou ciseau ?")
        choixJoueur = input("pierre feuille ou ciseau ? : ")
        #Si le retour de l'execution de la fonction input est "pierre" ou "caillou"
        if choixJoueur == "pierre" or choixJoueur == "caillou":
            #Alors la variable choixJoueur prend la valeur 0
            choixJoueur = 0
        #OU SINON le retour de l'execution de la fonction input est "feuille" ou "papier"
        elif choixJoueur == "feuille" or choixJoueur == "papier":
            #Alors la variable choixJoueur prend la valeur 1
            choixJoueur = 1
        #OU SINON le retour de l'execution de la fonction input est "ciseau"
        elif choixJoueur == "ciseau" or choixJoueur == "ciseaux":
            #Alors la variable choixJoueur prend la valeur 2
            choixJoueur = 2
        #Si la valeur de choixOrdinateur est différente de valeur de choixJoueur
        if choixOrdinateur != choixJoueur:
            #Si choixOrdinateur est égal à 0
            if choixOrdinateur == 0:
                #Si choixJoueur est égal à 1
                if choixJoueur == 1:
                    #Alors incrementer de 1 scoreJoueur
                    scoreJoueur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué pierre, vous gagnez la manche !")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
                #Si choixJoueur est égal à 2
                if choixJoueur == 2:
                    #Alors incrementer de 1 scoreOrdinateur
                    scoreOrdinateur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué pierre, vous perdez la manche :/")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
            #Si choixOrdinateur est égal à 1
            if choixOrdinateur == 1:
                #Si choixJoueur est égal à 0
                if choixJoueur == 0:
                    #Alors incrementer de 1 scoreOrdinateur
                    scoreOrdinateur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué feuille, vous perdez la manche :/")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
                #Si choixJoueur est égal à 2
                if choixJoueur == 2:
                    #Alors incrementer de 1 scoreJoueur
                    scoreJoueur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué feuille, vous gagnez la manche !")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
            #Si choixOrdinateur est égal à 2 
            if choixOrdinateur == 2:
                #Si choixJoueur est égal à 0
                if choixJoueur == 0:
                    #Alors incrementer de 1 scoreJoueur
                    scoreJoueur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué ciseau, vous gagnez la manche !")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
                #Si choixJoueur est égal à 1
                if choixJoueur == 1:
                    #Alors incrementer de 1 scoreOrdinateur
                    scoreOrdinateur += 1
                    #on affiche le resulat de la manche
                    print("L'Ordinateur a joué ciseau, vous perdez la manche :/")
                    #on affiche le score actuel
                    print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
        #Sinon
        else:
            #On affche un message d'égalité de manche
            print("Egalité...joue mieux")
            #on affiche le score actuel
            print("Ordinateur",scoreOrdinateur,"; Vous",scoreJoueur)
    #Si scoreOrdinateur est égal nombrePartiePourGagner      
    if scoreOrdinateur == nombreDePartiePourGagner:
        #Alors on afficher un message de défaite avec les scores
        print("Tu as perdu, contre un BOT, vraiment ???",scoreOrdinateur,"à",scoreJoueur,"en plus...")
    #Sinon
    else:
        #Alors on affiche un message de victoire avec les scores
        print("Tu as gagné, ouais... c'est juste de la chance.",scoreJoueur,"à",scoreOrdinateur,"mouais")
#On execute la fonction PierreFeuilleCiseau avec un entier choisi en input par le joueur
pierreFeuilleCiseau()
#FIN
