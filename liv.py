from doc import Document
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
