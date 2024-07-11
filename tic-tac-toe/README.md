# Tic Tac Toe

Ce projet est une implémentation du jeu classique Tic Tac Toe en Python, avec deux versions : une version graphique utilisant Tkinter et une version en terminal. Ce projet comprend quatre fichiers principaux :

1. `tic_tac_toe.py` : version graphique du jeu.
2. `tic_tac_toe_terminal.py` : version terminal du jeu.
3. `application.py` : interface pour lancer le jeu.
4. `main.py` : point d'entrée pour exécuter le jeu.

## Table des Matières

- [Installation](#installation)
- [Descritpion des fichiers](#description-des-fichiers)
- [Usage](#usage)
  - [Version Graphique](#version-graphique)
  - [Version Terminal](#version-terminal)
- [Fonctionnalités](#fonctionnalités)

## Installation

1. Clonez le dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/votre-utilisateur/python.git
    cd tic-tac-toe
    ```

2. Assurez-vous d'avoir **Python 3** installé sur votre machine.

3. Installez les dépendances requises (Tkinter est inclus dans la distribution standard de Python, mais peut nécessiter une installation séparée selon votre système) :
    ```bash
    pip install -r requirements.txt
    ```

## Description des fichiers

### tic_tac_toe.py
Ce fichier contient la classe TicTacToe, qui représente le jeu de Tic Tac Toe avec une interface graphique.

#### Fonctionnalités principales :
- Menu principal avec options pour commencer une nouvelle partie (1vs1 ou contre l'ordinateur), afficher les règles, afficher la licence et quitter le jeu.
- Saisie des noms des joueurs.
- Choix de la difficulté lorsque l'on joue contre l'ordinateur (Facile, Moyen, Difficile).
- Interface utilisateur pour jouer au jeu avec une grille graphique.
- Gestion des tours de jeu, vérification des gagnants et des égalités.
- Affichage des règles et de la licence via des boîtes de dialogue.

#### Exemple de code source :
```python
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    """Classe représentant le jeu de Tic Tac Toe."""

    def __init__(self, root):
        """Initialise le jeu avec la fenêtre principale."""
        self.root = root
        self.root.title("Tic Tac Toe")
        self.main_menu()

        # Initialisation des noms par défaut
        self.player1_name = "Joueur 1"
        self.player2_name = "Joueur 2"
        self.computer_name = "Ordinateur"
        self.player_name = "Vous"

    def main_menu(self):
        """Affiche le menu principal avec les options de jeu."""
        self.clear_screen()

        # Titre
        title = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 24))
        title.pack(pady=20)

        # Boutons du menu principal
        btn_1vs1 = tk.Button(self.root, text="1 vs 1", command=self.enter_names)
        btn_1vs1.pack(pady=5)

        btn_vs_computer = tk.Button(self.root, text="Contre l'ordinateur", command=self.choose_difficulty)
        btn_vs_computer.pack(pady=5)

        btn_rules = tk.Button(self.root, text="Règles", command=self.show_rules)
        btn_rules.pack(pady=5)

        btn_license = tk.Button(self.root, text="Licence", command=self.show_license)
        btn_license.pack(pady=5)

        btn_quit = tk.Button(self.root, text="Quitter", command=self.root.quit)
        btn_quit.pack(pady=5)

    def clear_screen(self):
        """Efface tous les widgets de la fenêtre principale."""
        for widget in self.root.winfo_children():
            widget.destroy()

    # Méthodes supplémentaires pour enter_names, choose_difficulty, show_rules, show_license, play_game, check_winner, etc.
```

### tic_tac_toe_terminal.py
Ce fichier contient le jeu de Tic Tac Toe jouable dans le terminal.

#### Fonctionnalités principales :
- Interface en ligne de commande pour jouer au Tic Tac Toe.
- Gestion des tours de jeu, vérification des gagnants et des égalités.

Exemple de code source :
```python
def print_board(board):
    """Affiche le plateau de jeu."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie s'il y a un gagnant ou une égalité."""
    # Vérification des lignes, des colonnes et des diagonales
    # ...

def play_game():
    """Lance une partie de Tic Tac Toe dans le terminal."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Joueur {current_player}, entrez la ligne (0, 1, 2) : "))
        col = int(input(f"Joueur {current_player}, entrez la colonne (0, 1, 2) : "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Joueur {current_player} a gagné !")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Case déjà occupée. Essayez à nouveau.")

if __name__ == "__main__":
    play_game()
```

### application.py
Ce fichier contient la logique pour lancer l'application de Tic Tac Toe.

Exemple de code source :
```python
import tic_tac_toe
import tic_tac_toe_terminal

if __name__ == "__main__":
    choice = input("Voulez-vous jouer en mode graphique (1) ou en mode terminal (2) ? ")
    if choice == "1":
        import tkinter as tk
        root = tk.Tk()
        game = tic_tac_toe.TicTacToe(root)
        root.mainloop()
    elif choice == "2":
        tic_tac_toe_terminal.play_game()
    else:
        print("Choix invalide. Veuillez relancer le programme.")
```

### main.py
Ce fichier est le point d'entrée principal du programme.

Exemple de code source :
```python
import application

if __name__ == "__main__":
    application.main()
```

## Usage

### Version Graphique

Pour lancer la version graphique du jeu :

```bash
python main.py
```

Lorsque vous lancez le jeu, le jeu vous demandera si vous souhaitez jouer en mode graphique ou terminal. Choisissez l'option graphique pour commencer une partie en mode GUI. Une fenêtre Tkinter s'ouvre avec le menu principal. Voici les options disponibles :

- **1 vs 1** : Commence une partie entre deux joueurs humains.
- **Contre l'ordinateur** : Commence une partie contre l'ordinateur. Vous devrez choisir le niveau de difficulté.
- **Règles** : Affiche les règles du jeu dans une boîte de dialogue.
- **Licence** : Affiche la licence du jeu dans une boîte de dialogue.
- **Quitter** : Ferme la fenêtre du jeu.

#### Fonctionnalités du jeu graphique
- Saisie des noms des joueurs : Avant de commencer une partie, vous pouvez saisir les noms des joueurs.
- Choix de la difficulté contre l'ordinateur : Vous pouvez choisir entre trois niveaux de difficulté (Facile, Moyen, Difficile) lorsque vous jouez contre l'ordinateur.
- Interface utilisateur intuitive : La grille du jeu est affichée et vous pouvez cliquer sur les cases pour jouer votre tour.
- Gestion des tours et vérification des gagnants : Le jeu gère automatiquement les tours des joueurs et vérifie les conditions de victoire ou d'égalité.

### Version Terminal
Pour lancer la version terminal du jeu :

```bash
python main.py
```

Lorsque vous lancez le jeu en mode terminal, le jeu vous demandera si vous souhaitez jouer en mode graphique ou terminal. Choisissez l'option terminal pour commencer une partie dans le terminal (CLI).

#### Fonctionnalités du jeu terminal
- **Affichage du plateau** : Le plateau de jeu est affiché dans le terminal.
- **Saisie des mouvements** : Les joueurs saisissent les coordonnées de leurs mouvements (ligne et colonne).
- **Gestion des tours et vérification des gagnants** : Le jeu gère automatiquement les tours des joueurs et vérifie les conditions de victoire ou d'égalité.

### Fonctionnalités

- **Deux modes de jeu** : Version graphique avec Tkinter et version terminal.
- **Jouabilité contre l'ordinateur** : Jouez contre l'ordinateur avec différents niveaux de difficulté.
- **Gestion des tours** : Le jeu gère les tours des joueurs et la vérification des gagnants.
- **Affichage des règles et de la licence** : Affiche les règles du jeu et la licence dans des boîtes de dialogue.