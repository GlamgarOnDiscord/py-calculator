import tkinter as tk
from math import *

# Fonction pour mettre à jour l'affichage de la calculatrice
def update_display(value):
    current = display_var.get()
    display_var.set(current + str(value))

# Fonction pour effacer tout
def clear():
    display_var.set("")

# Fonction pour effectuer le calcul
def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        display_var.set("Erreur")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Variable de contrôle pour l'affichage
display_var = tk.StringVar()

# Création de l'écran de la calculatrice
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Création des boutons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'AC'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'AC':
        tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 20), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 20), command=lambda b=button: update_display(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Exécution de la boucle principale
root.mainloop()
