import tkinter as tk
from tkinter import PhotoImage
import pygame
import random

# Initialisation de Pygame pour les sons
pygame.mixer.init()

# Variables globales
current_ref = None
displayed_refs = []

# Fonction pour jouer un son
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Fonction pour jouer la musique d'accueil
def play_welcome_music():
    pygame.mixer.music.load('./sounds/welcome_music.mp3')
    pygame.mixer.music.play(-1)  # Boucle infinie

# Fonction pour générer et jouer une référence aléatoire parmi les 4 affichées
def play_random_ref():
    global current_ref
    current_ref = random.choice(displayed_refs)
    play_sound(f'./sounds/sound{current_ref}.mp3')
    result_label.config(text="")  # Efface le message de résultat

# Fonction pour vérifier si la réponse est correcte
def check_answer(idx):
    if idx == current_ref:
        pygame.mixer.music.stop()  # Arrêter le son
        result_label.config(text="Correct!", fg="green")
        update_displayed_refs()  # Change les références affichées
    else:
        result_label.config(text="Wrong! Try again.", fg="red")
    result_label.pack(pady=10)

# Fonction pour mettre à jour les références affichées
def update_displayed_refs():
    global displayed_refs, current_ref
    displayed_refs = random.sample(range(1, 13), 4)
    current_ref = None
    for widget in grid_frame.winfo_children():
        widget.destroy()
    create_grid()

# Fonction pour créer la grille dans le Canvas
def create_grid():
    for j in range(4):
        idx = displayed_refs[j]
        frame = tk.Frame(grid_frame, width=200, height=200, bg="white", highlightbackground="black", highlightthickness=1)
        frame.grid(row=0, column=j, padx=20, pady=20)
        img = PhotoImage(file=f'./images/image{idx}.png')
        button = tk.Button(frame, image=img, command=lambda idx=idx: check_answer(idx))
        button.image = img
        button.config(width=335, height=335)
        button.pack(expand=True)
        label = tk.Label(frame, text=f'Réf {idx}', font=("Roboto", 12), bg="white")
        label.pack()

# Fonction pour afficher la grille dans le Canvas
def show_grid():
    # Arrêter la musique d'accueil
    pygame.mixer.music.stop()

    # Détruire tous les widgets existants dans la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()

    # Bouton pour jouer une référence aléatoire
    play_button = tk.Button(root, text="Play Random Ref", font=("Roboto", 18), bg="#4CAF50", fg="white", command=play_random_ref)
    play_button.pack(pady=20)

    # Label pour afficher le résultat
    global result_label
    result_label = tk.Label(root, text="", font=("Roboto", 18), bg="white")
    result_label.pack(pady=10)

    # Création du Canvas avec une barre de défilement verticale
    global grid_frame
    canvas = tk.Canvas(root, bg="white", width=800, height=600, scrollregion=(0, 0, 1000, 1000))
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Ajout de la barre de défilement verticale
    v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=v_scrollbar.set)

    # Créer une nouvelle frame pour contenir la grille
    grid_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=grid_frame, anchor='nw')

    # Mettre à jour les références affichées
    update_displayed_refs()

    # Mettre à jour la taille du canvas
    grid_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Fonction pour afficher la page d'accueil
def show_home():
    # Détruire tous les widgets existants dans la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()

    # Création du Canvas pour la page d'accueil
    home_canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    home_canvas.pack(fill="both", expand=True)

    # Charger l'image de fond et redimensionner
    bg_image = PhotoImage(file='./images/background.png')
    home_canvas.create_image(0, 0, image=bg_image, anchor='nw')

    # Ajouter le texte et le bouton par-dessus l'image de fond
    welcome_label = tk.Label(root, text="FIND THE REF", font=("Roboto", 46, "bold"), bg="white", fg="#4CAF50")
    start_button = tk.Button(root, text="START", font=("Roboto", 24, "bold"), bg="#4CAF50", fg="white", command=show_grid)

    # Calculer les positions pour centrer les widgets
    label_x = screen_width // 2
    label_y = screen_height // 2 - 50

    button_x = screen_width // 2
    button_y = screen_height // 2 + 50

    # Ajouter les widgets au Canvas
    home_canvas.create_window(label_x, label_y, window=welcome_label)
    home_canvas.create_window(button_x, button_y, window=start_button)

    # Conserver une référence à l'image pour éviter qu'elle soit garbage collected
    home_canvas.image = bg_image

    # Jouer la musique d'accueil
    play_welcome_music()

# Fonction pour quitter le plein écran
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Création de la fenêtre principale
root = tk.Tk()
root.title("FIND THE REF")
root.geometry("1920x1080")
root.configure(bg="white")

# Obtenir la taille de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Mettre la fenêtre en mode zoomé (plein écran sans cacher les boutons)
root.state('zoomed')

# Lier la touche 'Esc' pour quitter le plein écran
root.bind("<Escape>", exit_fullscreen)

# Afficher la page d'accueil
show_home()

# Lancement de l'application
root.mainloop()
