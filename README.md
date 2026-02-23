README — Système de Gestion de Bibliothèque en Python
1. Présentation du projet

Ce projet est une application console développée en Python permettant de gérer une bibliothèque.

L’utilisateur peut :

Ajouter un livre

Ajouter un magazine

Emprunter un document

Retourner un document

Afficher le catalogue

Ce projet met en pratique les concepts de la Programmation Orientée Objet (POO).

2. Objectifs pédagogiques

Ce projet permet de comprendre :

Les classes et objets

L’héritage

Le polymorphisme

Les classes abstraites

L’encapsulation

Les propriétés (@property)

La gestion des exceptions

La gestion des menus interactifs

3. Structure du projet

Le programme est composé de plusieurs classes :

Document (classe abstraite)

Livre
Magazine
Bibliothecaire
Menu
4. Explication des classes
4.1 Classe Document

C’est une classe abstraite.

Elle définit les éléments communs à tous les documents :

titre

disponible

emprunter() (méthode abstraite)

retourner() (méthode abstraite)

On ne peut pas créer un objet Document directement.

Elle sert de modèle.

4.2 Classe Livre

Hérite de Document.

Attributs supplémentaires :

auteur

Méthodes :

emprunter()

retourner()

__str__() pour afficher les informations du livre

4.3 Classe Magazine

Hérite aussi de Document.

Attribut supplémentaire :

numero

Même fonctionnement que Livre.

4.4 Classe Bibliothecaire

Cette classe gère :

Une liste appelée catalogue

L’ajout de documents

La recherche par titre

L’affichage du catalogue

4.5 Classe Menu

Gère :

L’affichage du menu

Les interactions utilisateur

La gestion des choix

La validation des saisies

5. Notions importantes utilisées
Classe abstraite
from abc import ABC, abstractmethod

Empêche la création directe de Document.

Encapsulation

L’attribut :

self.__disponible

est privé.

On y accède via :

@property
Polymorphisme

Livre et Magazine ont les mêmes méthodes :

emprunter()
retourner()

Mais leur comportement est adapté.

6. Comment exécuter le programme
Installer Python (si nécessaire)

Vérifier :

python --version
Lancer le programme
python nom_du_fichier.py
7. Exemple d’utilisation
---------- MENU -----------
1. Ajouter un Livre
2. Ajouter un Magazine
3. Emprunter un document
4. Retourner un document
5. Afficher le catalogue
6. Quitter
8. Améliorations possibles

Ajouter une base de données MySQL

Ajouter un identifiant unique pour chaque document

Ajouter la suppression de document

Ajouter une interface graphique (Tkinter)

Ajouter une sauvegarde automatique

9. Personnalisation

Tu peux modifier :

Ajouter un nouveau type de document

Exemple :

class DVD(Document):

Il suffit d’implémenter :

emprunter()

retourner()

Modifier les messages

Changer les print() selon ton style.

Ajouter une recherche insensible à la casse

Modifier :

if doc.titre == titre:
10. Auteur

Nom : (Met ton nom ici)
Formation : Licence 3 Développement Web
Université : (Met ton université ici)
Année : 2026

 11. Ce que montre ce projet

Ce projet démontre :

Une bonne maîtrise de la POO

Une architecture extensible

Une gestion propre des interactions

Une séparation des responsabilités

Conclusion

Ce système de gestion de bibliothèque est un projet pédagogique permettant de comprendre les bases solides de la programmation orientée objet en Python.

Il peut évoluer vers une application professionnelle avec base de données et interface graphique.
