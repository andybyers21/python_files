# Say hello in 30 different languages

import random
import tkinter as tk

window = tk.Tk()
window.title("pynotes")
window.geometry("500x500")

# entry function


def phrase_generator():

    phrases = [
        "Hello ", "Marhaba ", "Namaska ", "Hola ", "Hafa adi ",
        "God dag ", "Hoi ", "Bonjour ", "Yasou ", "Shalom ", "Namaste ",
        "Nde-ewo ", "Salve ", "Konnichiwa ", "Salam ", "Zdravstvuyte ",
        "Anoj ", "xin chào ", "Scwmae ", "Sawubona "
    ]
    name = str(entr.get())
    return phrases[random.randint(0, 19)] + name


def phrase_display():

    greeting = phrase_generator()
    greeting_display = tk.Text(master=window, height=1, width=50)
    greeting_display.grid(column=1, row=3)

    greeting_display.insert(tk.END, greeting)


# Label
title = tk.Label(text="This is an app", font=("Monospace", 25))
title.grid(column=0, row=0)

# Entry Field
entr = tk.Entry()
entr.grid(column=1, row=1)
e_text = tk.Label(text="Please enter your name bro.")
e_text.grid(column=0, row=1)

# Button
btn = tk.Button(text="CLICK ME!", command=phrase_display)
btn.grid(column=1, row=2)

window.mainloop()
