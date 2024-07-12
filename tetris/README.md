# Tetris Game

![Tetris Gameplay](./gif/pub.gif)

## Introduction

Bienvenue dans notre implémentation de Tetris en Python en utilisant la bibliothèque Pygame. Ce projet est un jeu de Tetris classique où vous pouvez jouer, ajuster la vitesse du jeu dans les paramètres, et profiter de la musique de fond. Le jeu est conçu pour être simple à utiliser et agréable à jouer.

## Table des Matières

- [Installation](#installation)
- [Usage](#usage)
- [Fonctionnalités](#fonctionnalités)
- [Structure du Code](#structure-du-code)
- [Note](#note)

## Installation

1. Clonez le dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/votre-utilisateur/python.git
    cd tetris
    ```

2. Assurez-vous d'avoir **Python 3** installé sur votre machine.

3. Installez les dépendances requises (Pygame principalement) :
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Pour lancer le jeu, exécutez le fichier principal :

```bash
python tetris.py
```

## Fonctionnalités

- **Jeu de Tetris classique** : Jouez au Tetris avec les contrôles de direction et rotation.
- **Menu principal** : Accédez au jeu ou aux paramètres depuis le menu principal.
- **Paramètres de vitesse** : Choisissez entre trois vitesses différentes (Lent, Moyen, Rapide).
- **Musique de fond** : Profitez de la musique pendant que vous jouez.

## Structure du Code
Le code est organisé en plusieurs fonctions pour gérer les différentes parties du jeu :

- `main_menu()`
La fonction main_menu affiche le menu principal où vous pouvez choisir de jouer ou d'accéder aux paramètres.

- `settings_menu()`
La fonction settings_menu permet de sélectionner la vitesse du jeu. Il y a trois options : Lent, Moyen et Rapide.

- `main(fall_speed)`
La fonction main est le cœur du jeu Tetris. Elle gère le jeu principal, y compris la création des pièces, la détection des collisions, la gestion des entrées utilisateur et l'affichage du score.

- `draw_window(surface, grid, score)`
Cette fonction dessine la fenêtre de jeu avec la grille actuelle et le score.

- `draw_button(surface, text, rect, color, text_color)`
Cette fonction dessine un bouton à l'écran avec le texte et les couleurs spécifiés.

- `play_music(file)`
Cette fonction joue de la musique en utilisant le fichier spécifié.

## Note

Une belle musique d'acceuil vous attend au lancement du jeu. Attention aux oreilles !