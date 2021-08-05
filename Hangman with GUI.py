import tkinter as tk
import tkinter.messagebox
import random
from file import words, tips
import string


def get_valid_word():
    global word
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def btn_click(*args):
    global is_running, to_be_guessed, alphabet, guessed, word
    if not is_running:
        tkinter.messagebox.showinfo("Game Haven't Started Yet", "Press \"play\" to start the game.")
        return 0
    user_letter = txt.get("1.0", "end-1c").upper()
    user_letter = user_letter.rstrip()
    txt.delete("1.0", "end")
    if user_letter in alphabet - set(guessed):
        guessed.append(user_letter)
        guessed.sort()
        if user_letter in to_be_guessed:
            title3.config(text=f"Yes, {user_letter} is in the word.", fg="green")
            to_be_guessed.remove(user_letter)
        else:
            title3.config(text=f"No, {user_letter} is not in the word.", fg="red")
    elif user_letter in guessed:
        title3.config(text=f"You have already guessed {user_letter}. Try again.", fg="red")
    else:
        title3.config(text=f"{user_letter}is an Invalid input. Try again.", fg="red")
    current_word = [letter if letter in guessed else '-' for letter in word]
    title2.config(text=' '.join(current_word))
    if len(to_be_guessed) == 0:
        tkinter.messagebox.showinfo("Congrats", "Congrats! You have guessed the word: " + word)

    # show former guesses
    title4.config(text="USED LETTERS:" + ' '.join(guessed))
    # show current word
    current_word = [letter if letter in guessed else '-' for letter in word]
    title2.config(text=' '.join(current_word))


def start_game():
    global is_running, to_be_guessed, alphabet, guessed, word
    word = get_valid_word()
    is_running = True
    to_be_guessed = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = []
    current_word = [letter if letter in guessed else '-' for letter in word]
    title2.config(text=' '.join(current_word))


root = tk.Tk()
root.bind('<Return>', btn_click)
word = ''
is_running = False
to_be_guessed = set()
alphabet = set(string.ascii_uppercase)
guessed = []

canvas = tk.Canvas(root, height=500, width=800, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

title1 = tk.Label(frame, text="CURRENT WORD", font=("Arial", 25), fg="white", bg="#263D42")
title1.place(relx=0.5, rely=0.15, anchor="center")
title2 = tk.Label(frame, text="- - - - -", font=("Arial", 40))
title2.place(relx=0.5, rely=0.3, anchor="center")
title3 = tk.Label(frame, text="BLAH BLAH BLAH", font=("Arial", 10))
title3.place(relx=0.5, rely=0.45, anchor="center")
title4 = tk.Label(frame, text="USED LETTERS:", font=("Arial", 10))
title4.place(relx=0.5, rely=0.50, anchor="center")
tip_txt = random.choice(tips)
tip = tk.Label(root, text="TIPS: " + tip_txt, font=("Arial", 10))
tip.pack()

txt = tk.Text(frame, font=("Arial", 30), height=1, width=2)
txt.place(relx=0.5, rely=0.65, anchor="center")
btn = tk.Button(frame, text="SUBMIT", command=btn_click)
btn.place(relx=0.5, rely=0.8, anchor="center")

start_game()
root.mainloop()
