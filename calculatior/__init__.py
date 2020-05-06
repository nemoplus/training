# -*- coding: utf-8 -*-

__version__ = "0.0.1"

import tkinter as tk

BUTTONS = [
    ['%', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', 'C'],
]



def run():
    def make_click(ch:str):
        def click(e):
            if ch == '=':
                calc(e)
            elif ch == 'C':
                label["text"] = ""
                text.delete(0, tk.END)
            else:
                text.insert(tk.END, ch)
        return click

    def calc(e):
        try:
            label["text"] = '= ' + str(eval(text.get()))
        except Exception as err:
            label["text"] = err

    win = tk.Tk()
    win.title("電卓")

    text  = tk.Entry(win, font=('', 20), justify="center")
    text.pack(fill='x')
    text.bind('<Return>', calc)

    label = tk.Label(win, font=('', 20), anchor="center")
    label.pack(fill='x')

    fr = tk.Frame(win)
    fr.pack()
    count_y = 0
    count_x = 0
    for y, cols in enumerate(BUTTONS):
        count_tmp = 0
        for x, n in enumerate(cols):
            count_tmp += 1
            btn = tk.Button(fr, text=n, font=('', 20), width=6, height=3)
            btn.grid(row = y + 1, column = x + 1)
            btn.bind('<1>', make_click(n))
        count_y += 1
        if count_x < count_tmp:
            count_x = count_tmp

    win.geometry(str( count_x * 100) + "x" + str(count_y * 120))
    win.mainloop()


if __name__ == "__main__":
    run()

