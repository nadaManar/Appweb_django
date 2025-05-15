# Projet de gestion de catalogue de formations

Ce projet consiste à développer une application Django pour gérer le catalogue des formations d'un département universitaire.

---


## Questions et consignes du projet

### Question 1  
- Créer un projet Django intitulé **ct** et une application intitulée **uo**.  
- Ajouter l’application au fichier de configuration du projet Django.  
- Créer un fichier README.md listant les membres du groupe (prénoms, noms, emails).  
- Étiqueter le dépôt avec le tag `question1`.  
- Indiquer dans ce README les commandes Django utilisées.  

---

### Question 2  
- Créer une vue et un template pour afficher, à l’URL `/about/`, une page de présentation de l’application.

---

### Question 3  
- Rendre l’application d’administration Django accessible à l’URL `/admin`.  
- Permettre la gestion des modèles par l’administrateur.

---

### Question 4  
- Ajouter comme utilisateurs les enseignants du module Framework Web 1.  
- Générer un fichier `enseignant.json` dans le répertoire adéquat pour charger ces utilisateurs


---

### Question 5  
- Créer un modèle **Formation** avec les attributs :  
- `intitule` (chaîne, max 100 caractères),  
- `description` (texte),  
- un unique responsable (utilisateur), pouvant être indéterminé.  
- Un utilisateur ne peut pas être responsable de plusieurs formations.

---

### Question 6  
- Ajouter quatre formations réalistes :  
- Licence Informatique — Parcours Ingénierie informatique,  
- Licence Informatique — Parcours MIAGE,  
- Master Informatique,  
- Master MIAGE.  
- Générer un fichier `formation.json` pour charger ces données

 
---

### Question 7  
- Créer un modèle **UE** avec :  
- `titre` (chaîne, max 100 caractères),  
- `description` (texte),  
- trois attributs numériques :  
  - `CM` (heures de cours),  
  - `TD` (travaux dirigés),  
  - `TP` (travaux pratiques),  
- `credits` (nombre d’ECTS).  
- UE rattachée à une ou plusieurs formations.  
- UE avec un ou plusieurs responsables (utilisateurs).  
- Aucun champ ne peut être null.

---

### Question 8  
- Ajouter au moins 12 UE réalistes, rattachées à différentes formations, avec responsables définis pour certaines.  
- Générer un fichier `ue.json` pour charger ces données :  


---

### Question 9  
- Créer une vue et un template pour afficher une formation à l’URL `/formation/n` (n = id unique).  
- Afficher la liste des titres des UE rattachées, avec lien vers leur fiche détaillée.

---

### Question 10  
- Créer une vue et un template pour afficher une UE à l’URL `/ue/m` (m = id unique).  
- Afficher la liste des formations auxquelles l’UE est rattachée, avec lien vers leur fiche détaillée.

---

### Question 11  
- Créer une vue et un template pour afficher la liste des formations, avec lien vers la fiche détaillée.

---

### Question 12  
- Créer une vue et un template pour afficher la liste de toutes les UE, avec lien vers la fiche détaillée.

---

### Question 13  
- Créer une vue et un template pour permettre l’ajout d’une UE.  
- URL d’accès : `/ue/ajouter`.

---

### Question 14  
- Créer un template pour la page principale et un menu, utilisés dans tous les templates par héritage.  
- URL racine : `/`.

---

### Question 15  
- Créer une vue et un template pour modifier une UE existante.  
- URL d’accès : `/ue/modifier/m`.  
- Ajouter les accès depuis les templates pertinents.

---

### Question 16  
- Créer une vue et un template pour supprimer une UE existante.  
- URL d’accès : `/ue/supprimer/m`.  
- Ajouter les accès depuis les templates pertinents.

---

### Question 17  
- Améliorer l’esthétique de tous les templates avec Bootstrap 1.

---

### Question 18  
- Ajouter l’authentification à l’application.  
- Permettre de se connecter et se déconnecter via le menu.

---

### Question 19  
- Ajouter la gestion des autorisations :  
- Un utilisateur non authentifié ne peut que consulter le site,  
- Un responsable de formation peut ajouter, modifier, supprimer toutes les UE rattachées à sa formation,  
- Un responsable d’UE peut modifier ses UE, mais pas ajouter ou supprimer.

---

### Question 20  
- Ajouter une page accessible uniquement aux responsables de formation affichant, pour une formation donnée :  
- Nombre d’UE rattachées,  
- Liste des responsables d’UE triée par ordre alphabétique,  
- Volume total de CM, TD, TP,  
- Volume total en heures équivalent TD (1h CM = 1.5h TD, 1h TD ou TP = 1h),  
- Nombre total d’ECTS.

---

## Commandes Django courantes utilisées

```bash
django-admin startproject ct
python manage.py startapp uo
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata <fichier>.json


