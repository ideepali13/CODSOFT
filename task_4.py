import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock–Paper–Scissors Game")
root.geometry("400x450")
root.config(bg="#f0f0f0")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    # Update Labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

# Title Label
title = tk.Label(root, text="Rock – Paper – Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Result Labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#f0f0f0")
user_label.pack()

computer_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#f0f0f0")
computer_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()