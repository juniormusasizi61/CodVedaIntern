import tkinter as tk
from tkinter import messagebox
import random

# Initialize game variables
secret_number = random.randint(1, 100)
attempts_left = 7

# Function to check the user's guess
def check_guess():
    global attempts_left, secret_number
    try:
        guess = int(entry_guess.get())
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid", "Please enter a number between 1 and 100.")
            return
        
        attempts_left -= 1

        if guess == secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed it! The number was {secret_number}.")
            reset_game()
        elif guess < secret_number:
            feedback_label.config(text=f"Too low! Attempts left: {attempts_left}")
        else:
            feedback_label.config(text=f"Too high! Attempts left: {attempts_left}")

        if attempts_left == 0 and guess != secret_number:
            messagebox.showinfo("Game Over", f"Sorry! You're out of attempts. The number was {secret_number}.")
            reset_game()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = 7
    feedback_label.config(text="Guess a number between 1 and 100")
    entry_guess.delete(0, tk.END)

# Build the UI
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")
root.config(bg="#f9f9f9")

title_label = tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
title_label.pack(pady=10)

instructions = tk.Label(root, text="Guess the number (1 - 100). You have 7 attempts!", bg="#f9f9f9", fg="#555")
instructions.pack(pady=5)

entry_guess = tk.Entry(root, width=15, font=("Arial", 12))
entry_guess.pack(pady=5)

btn_guess = tk.Button(root, text="Check Guess", command=check_guess, bg="#4CAF50", fg="white", padx=10, pady=5)
btn_guess.pack(pady=10)

feedback_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12), bg="#f9f9f9", fg="#222")
feedback_label.pack(pady=10)

btn_reset = tk.Button(root, text="Restart Game", command=reset_game, bg="#2196F3", fg="white", padx=10, pady=5)
btn_reset.pack(pady=5)

root.mainloop()
