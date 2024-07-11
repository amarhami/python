from application import TerminalApplication, GUIApplication

def main():
    """Point d'entrée principal de l'application."""
    print("Choisissez une version de l'application :")
    print("1. Terminal")
    print("2. Interface graphique")
    choice = input("Votre choix : ")

    if choice == '1':
        app = TerminalApplication()
    elif choice == '2':
        app = GUIApplication()
    else:
        print("Choix invalide.")
        return

    app.run()

if __name__ == "__main__":
    main()
