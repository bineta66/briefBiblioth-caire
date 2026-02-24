from doc import Document
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
