# Soundbox Quiz - FIND THE REF

![Soundbox Quiz](./images/background.png)

## Introduction

Bienvenue dans le Soundbox Quiz "FIND THE REF". Ce jeu interactif vous met au défi de reconnaître des sons et de les associer à leurs références visuelles correspondantes. Développé en Python avec Tkinter pour l'interface graphique et Pygame pour la gestion des sons, ce jeu est à la fois amusant et éducatif.

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
    cd soundbox
    ```

2. Assurez-vous d'avoir **Python 3** installé sur votre machine.

3. Installez les dépendances requises (Pygame, Tkinter est inclus dans la distribution standard de Python, mais peut nécessiter une installation séparée selon votre système) :
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Pour lancer le jeu, exécutez le fichier principal :

```bash
python soundbox.py
```

## Fonctionnalités

- **Page d'accueil interactive** : Une page d'accueil avec musique de fond et boutons de navigation.
- **Jeu de quiz sonore** : Écoutez un son et essayez de trouver l'image correspondante parmi une grille d'images.
- **Feedback instantané** : Recevez un feedback immédiat (correct ou incorrect) lorsque vous sélectionnez une image.
- **Musique de fond** : Une musique d'accueil est jouée à l'écran d'accueil.

## Structure du Code
Le code est organisé en plusieurs fonctions pour gérer les différentes parties du jeu :

- `play_sound(sound_file)`
Cette fonction joue le son spécifié.

- `play_welcome_music()`
Cette fonction joue la musique de fond d'accueil en boucle infinie.

- `play_random_ref()`
Cette fonction sélectionne et joue un son aléatoire à partir de la liste de références.

- `check_answer(idx)`
Cette fonction vérifie si l'image sélectionnée correspond au son joué et affiche le résultat (correct ou incorrect).

- `show_grid()`
Cette fonction affiche la grille d'images où les joueurs peuvent sélectionner l'image correspondant au son joué.

- `show_home()`
Cette fonction affiche la page d'accueil avec une image de fond, un titre et un bouton pour démarrer le jeu.

- `exit_fullscreen(event=None)`
Cette fonction permet de quitter le mode plein écran lorsque la touche 'Escape' est pressée.

- `main()`
La fonction principale initialise l'interface utilisateur et lance le jeu.

## Note

Une belle musique d'acceuil vous attend au lancement du jeu. Attention aux oreilles !