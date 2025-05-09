import tkinter as tk
from tkinter import ttk, font
import random

def setup_main():
    main = tk.Tk()
    main.title("Greed")
    main.geometry("800x600")
    main.configure(bg="#2E2E2E")
    return main

def setup_fonts():
    title_font = font.Font(family="Helvetica", size=36, weight="bold")
    button_font = font.Font(family="Helvetica", size=14)
    text_font = font.Font(family="Helvetica", size=12)
    return title_font, button_font, text_font

def setup_styles(button_font):
    style = ttk.Style()
    style.configure("TButton", 
                    font=button_font, 
                    background="#4CAF50", 
                    foreground="black",
                    padding=10)
    style.configure("TFrame", background="#2E2E2E")
    style.configure("TLabel", 
                    font=button_font, 
                    background="#2E2E2E", 
                    foreground="white")

def show_main_menu(main, title_font, button_font, text_font):
    # Clear the window
    for widget in main.winfo_children():
        widget.destroy()
    
    # Create main frame
    main_frame = ttk.Frame(main)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)
    
   

def show_manual(main, title_font, text_font):
    # Clear the window
    for widget in main.winfo_children():
        widget.destroy()
    
    # Create manual frame
    manual_frame = ttk.Frame(main)
    manual_frame.pack(expand=True, fill="both", padx=20, pady=20)
    
    # Title manual
    title_label = tk.Label(manual_frame, 
                           text="MANUAL", 
                           font=title_font, 
                           bg="#2E2E2E", 
                           fg="#2196F3")
    title_label.pack(pady=20)
    
    # Manual text
    manual_text = """
    HOW TO PLAY GREED:
    
    1. Each player takes turns rolling a die.
    2. On your turn, you can roll as many times as you want.
    3. Each roll adds to your pot (not directly to your score).
    4. You can choose to "Hold" at any time, which adds your pot to your score.
    5. If you roll a 1, you lose everything in your pot and your turn ends.
    6. First player to reach 100 points wins!
    
    CONTROLS:
    - Roll: Roll the die and add to your pot
    - Hold: Add your pot to your score and end your turn
    """
    
    manual_label = tk.Label(manual_frame, 
                            text=manual_text, 
                            font=text_font, 
                            bg="#2E2E2E", 
                            fg="white",
                            justify="left")
    manual_label.pack(pady=20)
    
   


if __name__ == "__main__":
    main = setup_main()
    title_font, button_font, text_font = setup_fonts()
    setup_styles(button_font)
    show_main_menu(main, title_font, button_font, text_font)
    main.mainloop()