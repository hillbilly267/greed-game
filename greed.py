import tkinter as tk
import random

# Globala variabler
players = 0
scores = []
current = 0
pool_points = 0

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
    global players, scores, current, pool_points
    players = n
    scores = [0]*n
    current = 0
    pool_points = 0
    show_game_ui()

# Skapa spelets UI
def show_game_ui():
    clear()
    global score_labels, turn_label, dice_label, pool_label, feedback_label, roll_btn, hold_btn
    root.config(bg="#222831")

    # Huvudkontainer
    main_frame = tk.Frame(root, bg="#222831")
    main_frame.pack(expand=True, fill='both')

    # Poängram högst upp
    score_frame = tk.Frame(main_frame, bg="#222831")
    score_frame.pack(fill='x', pady=20)
    
    score_labels = []
    players_per_row = min(3, players)
    for i in range(players):
        col = i % players_per_row
        row = i // players_per_row
        lbl = tk.Label(
            score_frame,
            text=f"Spelare {i+1}: 0",
            bg="#222831", fg="#ffd369",
            font=("Arial", 16, "bold")
        )
        lbl.grid(row=row, column=col, padx=20, pady=10)
        score_labels.append(lbl)

    # Spelinfo i mitten
    game_frame = tk.Frame(main_frame, bg="#222831")
    game_frame.pack(expand=True, fill='both', pady=20)

    turn_label = tk.Label(
        game_frame,
        text=f"Tur: Spelare {current+1}",
        bg="#222831", fg="#ffd369",
        font=("Arial", 24, "bold")
    )
    turn_label.pack(pady=20)

    dice_label = tk.Label(
        game_frame,
        text="Tärning: -",
        bg="#222831", fg="#ffd369",
        font=("Arial", 48, "bold")  # Mycket större tärningstext
    )
    dice_label.pack(pady=20)

    pool_label = tk.Label(
        game_frame,
        text="Pool: 0",
        bg="#222831", fg="#ffd369",
        font=("Arial", 32, "bold")  # Större pooltext
    )
    pool_label.pack(pady=20)

    feedback_label = tk.Label(
        game_frame,
        text="",
        bg="#222831", fg="#ffd369",
        font=("Arial", 18, "bold")
    )
    feedback_label.pack(pady=20)

    # Knappar längst ner
    button_frame = tk.Frame(main_frame, bg="#222831")
    button_frame.pack(fill='x', pady=30)

    roll_btn = tk.Button(
        button_frame,
        text="KASTA",
        bg="#393e46", fg="#ffd369",
        font=("Arial", 24, "bold"),  # Större knapptext
        width=10, height=2,
        command=roll_dice
    )
    roll_btn.pack(side='left', expand=True, padx=20)

    hold_btn = tk.Button(
        button_frame,
        text="SPARA",
        bg="#393e46", fg="#ffd369",
        font=("Arial", 24, "bold"),  # Större knapptext
        width=10, height=2,
        command=hold_points
    )
    hold_btn.pack(side='right', expand=True, padx=20)

    menu_btn = tk.Button(
        main_frame,
        text="MENY",
        bg="#393e46", fg="#ffd369",
        font=("Arial", 16, "bold"),  # Större menyknapp
        width=8, height=1,
        command=show_menu
    )
    menu_btn.pack(side='bottom', pady=20)

# Kasta tärningen
def roll_dice():
    global pool_points
    value = random.randint(1, 6)
    dice_label.config(text=f"Tärning: {value}")
    if value == 1:
        pool_points = 0
        pool_label.config(text="Pool: 0")
        feedback_label.config(text=f"Spelare {current+1} slog 1!")
        disable_buttons()
        root.after(1000, switch_turn)
    else:
        pool_points += value
        pool_label.config(text=f"Pool: {pool_points}")

# Spara poängen
def hold_points():
    global scores, pool_points
    scores[current] += pool_points
    if scores[current] >= 50:
        feedback_label.config(text=f"Spelare {current+1} vinner!")
        disable_buttons()
        return
    pool_points = 0
    update_scores()
    feedback_label.config(text=f"Spelare {current+1} sparade sina poäng.")
    disable_buttons()
    root.after(1000, switch_turn)

# Byt spelare
def switch_turn():
    global current, pool_points
    current = (current + 1) % players
    pool_points = 0
    update_scores()
    turn_label.config(text=f"Tur: Spelare {current+1}")
    pool_label.config(text="Pool: 0")
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
root.geometry("500x800")
show_menu()
root.mainloop()