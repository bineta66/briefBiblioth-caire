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