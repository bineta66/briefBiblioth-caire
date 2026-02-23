from abc import ABC, abstractmethod


class Document(ABC):

    def __init__(self, titre):
        self.titre = titre
        self.__disponible = True  


    @property
    def disponible(self):
        return self.__disponible

    def changeEtat (self, disponible):
        self.__disponible = disponible

    @abstractmethod
    def emprunter(self):
        pass

    @abstractmethod
    def retourner(self):
        pass


class Livre(Document):

    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

    def emprunter(self):
        if not self.disponible:
            raise Exception(" Ce livre est déjà emprunté.")
        self.changeEtat(False)
        print("Livre emprunté.")

    def retourner(self):
        if self.disponible:
            raise Exception(" Ce livre est déjà disponible.")
        self.changeEtat(True)
        print(" Livre retourné.")

    def __str__(self):
        return f"Livre | {self.titre} |  de {self.auteur} | Disponible : {self.disponible}"


class Magazine(Document):

    def __init__(self, titre, numero):
        super().__init__(titre)
        self.numero = numero

    def emprunter(self):
        if not self.disponible:
            raise Exception("Ce magazine est déjà emprunté.")
        self.changeEtat(False)
        print(" Magazine emprunté.")

    def retourner(self):
        if self.disponible:
            raise Exception(" Ce magazine est déjà disponible.")
        self.changeEtat == True
        self.changeEtat(True)
        print(" Magazine retourné.")

    def __str__(self):
        return f"Magazine | {self.titre} | N°{self.numero} | Disponible : {self.disponible}"




class Bibliothecaire:

    def __init__(self):
        self.catalogue = []

    def ajouter_document(self, document):
        self.catalogue.append(document)

    def rechercher_par_titre(self, titre):
        for doc in self.catalogue:
            if doc.titre == titre:
                return doc
        return None

    def afficher_catalogue(self):
        if not self.catalogue:
            print(" Catalogue vide.")
            return

        for doc in self.catalogue:
            print(doc)



class Menu:

    def __init__(self):
        self.biblio = Bibliothecaire()

    def saisir_texte(self, message):
        while True:
            valeur = input(message).strip()
            if valeur == "" or  not valeur.isalpha():
                print("Champ obligatoire et des lettre.")
            else:
                return valeur

    def saisir_numero(self, message):
        while True:
            valeur = input(message).strip()
            if valeur.isdigit():
                return int(valeur)
            else:
                print("Veuillez entrer un nombre valide.")

    def menu(self):
        print("\n---------- MENU -----------")
        print("1. Ajouter un Livre")
        print("2. Ajouter un Magazine")
        print("3. Emprunter un document")
        print("4. Retourner un document")
        print("5. Afficher le catalogue")
        print("6. Quitter")

    def lancer(self):
        while True:
            self.menu()
            choix = input("Choix : ").strip()

            if choix == "1":
                titre = self.saisir_texte("Titre du livre : ")
                auteur = self.saisir_texte("Auteur : ")
                self.biblio.ajouter_document(Livre(titre, auteur))
                print("Livre ajouté avec succès.")

            elif choix == "2":
                titre = self.saisir_texte("Titre du magazine : ")
                numero = self.saisir_numero("Numéro : ")
                self.biblio.ajouter_document(Magazine(titre, numero))
                print("Magazine ajouté avec succès.")

            elif choix == "3":
                titre = self.saisir_texte("Titre du document : ")
                doc = self.biblio.rechercher_par_titre(titre)

                if doc:
                    try:
                        doc.emprunter()
                    except Exception as e:
                        print(e)
                else:
                    print("Document introuvable.")

            elif choix == "4":
                titre = self.saisir_texte("Titre du document : ")
                doc = self.biblio.rechercher_par_titre(titre)

                if doc:
                    try:
                        doc.retourner()
                    except Exception as e:
                        print(e)
                else:
                    print("Document introuvable.")

            elif choix == "5":
                self.biblio.afficher_catalogue()

            elif choix == "6":
                print("Au revoir.")
                break

            else:
                print("Choix invalide.")
  



if __name__ == "__main__":
    menu = Menu()
    menu.lancer()