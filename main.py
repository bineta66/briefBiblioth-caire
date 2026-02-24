from biblio import Bibliothecaire
from liv import Livre
from mag import Magazine
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