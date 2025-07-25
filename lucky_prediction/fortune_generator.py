import tkinter as tk
import random

predictions=["One day you’ll understand everything. But not today.",
             'Chaos suits you. Own it.',
             'No plan? Perfect. Do it freestyle.',
             'Fortune is hiding in your second sock.',
             'Time is fake. You’re not late.',
             'You will make a choice that rewires your path.',
             'A window will open where you expected a wall.',
             'Something tiny will make you wildly happy.']

def get_fortune():
    selected=random.choice(predictions)
    fortune_label.config(text=selected)

window=tk.Tk()
window.title("Fortune generator")
window.geometry("500x400")
window.config(bg='#768258')
title_label = tk.Label(window,
                 text="Your fortune for today:",
                 font=('Courier', 16, 'normal'),
                 bg='#768258',
                 fg='black')
title_label.pack(padx = 30, pady = 30)

fortune_button = tk.Button(window,
                           text = 'Get predictions',
                           font = ('Courier', 14, 'normal'),
                           bg = "#C5B93F",
                           fg = 'black',
                           padx = 10,
                           pady = 10,
                           command = get_fortune,
                           cursor = 'hand2',
                           activebackground = "#C78015"
)
fortune_button.pack(pady = 30)

fortune_label = tk.Label(window,
                         text='',
                         font=('Courier', 14, 'normal'),
                         bg = '#768258',
                         fg = 'black',
                         wraplength=350)
fortune_label.pack(pady=30, padx=30, fill='x')


tk.mainloop()