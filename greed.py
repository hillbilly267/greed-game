import tkinter as tk
import random

# Globala variabler
players = 0
scores = []
current = 0
round_points = 0

# Töm fönstret
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# Meny
def show_menu():
    clear()
    root.config(bg="#222831")  # Mörk bakgrund
    tk.Label(root, text="Tärningsspel", font=("Arial", 22, "bold"), bg="#222831", fg="#ffd369").pack(pady=30)
    tk.Button(
        root, text="Spela", command=choose_players,
        bg="#393e46", fg="#ffd369",
        font=("Arial", 16, "bold"),
        width=16, height=2,
    ).pack(pady=15)
    tk.Button(
        root, text="Manual", command=show_manual,
        bg="#393e46", fg="#ffd369",
        font=("Arial", 16, "bold"),
        width=16, height=2,
    ).pack(pady=5)

# Manual
def show_manual():
    clear()
    tk.Label(root, text="Manual",bg="#393e46", fg="#ffd369",font=("Arial", 18, "bold")).pack(pady=10)
    tk.Label(root, text="Först till 50 poäng.\nKasta tärningen eller spara poängen.\nSlår du 1 förlorar du rundans poäng och turen går vidare.",bg="#393e46", fg="#ffd369",font=("Arial", 10, "bold")).pack(pady=10)
    tk.Button(root, text="Tillbaka", bg="#393e46", fg="#ffd369",font=("Arial", 18, "bold"), command=show_menu).pack(pady=10)

# Välj antal spelare
def choose_players():
    clear()
    root.config(bg="#222831")
    tk.Label(root, text="Välj antal spelare", font=("Arial", 16, "bold"), bg="#222831", fg="#ffd369").pack(pady=20)
    for i in range(2, 7):
        tk.Button(
            root, text=f"{i} spelare", command=lambda n=i: start_game(n),
            bg="#393e46", fg="#ffd369",
            font=("Arial", 14, "bold"),
            width=16, height=1,).pack(pady=7)
    tk.Button(
        root, text="Tillbaka", command=show_menu,
        bg="#393e46", fg="#ffd369",
        font=("Arial", 12, "bold"),
        width=12, height=1,
    ).pack(pady=15)

# Starta spelet
def start_game(n):
    global players, scores, current, round_points
    players = n
    scores = [0]*n
    current = 0
    round_points = 0
    show_game_ui()

# Skapa spelets UI
def show_game_ui():
    clear()
    global score_labels, turn_label, dice_label, round_label, feedback_label, roll_btn, hold_btn

    score_labels = []
    frame1 = tk.Frame(root, bg="#393e46")
    frame2 = tk.Frame(root, bg="#393e46")
    frame1.pack(pady=5)
    frame2.pack(pady=5)
    for i in range(players):
        lbl = tk.Label(
            frame1 if i < 2 else frame2,
            text=f"Spelare {i+1}: 0",
            bg="#393e46", fg="#ffd369",
            font=("Arial", 14, "bold")
        )
        lbl.pack(side="left", padx=10)
        score_labels.append(lbl)

    turn_label = tk.Label(root, text=f"Tur: Spelare {current+1}", bg="#393e46", fg="#ffd369",font=("Arial", 18, "bold"))
    turn_label.pack(pady=10)

    dice_label = tk.Label(root, text="Tärning: -",bg="#393e46", fg="#ffd369",font=("Arial", 20, "bold"))
    dice_label.pack()

    round_label = tk.Label(root, text="Pool: 0",bg="#393e46", fg="#ffd369",font=("Arial", 10, "bold"))
    round_label.pack(pady=5)

    feedback_label = tk.Label(root, text="", bg="#393e46", fg="#ffd369",font=("Arial", 10, "bold"))
    feedback_label.pack(pady=5)

    roll_btn = tk.Button(root, text="Kasta", bg="#393e46", fg="#ffd369",font=("Arial", 12, "bold"), command=roll_dice)
    roll_btn.pack(pady=5)

    hold_btn = tk.Button(root, text="Spara", bg="#393e46", fg="#ffd369",font=("Arial", 12, "bold"), command=hold_points)
    hold_btn.pack(pady=5)

    tk.Button(root, text="Meny", bg="#393e46", fg="#ffd369",font=("Arial", 10, "bold"), command=show_menu).pack(pady=10)

# Kasta tärningen
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

# Spara poängen
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

# Byt spelare
def switch_turn():
    global current, round_points
    current = (current + 1) % players
    round_points = 0
    update_scores()
    turn_label.config(text=f"Tur: Spelare {current+1}")
    round_label.config(text="Runda: 0")
    feedback_label.config(text="")
    enable_buttons()

# Uppdatera poängvisning
def update_scores():
    for i in range(players):
        score_labels[i].config(text=f"Spelare {i+1}: {scores[i]}")

# Inaktivera knappar
def disable_buttons():
    roll_btn.config(state="disabled")
    hold_btn.config(state="disabled")

# Aktivera knappar
def enable_buttons():
    roll_btn.config(state="normal")
    hold_btn.config(state="normal")

# Starta spelet
root = tk.Tk()
root.title("Tärningsspel")
root.geometry("400x400")
show_menu()
root.mainloop()