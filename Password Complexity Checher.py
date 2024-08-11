import tkinter as tk
from tkinter import ttk
import re

def check_password_strength(event=None):
    password = entry.get()
    
    # Criteria checks
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Strength calculation
    strength = sum([length, has_upper, has_lower, has_digit, has_special])
    
    # Feedback based on strength
    if strength == 5:
        strength_feedback = "Very Strong"
    elif strength == 4:
        strength_feedback = "Strong"
    elif strength == 3:
        strength_feedback = "Medium"
    elif strength == 2:
        strength_feedback = "Weak"
    else:
        strength_feedback = "Very Weak"
    
    # Update the strength label
    strength_var.set(strength_feedback)
    
    # Update the progress bar value (each strength point is 20% of the bar)
    strength_meter['value'] = strength * 20
    
    # Update the color of the progress bar
    if strength <= 2:
        style.configure("TProgressbar", troughcolor='white', background='red')
    elif strength == 3:
        style.configure("TProgressbar", troughcolor='white', background='orange')
    else:
        style.configure("TProgressbar", troughcolor='white', background='green')
    
    # Detailed feedback
    suggestions = ""
    if not length:
        suggestions += "- Password should be at least 8 characters long.\n"
    if not has_upper:
        suggestions += "- Include at least one uppercase letter.\n"
    if not has_lower:
        suggestions += "- Include at least one lowercase letter.\n"
    if not has_digit:
        suggestions += "- Include at least one number.\n"
    if not has_special:
        suggestions += "- Include at least one special character."
    
    # Update the suggestions label
    suggestions_var.set(suggestions if suggestions else "Your password is strong!")

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_button.config(text="Show")
    else:
        entry.config(show='')
        toggle_button.config(text="Hide")

# Tkinter setup
root = tk.Tk()
root.title("Password Strength Checker")

# Resize the main window
root.geometry("450x400")

# GUI Elements
label = tk.Label(root, text="Enter a password:")
label.pack(pady=10)

# Frame to hold the entry field and the show/hide button
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, width=25, show='*')
entry.grid(row=0, column=0, padx=(0, 5))

# Bind the entry field to the key release event to check password strength as you type
entry.bind('<KeyRelease>', check_password_strength)

# Toggle password visibility button inside the entry frame
toggle_button = tk.Button(entry_frame, text="Show", command=toggle_password, width=6)
toggle_button.grid(row=0, column=1)

# Strength Frame
strength_frame = tk.LabelFrame(root, text="Strength", padx=10, pady=10)
strength_frame.pack(pady=10, fill="both", expand="yes")

strength_var = tk.StringVar()
strength_display = tk.Label(strength_frame, textvariable=strength_var, font=("Helvetica", 12, "bold"))
strength_display.pack()

# Progress bar for strength
style = ttk.Style()
style.configure("TProgressbar", troughcolor='white', background='red')
strength_meter = ttk.Progressbar(strength_frame, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
strength_meter.pack(pady=10)

# Suggestions Frame
suggestions_frame = tk.LabelFrame(root, text="Comment", padx=10, pady=10)
suggestions_frame.pack(pady=10, fill="both", expand="yes")

suggestions_var = tk.StringVar()
suggestions_display = tk.Label(suggestions_frame, textvariable=suggestions_var, wraplength=350, justify="left")
suggestions_display.pack()

# Start the GUI loop
root.mainloop()
