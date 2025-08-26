import tkinter as tk
from tkinter import filedialog, messagebox

# Function to count words in a file
def count_words_in_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please choose a valid file.")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

# Function to browse and count words
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            word_count = count_words_in_file(file_path)
            result_label.config(text=f"File: {file_path}\nWord Count: {word_count}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("📖 Word Counter")
root.geometry("450x250")
root.config(bg="#f9f9f9")

title_label = tk.Label(root, text="📖 Word Counter", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
title_label.pack(pady=15)

instructions = tk.Label(root, text="Select a .txt file to count the words inside.", bg="#f9f9f9", fg="#555")
instructions.pack(pady=5)

browse_button = tk.Button(root, text="Browse File", command=browse_file, bg="#4CAF50", fg="white", padx=10, pady=5)
browse_button.pack(pady=15)

result_label = tk.Label(root, text="No file selected.", font=("Arial", 12), bg="#f9f9f9", fg="#222", wraplength=400, justify="center")
result_label.pack(pady=10)

root.mainloop()
