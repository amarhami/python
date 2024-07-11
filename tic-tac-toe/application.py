from abc import ABC, abstractmethod

class Application(ABC):
    """Classe abstraite pour les applications."""

    @abstractmethod
    def run(self):
        """Méthode pour lancer l'application."""
        pass

    @abstractmethod
    def quit(self):
        """Méthode pour quitter l'application."""
        pass

class TerminalApplication(Application):
    """Application pour le terminal."""

    def run(self):
        """Lance l'application terminal."""
        print("Lancement de l'application terminal...")
        self.main_menu()

    def main_menu(self):
        """Affiche le menu principal dans le terminal."""
        while True:
            print("\nTic Tac Toe - Terminal")
            print("1. Nouvelle Partie")
            print("2. Règles")
            print("3. Licence")
            print("4. Quitter")
            choice = input("Votre choix : ")

            if choice == '1':
                self.start_game()
            elif choice == '2':
                self.show_rules()
            elif choice == '3':
                self.show_license()
            elif choice == '4':
                self.quit()
                break
            else:
                print("Choix invalide.")

    def start_game(self):
        """Démarre une nouvelle partie."""
        from tic_tac_toe_terminal import TicTacToeTerminal
        game = TicTacToeTerminal()
        game.play()

    def show_rules(self):
        """Affiche les règles du jeu."""
        print("\nLes règles du Tic Tac Toe sont simples :")
        print("1. Le jeu se joue à deux joueurs, X et O.")
        print("2. Les joueurs jouent à tour de rôle.")
        print("3. Le premier joueur à aligner trois de ses symboles horizontalement, verticalement ou en diagonale gagne.")
        print("4. Si toutes les cases sont remplies sans qu'il y ait de gagnant, la partie est nulle.")

    def show_license(self):
        """Affiche les informations de licence."""
        print("\nLicence :")
        print("Ce jeu de Tic Tac Toe est distribué sous la licence MIT.")
        print("Vous êtes libre de l'utiliser, le modifier et le distribuer.")

    def quit(self):
        """Quitte l'application."""
        print("Fermeture de l'application terminal...")

class GUIApplication(Application):
    """Application pour l'interface graphique."""

    def run(self):
        """Lance l'application graphique."""
        print("Lancement de l'application graphique...")
        from tic_tac_toe import TicTacToe
        import tkinter as tk

        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

    def quit(self):
        """Quitte l'application."""
        print("Fermeture de l'application graphique...")
