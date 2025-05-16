import tkinter as tk
import random

# S: Globala variabler
players = 0
scores = []
current = 0
round_points = 0

# S: Töm fönstret
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# D: Meny
def show_menu():
    clear()
    tk.Label(root, text="Tärningsspel", font=("Arial", 20)).pack(pady=20)
    tk.Button(root, text="Spela", command=choose_players, font=("Arial", 14), height=2, width=15).pack(pady=10)
    tk.Button(root, text="Manual", command=show_manual, font=("Arial", 14), height=2, width=15).pack(pady=10)

# D: Manual
def show_manual():
    clear()
    tk.Label(root, text="Manual", font=("Arial", 18)).pack(pady=10)
    tk.Label(root, text="Först till 50 poäng.\nKasta tärningen eller spara poängen.\nSlår du 1 förlorar du rundans poäng och turen går vidare.").pack(pady=10)
    tk.Button(root, text="Tillbaka", command=show_menu).pack(pady=10)

# S/D: Välj antal spelare
def choose_players():
    clear()
    tk.Label(root, text="Välj antal spelare", font=("Arial", 16)).pack(pady=10)
    for i in range(2, 7):
        tk.Button(root, text=f"{i} spelare", command=lambda n=i: start_game(n), font=("Arial"), height=2, width=8).pack(pady=5)

# S: Starta spelet
def start_game(n):
    global players, scores, current, round_points
    players = n
    scores = [0]*n
    current = 0
    round_points = 0
    show_game_ui()

# S: Skapa spelets UI
def show_game_ui():
    clear()
    global score_labels, turn_label, dice_label, round_label, feedback_label, roll_btn, hold_btn

    score_labels = []
    for i in range(players):
        lbl = tk.Label(root, text=f"Spelare {i+1}: 0")
        lbl.pack()
        score_labels.append(lbl)

    turn_label = tk.Label(root, text=f"Tur: Spelare {current+1}", font=("Arial", 14, "bold"))
    turn_label.pack(pady=10)

    dice_label = tk.Label(root, text="Tärning: -", font=("Arial", 20))
    dice_label.pack()

    round_label = tk.Label(root, text="Runda: 0")
    round_label.pack(pady=5)

    feedback_label = tk.Label(root, text="")
    feedback_label.pack(pady=5)

    roll_btn = tk.Button(root, text="Kasta", command=roll_dice)
    roll_btn.pack(pady=5)

    hold_btn = tk.Button(root, text="Spara", command=hold_points)
    hold_btn.pack(pady=5)

    tk.Button(root, text="Meny", command=show_menu).pack(pady=10)

# S: Kasta tärningen
def roll_dice():
    global round_points
    value = random.randint(1, 6)
    dice_label.config(text=f"Tärning: {value}")
    if value == 1:
        round_points = 0
        round_label.config(text="Runda: 0")
        feedback_label.config(text=f"Spelare {current+1} slog 1!")
        disable_buttons()
        root.after(1000, switch_turn)
    else:
        round_points += value
        round_label.config(text=f"Runda: {round_points}")

# S: Spara poängen
def hold_points():
    global scores, round_points
    scores[current] += round_points
    if scores[current] >= 50:
        feedback_label.config(text=f"Spelare {current+1} vinner!")
        disable_buttons()
        return
    round_points = 0
    update_scores()
    feedback_label.config(text=f"Spelare {current+1} sparade sina poäng.")
    disable_buttons()
    root.after(1000, switch_turn)

# S: Byt spelare
def switch_turn():
    global current, round_points
    current = (current + 1) % players
    round_points = 0
    update_scores()
    turn_label.config(text=f"Tur: Spelare {current+1}")
    round_label.config(text="Runda: 0")
    feedback_label.config(text="")
    enable_buttons()

# S: Uppdatera poängvisning
def update_scores():
    for i in range(players):
        score_labels[i].config(text=f"Spelare {i+1}: {scores[i]}")

# S: Inaktivera knappar
def disable_buttons():
    roll_btn.config(state="disabled")
    hold_btn.config(state="disabled")

# S: Aktivera knappar
def enable_buttons():
    roll_btn.config(state="normal")
    hold_btn.config(state="normal")

# S: Starta spelet
root = tk.Tk()
root.title("Tärningsspel")
root.geometry("400x400")
show_menu()
root.mainloop()