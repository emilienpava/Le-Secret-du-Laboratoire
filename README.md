# Le-Secret-du-LaboratoireLe Secret du Laboratoire 404

API REST développée avec Python, FastAPI et Pydantic pour gérer le backend d'un jeu d'escape game.

Présentation

Le Secret du Laboratoire 404 est un escape game sur le thème Science-fiction / Horreur.

Le joueur doit progresser à travers plusieurs salles, récupérer des objets, résoudre des énigmes et déverrouiller des portes afin de s'échapper du laboratoire.

Le maître du jeu est une intelligence artificielle appelée IA-NEXUS.

Technologies utilisées

Python

FastAPI

Pydantic

Uvicorn

Programmation orientée objet (POO)

SHA-256 pour les énigmes de type HashPuzzle

Swagger / OpenAPI pour tester l'API

Structure du projet

projetpython/
├── app/
│   ├── domain/
│   │   ├── game_element.py
│   │   ├── item.py
│   │   ├── door.py
│   │   ├── puzzle.py
│   │   ├── code_puzzle.py
│   │   ├── hash_puzzle.py
│   │   └── room.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── puzzle.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── player_game.py
│   │
│   ├── game_data.py
│   └── main.py
│
└── README.md

Rôle des principaux dossiers

domain/ : contient les classes métier et la logique du jeu.

schemas/ : contient les modèles Pydantic utilisés pour valider les données reçues par l'API.

routers/ : contient les différentes routes de l'API REST.

game_data.py : contient les salles, objets, portes et énigmes du jeu.

main.py : initialise l'application FastAPI et enregistre les routes.

Installation

1. Cloner le projet

git clone <URL_DU_REPOSITORY>
cd projetpython

2. Créer un environnement virtuel

python3 -m venv .venv

3. Activer l'environnement virtuel

Sous Linux / macOS :

source .venv/bin/activate

Sous Windows :

.venv\Scripts\activate

4. Installer les dépendances

pip install fastapi uvicorn

Lancer l'API

Depuis la racine du projet :

uvicorn app.main:app --reload

L'API est alors disponible à l'adresse :

http://127.0.0.1:8000

Documentation Swagger

FastAPI génère automatiquement une documentation interactive.

Ouvrir :

http://127.0.0.1:8000/docs

Cette interface permet de tester directement toutes les routes de l'API.

La documentation OpenAPI est également disponible à :

http://127.0.0.1:8000/openapi.json

Routes de l'API

Vérifier l'état de l'API

GET /health

Retourne l'état de fonctionnement de l'API.

Exemple :

{
  "status": "online",
  "game_title": "Le Secret du Laboratoire 404",
  "engine_version": "1.0.0"
}

Récupérer toutes les salles

GET /rooms

Retourne la liste des salles du jeu.

Récupérer une salle

GET /rooms/{room_id}

Exemple :

GET /rooms/room1

Retourne les informations de la salle correspondant à l'identifiant fourni.

Si la salle n'existe pas, l'API retourne une erreur 404.

Soumettre une réponse à une énigme

POST /puzzles/submit

Exemple de requête :

{
  "puzzle_id": "puzzle1",
  "attempt_code": "1234",
  "player_id": "player1"
}

Si la réponse est correcte :

{
  "success": true,
  "message": "Porte déverrouillée !"
}

Si la réponse est incorrecte :

{
  "success": false,
  "message": "Mauvaise réponse."
}

Validation des données

Les données envoyées à POST /puzzles/submit sont validées avec Pydantic.

Le champ attempt_code ne peut pas être vide.

Une requête comme :

{
  "puzzle_id": "puzzle1",
  "attempt_code": "",
  "player_id": "player1"
}

est refusée par l'API avec le code HTTP :

422 Unprocessable Entity

Les énigmes

Le projet utilise une classe abstraite Puzzle dont héritent plusieurs types d'énigmes.

CodePuzzle

CodePuzzle compare directement la réponse du joueur avec un code secret.

Exemple :

Code attendu : 1234
Réponse : 1234
Résultat : réussite

HashPuzzle

HashPuzzle utilise l'algorithme SHA-256.

La réponse du joueur est transformée en hash puis comparée au hash enregistré dans le jeu.

Pour le puzzle puzzle2, la réponse correcte est :

NEXUS

Salles du jeu

Le jeu contient actuellement quatre salles :

Identifiant

Salle

Contenu principal

room1

Salle d'accueil

Objets et porte vers le laboratoire

room2

Laboratoire

Coffre et CodePuzzle

room3

Salle informatique

Système informatique et HashPuzzle

room4

Salle de sortie

Salle finale

Tests fonctionnels

Les principales fonctionnalités ont été vérifiées avec Swagger :

L'API démarre avec Uvicorn.

La route GET /health fonctionne.

La route GET /rooms retourne les salles.

La route GET /rooms/{room_id} retourne une salle précise.

Une salle inexistante retourne une erreur 404.

CodePuzzle accepte une bonne réponse.

CodePuzzle refuse une mauvaise réponse.

HashPuzzle vérifie correctement une réponse avec SHA-256.

Une réponse vide est refusée avec une erreur 422.

Une bonne réponse à un puzzle retourne success: true.

Une mauvaise réponse retourne success: false.

Architecture

Le projet suit une séparation simple entre :

Données du jeu
      ↓
Classes métier (POO)
      ↓
Routes FastAPI
      ↓
Validation Pydantic
      ↓
API REST

Cette organisation permet de séparer la logique du jeu, la validation des données et la communication avec le client.

Objectif du projet

Ce projet a pour objectif de mettre en pratique :

la programmation orientée objet en Python ;

l'héritage et les classes abstraites ;

la création d'une API REST ;

FastAPI ;

Pydantic et la validation automatique ;

les méthodes HTTP GET et POST ;

la gestion des erreurs HTTP ;

la documentation automatique avec Swagger / OpenAPI ;

le fonctionnement d'une énigme utilisant SHA-256.