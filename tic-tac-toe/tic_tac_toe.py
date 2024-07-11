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
        """Affiche le menu principal avec les options."""
        self.clear_frame()

        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=('Roboto', 54, 'bold'))
        self.title_label.pack(pady=20)

        button_style = {'font': ('Roboto', 14, 'bold'), 'width': 30, 'height': 2}

        self.new_game_button_1vs1 = tk.Button(self.root, text="Nouvelle Partie (1vs1)", **button_style, bg='#4CAF50', fg='white', command=self.enter_player_names_1vs1)
        self.new_game_button_1vs1.pack(pady=10)

        self.new_game_button_vs_computer = tk.Button(self.root, text="Nouvelle Partie (vs Ordinateur)", **button_style, bg='#2196F3', fg='white', command=self.enter_player_name_vs_computer)
        self.new_game_button_vs_computer.pack(pady=10)

        self.rules_button = tk.Button(self.root, text="Règles", **button_style, bg='#FFC107', fg='black', command=self.show_rules)
        self.rules_button.pack(pady=10)

        self.license_button = tk.Button(self.root, text="Licence", **button_style, bg='#FF5722', fg='white', command=self.show_license)
        self.license_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quitter", **button_style, bg='red', fg='white', command=self.root.quit)
        self.quit_button.pack(pady=10)

    def enter_player_names_1vs1(self):
        """Permet de saisir les noms des joueurs pour le mode 1vs1."""
        self.clear_frame()

        self.title_label = tk.Label(self.root, text="Noms des joueurs", font=('Roboto', 24, 'bold'))
        self.title_label.pack(pady=20)

        tk.Label(self.root, text="Nom du Joueur 1 (X):", font=('Roboto', 14)).pack(pady=5)
        self.player1_name_entry = tk.Entry(self.root, font=('Roboto', 14))
        self.player1_name_entry.pack(pady=5)

        tk.Label(self.root, text="Nom du Joueur 2 (O):", font=('Roboto', 14)).pack(pady=5)
        self.player2_name_entry = tk.Entry(self.root, font=('Roboto', 14))
        self.player2_name_entry.pack(pady=5)

        start_button = tk.Button(self.root, text="Commencer", font=('Roboto', 14, 'bold'), bg='#4CAF50', fg='white', command=self.start_game_1vs1)
        start_button.pack(pady=20)

        back_button = tk.Button(self.root, text="Retour", font=('Roboto', 14, 'bold'), bg='#FF5722', fg='white', command=self.main_menu)
        back_button.pack(pady=10)

    def enter_player_name_vs_computer(self):
        """Permet de saisir le nom du joueur pour le mode contre l'ordinateur."""
        self.clear_frame()

        self.title_label = tk.Label(self.root, text="Nom du joueur", font=('Roboto', 24, 'bold'))
        self.title_label.pack(pady=20)

        tk.Label(self.root, text="Votre Nom (X):", font=('Roboto', 14)).pack(pady=5)
        self.player_name_entry = tk.Entry(self.root, font=('Roboto', 14))
        self.player_name_entry.pack(pady=5)

        start_button = tk.Button(self.root, text="Suivant", font=('Roboto', 14, 'bold'), bg='#4CAF50', fg='white', command=self.choose_difficulty)
        start_button.pack(pady=20)

        back_button = tk.Button(self.root, text="Retour", font=('Roboto', 14, 'bold'), bg='#FF5722', fg='white', command=self.main_menu)
        back_button.pack(pady=10)

    def choose_difficulty(self):
        """Permet au joueur de choisir la difficulté contre l'ordinateur."""
        self.player_name = self.player_name_entry.get() or "Vous"  # Mise à jour du nom du joueur
        #self.player_name = f"{player_name_entry}" if self.player_name_entry else "Vous"
        self.clear_frame()

        self.title_label = tk.Label(self.root, text="Choisissez la difficulté", font=('Roboto', 24, 'bold'))
        self.title_label.pack(pady=20)

        button_style = {'font': ('Roboto', 14, 'bold'), 'width': 20, 'height': 2}

        self.easy_button = tk.Button(self.root, text="Facile", **button_style, bg='#8BC34A', fg='white', command=lambda: self.choose_first_player(difficulty='easy'))
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self.root, text="Moyen", **button_style, bg='#FFC107', fg='black', command=lambda: self.choose_first_player(difficulty='medium'))
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self.root, text="Difficile", **button_style, bg='#F44336', fg='white', command=lambda: self.choose_first_player(difficulty='hard'))
        self.hard_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Retour au Menu", **button_style, bg='#607D8B', fg='white', command=self.main_menu)
        self.back_button.pack(pady=10)

    def choose_first_player(self, difficulty):
        """Permet au joueur de choisir qui commence la partie."""
        self.clear_frame()

        self.title_label = tk.Label(self.root, text="Qui commence ?", font=('Roboto', 24, 'bold'))
        self.title_label.pack(pady=20)

        button_style = {'font': ('Roboto', 14, 'bold'), 'width': 20, 'height': 2}

        self.player_first_button = tk.Button(self.root, text=f"{self.player_name} (X)", **button_style, bg='#4CAF50', fg='white', command=lambda: self.start_game(mode='vs_computer', difficulty=difficulty, first_player='X'))
        self.player_first_button.pack(pady=10)

        self.computer_first_button = tk.Button(self.root, text="Ordinateur (O)", **button_style, bg='#F44336', fg='white', command=lambda: self.start_game(mode='vs_computer', difficulty=difficulty, first_player='O'))
        self.computer_first_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Retour", **button_style, bg='#607D8B', fg='white', command=self.choose_difficulty)
        self.back_button.pack(pady=10)

    def start_game_1vs1(self):
        """Démarre une nouvelle partie en mode 1vs1."""
        self.player1_name = self.player1_name_entry.get() or "Joueur 1"
        self.player2_name = self.player2_name_entry.get() or "Joueur 2"
        self.start_game(mode='1vs1', first_player='X')

    def start_game(self, mode='1vs1', difficulty=None, first_player='X'):
        """Démarre une nouvelle partie."""
        self.clear_frame()
        self.board = [""] * 9
        self.current_player = first_player
        self.buttons = []
        self.mode = mode
        self.difficulty = difficulty
        self.create_widgets()

        # Si le mode est vs_computer et que l'ordinateur commence, faire jouer l'ordinateur
        if mode == 'vs_computer':
            if first_player == 'O':
                self.computer_move()

    def create_widgets(self):
        """Crée les widgets pour le jeu."""
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        #player_name = self.player1_name if self.current_player == 'X' else self.player2_name if self.mode == '1vs1' else self.player_name
        #player_name = ""
        if self.mode == '1vs1':
            player_name = self.player1_name if self.current_player == 'X' else self.player2_name
        elif self.mode == 'vs_computer':
            player_name = self.player_name if self.current_player == 'X' else self.computer_name

        self.status_label = tk.Label(self.root, text=f"Tour de {player_name} ({self.current_player})", font=('Roboto', 14))
        self.status_label.pack(pady=10)

        self.canvas = tk.Canvas(self.frame, width=300, height=300)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        self.draw_grid()

        self.reset_button = tk.Button(self.root, text="Retour au Menu", font=('Roboto', 14, 'bold'), width=20, height=2, padx=10, pady=10, bg='#FF5722', fg='white', command=self.main_menu)
        self.reset_button.pack(pady=20)

    def draw_grid(self):
        """Trace la grille du jeu sur le canevas."""
        for i in range(1, 3):
            self.canvas.create_line(100 * i, 0, 100 * i, 300, width=3)
            self.canvas.create_line(0, 100 * i, 300, 100 * i, width=3)

    def draw_symbol(self, row, col, symbol):
        """Dessine le symbole (X ou O) sur la grille."""
        x_center = col * 100 + 50
        y_center = row * 100 + 50

        if symbol == "X":
            self.canvas.create_line(x_center - 25, y_center - 25, x_center + 25, y_center + 25, width=4, fill='blue')
            self.canvas.create_line(x_center - 25, y_center + 25, x_center + 25, y_center - 25, width=4, fill='blue')
        else:
            self.canvas.create_oval(x_center - 25, y_center - 25, x_center + 25, y_center + 25, width=4, outline='red')

    def on_canvas_click(self, event):
        """Gère le clic sur le canevas pour jouer."""
        x, y = event.x, event.y
        col, row = x // 100, y // 100
        index = row * 3 + col
        
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.draw_symbol(row, col, self.current_player)

            if self.check_winner():
                if self.mode == '1vs1':
                    winner_name = self.player1_name if self.current_player == 'X' else self.player2_name
                elif self.mode == 'vs_computer':
                    winner_name = self.player_name if self.current_player == 'X' else self.computer_name
                #winner_name = self.player1_name if self.current_player == 'X' else self.player2_name if self.mode == '1vs1' else self.computer_name
                self.update_status(f"{winner_name} ({self.current_player}) a gagné!")
                messagebox.showinfo("Tic Tac Toe", f"{winner_name} ({self.current_player}) a gagné!")
                self.prompt_new_game()
            elif all(cell != "" for cell in self.board):
                self.update_status("Match nul!")
                messagebox.showinfo("Tic Tac Toe", "Match nul!")
                self.prompt_new_game()
            else:
                if self.mode == '1vs1':
                    self.current_player = "O" if self.current_player == "X" else "X"
                elif self.mode == 'vs_computer':
                    self.current_player = "O" if self.current_player == "X" else "X"
                    if self.current_player == 'O':
                        self.computer_move()
                #player_name = self.player1_name if self.current_player == 'X' else self.player2_name if self.mode == '1vs1' else self.computer_name
                if self.mode == '1vs1':
                    player_name = self.player1_name if self.current_player == 'X' else self.player2_name
                elif self.mode == 'vs_computer':
                    player_name = self.player_name if self.current_player == 'X' else self.computer_name
                self.update_status(f"Tour de {player_name} ({self.current_player})")

    def computer_move(self):
        """Effectue le mouvement de l'ordinateur."""
        if self.difficulty == 'easy':
            square = self.get_random_move()
        elif self.difficulty == 'medium':
            square = self.get_smart_move()
        elif self.difficulty == 'hard':
            square = self.get_best_move()

        computer_symbol = 'O'
        self.board[square] = computer_symbol
        row, col = square // 3, square % 3
        self.draw_symbol(row, col, computer_symbol)

        if self.check_winner():
            self.update_status(f"{self.computer_name} ({computer_symbol}) a gagné!")
            messagebox.showinfo("Tic Tac Toe", f"{self.computer_name} ({computer_symbol}) a gagné!")
            self.prompt_new_game()
        elif all(cell != "" for cell in self.board):
            self.update_status("Match nul!")
            messagebox.showinfo("Tic Tac Toe", "Match nul!")
            self.prompt_new_game()
        else:
            self.current_player = 'X'
            self.update_status(f"Tour de {self.player1_name} ({self.current_player})")

    def get_random_move(self):
        """Renvoie un mouvement aléatoire valide."""
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
        return random.choice(empty_cells)

    def get_smart_move(self):
        """Renvoie un mouvement intelligent."""
        # Si l'ordinateur peut gagner, il joue ce coup
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = 'O'
                if self.check_winner():
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Si l'adversaire peut gagner au prochain coup, l'ordinateur bloque ce coup
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = 'X'
                if self.check_winner():
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Sinon, jouer un coup aléatoire
        return self.get_random_move()

    def get_best_move(self):
        """Renvoie le meilleur mouvement possible en utilisant l'algorithme Minimax."""
        best_score = float('-inf')
        best_move = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, depth, is_maximizing):
        """Implémente l'algorithme Minimax."""
        if self.check_winner():
            return 1 if not is_maximizing else -1
        elif all(cell != "" for cell in board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        """Vérifie s'il y a un gagnant."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]  # Diagonales
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def update_status(self, message):
        """Met à jour le label de statut avec le message donné."""
        self.status_label.config(text=message)

    def prompt_new_game(self):
        """Invite l'utilisateur à jouer une nouvelle partie ou à retourner au menu."""
        response = messagebox.askyesno("Tic Tac Toe", "Voulez-vous jouer une nouvelle partie ?")
        if response:
            if self.mode == '1vs1':
                self.start_game(mode='1vs1', first_player='X')
            elif self.mode == 'vs_computer':
                #self.choose_difficulty()
                #self.choose_first_player(difficulty=self.difficulty)
                #self.start_game(mode='vs_computer', )
                self.enter_player_name_vs_computer()
        else:
            self.main_menu()

    def clear_frame(self):
        """Supprime tous les widgets de la fenêtre."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_rules(self):
        """Affiche une boîte de dialogue avec les règles du jeu."""
        rules = """
                        Règles du Tic Tac Toe:

        1. Le jeu se joue sur une grille de 3x3.
        
        2. Vous êtes X, votre ami (ou l'ordinateur) est O.
        
        3. Les joueurs jouent à tour de rôle pour placer leurs marques dans les cellules vides.
        
        4. Le premier joueur à aligner 3 de ses marques horizontalement, verticalement ou en diagonale gagne.
        
        5. Si toutes les 9 cellules sont remplies et qu'aucun joueur n'a aligné 3 marques, le jeu est déclaré match nul.
        """
        messagebox.showinfo("Règles du Tic Tac Toe", rules)

    def show_license(self):
        """Affiche une boîte de dialogue avec les informations de licence."""
        license_info = """
                                    Licence ADYXEM:
        
        Le logiciel Tic Tac Toe est sous licence ADYXEM. Vous êtes libre d'utiliser, de copier, de modifier, de fusionner, de publier, de distribuer, de sous-licencier et/ou de vendre des copies du logiciel, sous réserve des conditions suivantes :
        
        1. Le copyright et la permission de licence doivent être inclus dans toutes les copies ou portions substantielles du logiciel.
        
        2. LE LOGICIEL EST FOURNI "EN L'ÉTAT", SANS GARANTIE D'AUCUNE SORTE, EXPRIMÉE OU IMPLICITE, Y COMPRIS MAIS SANS S'Y LIMITER LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE DE CONTREFAÇON.
        """
        messagebox.showinfo("Licence", license_info)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
