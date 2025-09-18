import tkinter as tk
import random
import time
from threading import Thread

user_score = 0
computer_score = 0
rounds = 0
choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(choices)

# Function: Play round with instant reveal
def play(user_choice):
    global user_score, computer_score, rounds
   
    # Show "Rock...Paper...Scissors...Shoot!"
    result_label.config(text="Rock...")
    root.update()
    time.sleep(0.4)
    result_label.config(text="Paper...")
    root.update()
    time.sleep(0.4)
    result_label.config(text="Scissors...")
    root.update()
    time.sleep(0.4)
    result_label.config(text="SHOOT!")
    root.update()
    time.sleep(0.5)
   
    computer_choice = get_computer_choice()
    rounds += 1
   
    if user_choice == computer_choice:
        result = f"Tie! You both chose {user_choice}"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result = f"You Win! {user_choice} beats {computer_choice}"
    else:
        computer_score += 1
        result = f"You Lose! {computer_choice} beats {user_choice}"
   
    result_label.config(text=f"You: {user_choice} | Opponent: {computer_choice}\n{result}")
    score_label.config(text=f"Round {rounds} → You: {user_score} | Opponent: {computer_score}")

def threaded_play(choice):
    Thread(target=play, args=(choice,)).start()

def reset_game():
    global user_score, computer_score, rounds
    user_score = 0
    computer_score = 0
    rounds = 0
    result_label.config(text="Game Reset! Play again")
    score_label.config(text="Score → You: 0 | Opponent: 0")

# GUI setup
root = tk.Tk()
root.title("Codsoft Rock Paper Scissors")
root.geometry("450x450")
root.config(bg="#0505fa")

title_label = tk.Label(root, text="Codsoft Rock-Paper-Scissors", font=("Arial", 16, "bold"), bg="#D3372C", fg="white")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14, "bold"), bg="#14800a", fg="yellow")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0 | Opponent: 0", font=("Arial", 12,"bold"), bg="#F8F809", fg="red")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#0505fa")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=12, bg="tomato", fg="white", font=("Arial", 12, "bold"),
                     command=lambda: threaded_play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=12, bg="skyblue", fg="black", font=("Arial", 12, "bold"),
                      command=lambda: threaded_play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, bg="limegreen", fg="white", font=("Arial", 12, "bold"),
                         command=lambda: threaded_play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

reset_btn = tk.Button(root, text="Reset Game", width=15, bg="orange", fg="black", font=("Arial", 12, "bold"), command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()