import tkinter as tk
from tkinter import messagebox
import random

# Game data
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 5

# Game logic
def play(user_choice):
    global user_score, computer_score, rounds_played

    if rounds_played >= max_rounds:
        messagebox.showinfo("Game Over", "🎉 Game Over! Click 'Reset Scores' to play again.")
        return

    rounds_played += 1
    comp_choice = random.choice(choices)

    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice.capitalize()}")

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "scissors" and comp_choice == "paper") or
        (user_choice == "paper" and comp_choice == "rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(
        text=f"Score - You: {user_score} | Computer: {computer_score} | Round: {rounds_played}/{max_rounds}"
    )

    # Disable choice buttons until next round
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")
    next_btn.config(state="normal")

# Next round reset
def next_round():
    user_choice_label.config(text="You chose:")
    comp_choice_label.config(text="Computer chose:")
    result_label.config(text="")

    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")
    next_btn.config(state="disabled")

# Reset everything
def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0

    user_choice_label.config(text="You chose:")
    comp_choice_label.config(text="Computer chose:")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0 | Round: 0/5")

    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")
    next_btn.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#e3f2fd")

# Title
tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 16, "bold"), bg="#e3f2fd").pack(pady=10)

# Choices display
user_choice_label = tk.Label(root, text="You chose:", font=("Arial", 12), bg="#e3f2fd")
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer chose:", font=("Arial", 12), bg="#e3f2fd")
comp_choice_label.pack()

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#e3f2fd")
result_label.pack(pady=10)

# Score
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0 | Round: 0/5", font=("Arial", 12), bg="#e3f2fd")
score_label.pack(pady=5)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=12, font=("Arial", 12), command=lambda: play("rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=12, font=("Arial", 12), command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=12, font=("Arial", 12), command=lambda: play("scissors"))
scissors_btn.pack(pady=5)

# Reset and Next buttons
tk.Button(root, text="Reset Scores", font=("Arial", 11), bg="#f44336", fg="white", command=reset_game).pack(pady=5)

next_btn = tk.Button(root, text="Next Round", font=("Arial", 11), bg="#9c27b0", fg="white", command=next_round, state="disabled")
next_btn.pack(pady=5)

# Run the app
root.mainloop()
