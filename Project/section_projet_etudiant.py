class Section:
    def __init__(self, numSection, nomSection):
        self.__numSection = numSection
        self.__nomSection = nomSection

    def getNumSection(self):
        return self.__numSection

    def getNomSection(self):
        return self.__nomSection

    # setters

class Projet:
    def __init__(self, numProjet, theme):
        self.__numProjet = numProjet
        self.__theme = theme

    def getNumProjet(self):
        return self.__numProjet

    def getTheme(self):
        return self.__theme

    # setters

class Etudiant:
    def __init__(self, numEtudiant, nom, prenom, section, projet):
        self.__numEtudiant = numEtudiant
        self.__nom = nom
        self.__prenom = prenom
        self.__section = section
        self.__projet = projet

    def getNumEtudiant(self):
        return self.__numEtudiant

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getSection(self):
        return self.__section

    def getProjet(self):
        return self.__projet

    # setters

def main():
    liste_section = []
    liste_projet = []
    liste = []
    choix = 0
    while choix == 0:
        print("1. Creer une section")
        print("2. Creer un projet")
        print("3. Creer un etudiant")
        print("4. Lister les sections")
        print("5. Lister les projets")
        print("6. Lister les etudiants")
        print("7. Afficher les etudiants d'une section donnee")
        print("8. Afficher les etudiants qui y travaillent dans un projet donnee ")
        print("9. Afficher pour un projet donnee les etudiants qui y travaillent et leurs projets repectifs")
        print("10. Sortie")
        choix = int(input("Votre choix ? "))
        if choix == 1:
            choix = 0
            numSection = int(input("Numero section? "))
            nomSection = input("Nom section? ")
            section = Section(numSection, nomSection)
            liste_section.append(section)
        else:
            if choix == 2:
                choix = 0
                numProjet = int(input("Numero projet? "))
                theme = input("Theme? ")
                projet = Projet(numProjet, theme)
                liste_projet.append(projet)
            else:
                if choix == 3:
                    choix = 0
                    section = None
                    projet = None
                    numEtudiant = int(input("Numero etudiant? "))
                    nom = input("Nom? ")
                    prenom = input("Prenom? ")

                    while section == None:
                        numSection = int(input("Numero section de l'etudiant? "))
                        for i in range(len(liste_section)):
                            if liste_section[i].getNumSection() == numSection:
                                section = liste_section[i]
                                break
                        if section == None:
                            print("--- Numero inexistant !!! ---")

                    while projet == None:
                        numProjet = int(input("Numero projet de l'etudiant? "))
                        for i in range(len(liste_projet)):
                            if liste_projet[i].getNumProjet() == numProjet:
                                projet = liste_projet[i]
                                break
                        if projet == None:
                            print("--- Numero inexistant !!! ---")
                    etudiant = Etudiant(numEtudiant, nom, prenom, section, projet)
                    liste.append(etudiant)
                else:
                    if choix == 4:
                        choix = 0
                        for i in range(len(liste_section)):
                            print("________________________________________")
                            print("Numero section: ", liste_section[i].getNumSection())
                            print("Nom section: ", liste_section[i].getNomSection())
                            print()
                        print("________________________________________")
                    else:
                        if choix == 5:
                            choix = 0
                            for i in range(len(liste_projet)):
                                print("________________________________________")
                                print("Numero projet: ", liste_projet[i].getNumProjet())
                                print("Theme: ", liste_projet[i].getTheme())
                                print()
                            print("________________________________________")
                        else:
                            if choix == 6:
                                choix = 0
                                for i in range(len(liste)):
                                    print("________________________________________")
                                    print("Numero etudiant: ", liste[i].getNumEtudiant())
                                    print("Nom: ", liste[i].getNom())
                                    print("Prenom: ", liste[i].getPrenom())
                                    print("- Section-")
                                    print("Numero section: ", liste[i].getSection().getNumSection())
                                    print("Nom section: ", liste[i].getSection().getNomSection())
                                    print("- Projet -")
                                    print("Numero projet: ", liste[i].getProjet().getNumProjet())
                                    print("Theme: ", liste[i].getProjet().getTheme())
                                    print()
                                print("________________________________________")
                            else:
                                if choix == 7:
                                    choix = 0
                                    bad = True
                                    numSection = 0
                                    while bad:
                                        numSection = int(input("Numero section de l'etudiant? "))
                                        for i in range(len(liste_section)):
                                            if liste_section[i].getNumSection() == numSection:
                                                bad = False
                                                break
                                        if bad:
                                            print("--- Numero inexistant !!! ---")
                                    for i in range(len(liste)):
                                        if numSection == liste[i].getSection().getNumSection():
                                            print("________________________________________")
                                            print("Numero etudiant: ", liste[i].getNumEtudiant())
                                            print("Nom: ", liste[i].getNom())
                                            print("Prenom: ", liste[i].getPrenom())
                                            print()
                                    print("________________________________________")
                                else:
                                    if choix == 8:
                                        choix = 0
                                        bad = True
                                        numProjet = 0
                                        while bad:
                                            numProjet = int(input("Numero du projet de l'etudiant? "))
                                            for i in range(len(liste_projet)):
                                                if liste_projet[i].getNumProjet() == numProjet:
                                                    bad = False
                                                    break
                                            if bad:
                                                print("--- Numero inexistant !!! ---")
                                        for i in range(len(liste)):
                                            if numProjet == liste[i].getProjet().getNumProjet():
                                                print("________________________________________")
                                                print("Numero etudiant: ", liste[i].getNumEtudiant())
                                                print("Nom: ", liste[i].getNom())
                                                print("Prenom: ", liste[i].getPrenom())
                                                print()
                                        print("________________________________________")
                                    else:
                                        if choix == 9:
                                            choix = 0
                                            for i in range(len(liste_projet):
                                                print("________________________________________")
                                                print("- Projet -")
                                                print("Numero projet: ", liste_projet[i].getNumProjet())
                                                print("Theme: ", liste_projet[i].getTheme())
                                                for j in range(len(liste)):
                                                    if liste_projet[i].getNumProjet() == liste[j].getProjet().getNumProjet():
                                                        print("Numero etudiant: ", liste[j].getNumEtudiant())
                                                        print("Nom: ", liste[j].getNom())
                                                        print("Prenom: ", liste[j].getPrenom())
                                                        print("- Section -")
                                                        print("Numero section: ", liste[j].getSection().getNumSection())
                                                        print("Nom section: ", liste[j].getSection().getNomSection())
                                                        print()
                                            print("________________________________________")
    print("----------- Fin du programme -----------")

main()
