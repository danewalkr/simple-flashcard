'''| 📓 **Flashcard App** (Terminal or GUI) 
| File storage, repetition logic, saving progress |

At the end make chatgpt test how good this is for a resume and 
change the readme etc to suggest changes
'''
# app.py
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from flashcard_func import (
    open_new_card_window,
    load_deck,
    save_deck,
    answer_card,
    next_card,
    hint_card,
    question_display
)

load_deck()

class RunApp:
    def __init__(self):
        self.root = tb.Window(themename="cosmo")
        self.root.title("Flashcard App V1")
        self.root.geometry("500x500")

        # Main Frame
        self.main_frame = tb.Frame(self.root, padding=20)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Card Canvas (matches flashcard.py's canvas/card_text)
        self.canvas = tk.Canvas(self.main_frame, width=400, height=100)
        self.canvas.pack(pady=10)
        self.card_text = self.canvas.create_text(200, 50, text="", font=("Segoe UI", 16, "bold"), width=380)

        # Status Label
        self.status_label = tk.Label(self.main_frame, text="What is the answer?", font=("Segoe UI", 12))
        self.status_label.pack(pady=(20, 5))

        # Score Label
        self.score_label = tk.Label(self.main_frame, text="0/0", font=("Segoe UI", 11, "italic"))
        self.score_label.pack()

        # Answer Entry
        self.entry = tb.Entry(self.main_frame, font=("Segoe UI", 12), width=40)
        self.entry.bind("<Return>", lambda e: answer_card(self))
        self.entry.pack(pady=10)

        # Buttons Frame
        self.button_frame = tb.Frame(self.main_frame)
        self.button_frame.pack(pady=15)

        # Buttons
        self.answer_btn = tb.Button(self.button_frame, text="Answer", bootstyle="success", command=lambda: answer_card(self))
        self.answer_btn.pack(side=LEFT, padx=5)

        self.next_btn = tb.Button(self.button_frame, text="Next", bootstyle="warning", command=lambda: next_card(self))
        self.next_btn.pack(side=LEFT, padx=5)

        self.hint_btn = tb.Button(self.button_frame, text="Hint", bootstyle="info", command=lambda: hint_card(self))
        self.hint_btn.pack(side=LEFT, padx=5)

        self.new_card_btn = tb.Button(self.button_frame, text="Add Card", bootstyle="purple", command=lambda: open_new_card_window(self))
        self.new_card_btn.pack(side=LEFT, padx=5)

        # Show first card
        next_card(self)

    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    RunApp().main()
