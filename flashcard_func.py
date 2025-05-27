import json
import random
import tkinter as tk

current_index = 0
deck = []

correct_score = 0
seen_cards = -1


def load_deck(filename="projects_save/flashcard_app/data.json"):
    """Loads data from the JSON file"""
    global deck
    try:
        with open(filename, "r") as file:
            deck = json.load(file)
        random.shuffle(deck)
        return deck
    except FileNotFoundError:
        print("Data file not found. Creating new one...")
        deck = []
        save_deck(deck)


def save_deck(deck, filename="projects_save/flashcard_app/data.json"):
    """Saves data to the JSON file"""
    try:
        with open(filename, "w") as file:
            json.dump(deck, file, indent=2)
    except FileNotFoundError:
        print("Data file not found. Creating new one...")
        deck = []
        save_deck(deck)



def get_current_card():
    """Returns the current flashcard"""
    return deck[current_index]


def next_card(app):
    """Controls the next button functions"""
    global current_index, seen_cards

    if not deck:
        app.canvas.itemconfigure(app.card_text, text="No cards in deck.")
        app.status_label.config(text="Add some cards to begin.", fg="red")
        app.entry.delete(0, "end")
        app.score_label.config(text="0/0")
        return

    seen_cards += 1
    current_index = (current_index + 1) % len(deck)
    card = get_current_card()

    app.canvas.itemconfigure(app.card_text, text=card["question"])
    app.status_label.config(text="What is the answer?", fg="black")
    app.entry.delete(0, "end")
    app.score_label.config(text=f"{correct_score}/{seen_cards}")
    app.answer_btn.config(state=tk.NORMAL)

def answer_card(app):
    """Controls the answer button functions"""
    user_input = app.entry.get().strip().lower()
    correct_answer = get_current_card()["answer"].strip().lower()
    if not app.entry.get():
        app.status_label.config(text="Answer entry empty!", fg="red")
    else:
        app.answer_btn.config(state=tk.DISABLED)
        if user_input == correct_answer:
            global correct_score
            correct_score += 1
            app.status_label.config(text="Correct!", fg="green")
        else:
            app.status_label.config(text=f"Incorrect. | Correct: {correct_answer}", fg="red")

    app.entry.delete(0, 'end')


def hint_card(app):
    """Updates label with a hint"""
    current_hint = get_current_card()["hint"]
    app.status_label.config(text=f"Hint: {current_hint}", fg="orange")


def question_display(app):
    """Updates question display label"""
    return get_current_card()["question"]


def open_new_card_window(self):
    """Opens a window to input new flashcards"""
    new_win = tk.Toplevel(self.root)
    new_win.title("Add New Flashcard")
    new_win.geometry("300x250")

    # Labels & Entries
    tk.Label(new_win, text="Question:").pack()
    question_entry = tk.Entry(new_win, width=40)
    question_entry.pack()

    tk.Label(new_win, text="Answer:").pack()
    answer_entry = tk.Entry(new_win, width=40)
    answer_entry.pack()

    tk.Label(new_win, text="Hint (optional):").pack()
    hint_entry = tk.Entry(new_win, width=40)
    hint_entry.pack()

    def save_new_card():
        question = question_entry.get().strip()
        answer = answer_entry.get().strip()
        hint = hint_entry.get().strip()

        if not question or not answer:
            tk.Label(new_win, text="Question and Answer are required.", fg="red").pack()
            return

        new_card = {"question": question, "answer": answer, "hint": hint}
        deck.append(new_card)
        save_deck(deck)

        new_win.destroy()
        self.status_label.config(text="New card added!", fg="blue")

    tk.Button(
        new_win,
        text="Save Card",
        bg="green",
        fg="white",
        command=save_new_card
    ).pack(pady=10)
