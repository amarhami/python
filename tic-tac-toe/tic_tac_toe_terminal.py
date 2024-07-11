import random
import os

class TicTacToeTerminal:
    """Classe pour jouer au Tic Tac Toe dans le terminal."""

    def __init__(self):
        """Initialise le jeu avec une grille vide et les paramètres nécessaires."""
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """Affiche la grille actuelle."""
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """Retourne une liste des mouvements disponibles."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """Vérifie s'il reste des cases vides."""
        return ' ' in self.board

    def num_empty_squares(self):
        """Retourne le nombre de cases vides."""
        return self.board.count(' ')

    def make_move(self, square, letter):
        """Fait un mouvement dans une case donnée."""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """Détermine s'il y a un gagnant."""
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def play(self):
        """Lance une partie contre un autre joueur ou l'ordinateur."""
        print("\nChoisissez le mode de jeu :")
        print("1. 1 joueur (contre l'ordinateur)")
        print("2. 2 joueurs (1vs1)")
        mode = input("Votre choix : ")

        if mode not in ['1', '2']:
            print("Choix invalide. Mode par défaut : 1 joueur (contre l'ordinateur)")
            mode = '1'

        if mode == '1':
            self.play_vs_computer()
        else:
            self.play_1vs1()

    def play_vs_computer(self):
        """Lance une partie contre l'ordinateur."""
        print("\nChoisissez le niveau de difficulté :")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        difficulty = input("Votre choix : ")

        if difficulty not in ['1', '2', '3']:
            print("Choix invalide. Niveau par défaut : Facile")
            difficulty = '1'

        player_letter = 'X'
        computer_letter = 'O'
        turn = 'player'

        while self.empty_squares():
            if turn == 'player':
                self.print_board()
                square = self.get_player_move()
                if self.make_move(square, player_letter):
                    if self.current_winner:
                        self.print_board()
                        print(f"Félicitations ! Vous avez gagné !")
                        return
                    turn = 'computer'
            else:
                if difficulty == '1':
                    square = self.get_random_move()
                elif difficulty == '2':
                    square = self.get_smart_move()
                else:
                    square = self.get_best_move(computer_letter)
                if self.make_move(square, computer_letter):
                    if self.current_winner:
                        self.print_board()
                        print(f"Vous avez perdu ! L'ordinateur a gagné.")
                        return
                    turn = 'player'

        self.print_board()
        print("Match nul !")

    def play_1vs1(self):
        """Lance une partie 1vs1 entre deux joueurs."""
        player1_letter = 'X'
        player2_letter = 'O'
        turn = 'player1'

        while self.empty_squares():
            self.print_board()
            if turn == 'player1':
                square = self.get_player_move()
                if self.make_move(square, player1_letter):
                    if self.current_winner:
                        self.print_board()
                        print(f"Joueur 1 gagne !")
                        return
                    turn = 'player2'
            else:
                square = self.get_player_move()
                if self.make_move(square, player2_letter):
                    if self.current_winner:
                        self.print_board()
                        print(f"Joueur 2 gagne !")
                        return
                    turn = 'player1'

        self.print_board()
        print("Match nul !")

    def get_player_move(self):
        """Demande au joueur de faire un mouvement."""
        valid_square = False
        val = None
        while not valid_square:
            square = input("Votre mouvement (0-8) : ")
            try:
                val = int(square)
                if val not in self.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Mouvement invalide. Réessayez.")
        return val

    def get_random_move(self):
        """Retourne un mouvement aléatoire pour l'ordinateur."""
        return random.choice(self.available_moves())

    def get_smart_move(self):
        """Retourne un mouvement 'intelligent' pour l'ordinateur."""
        for move in self.available_moves():
            self.board[move] = 'O'
            if self.winner(move, 'O'):
                self.board[move] = ' '
                return move
            self.board[move] = ' '
        return self.get_random_move()

    def get_best_move(self, letter):
        """Retourne le meilleur mouvement possible pour l'ordinateur."""
        if len(self.available_moves()) == 9:
            return random.choice(self.available_moves())
        best_move = None
        best_score = -float('inf')
        for move in self.available_moves():
            self.board[move] = letter
            score = self.minimax(self.board, False, letter)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, board, is_maximizing, player):
        """Algorithme Minimax pour trouver le meilleur mouvement."""
        if self.winner_move('O'):
            return 1
        elif self.winner_move('X'):
            return -1
        elif not self.empty_squares():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.available_moves():
                board[move] = 'O'
                score = self.minimax(board, False, 'O')
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                board[move] = 'X'
                score = self.minimax(board, True, 'X')
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def winner_move(self, letter):
        """Détermine si un mouvement mène à une victoire."""
        for i in range(9):
            if self.board[i] == letter and self.winner(i, letter):
                return True
        return False
