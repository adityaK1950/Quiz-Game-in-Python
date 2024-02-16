import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])
    for i in range(4):
        choice_btns[i].config(text=question["choices"][i], state="normal")
    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text=f"Score: {score}/{len(quiz_data)}", foreground="green")
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Quiz Completed! Final Score: {score}/{len(quiz_data)}")
        root.destroy()

root = tk.Tk()
root.title("Quiz Application")
root.geometry("600x600")
style = Style(theme="minty")

style.configure("TLabel", font=("Helvetica", 24), padding=10)
style.configure("TButton", font=("Helvetica", 20), padding=5)

qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i),
        padding=5
    )
    button.pack(pady=5, padx=10)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor="center",
)
feedback_label.pack(pady=10)

score = 0

score_label = ttk.Label(
    root,
    text=f"Score: {score}/{len(quiz_data)}",
    anchor="center",
)
score_label.pack(pady=10)

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

current_question = 0
show_question()
root.mainloop()
