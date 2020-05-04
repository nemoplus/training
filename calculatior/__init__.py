# -*- coding: utf-8 -*-

__version__ = "0.0.1"

import tkinter as tk

BUTTONS = [
  ['7', '8', '9', '/'],
  ['4', '5', '6', '*'],
  ['1', '2', '3', '-'],
  ['0', '.', '=', '+'],
  ['C']
]


def run():
    def make_click(ch):
        def click(e):
            if ch == '=':
                calc(0)
            elif ch == 'C':
                label["text"] = ""
                text.delete(0, tk.END)
            else:
                text.insert(tk.END, ch)
        return click

    def calc(e):
        label["text"] = '= ' + str(eval(text.get()))

    win = tk.Tk()
    text = tk.Entry(win, font=('', 20), justify="center")
    label = tk.Label(win, font=('', 20), anchor="center")

    text.pack(fill='x')
    text.bind('<Return>', calc)

    label.pack(fill='x')

    fr = tk.Frame(win)
    fr.pack()
    for y, cols in enumerate(BUTTONS):
        for x, n in enumerate(cols):
            # print(y, ", ", x, " : ", n)
            btn = tk.Button(fr, text=n, font=('', 20), width=6, height=3)
            btn.grid(row = y + 1, column = x + 1)
            btn.bind('<1>', make_click(n))

    win.title("電卓")
    win.geometry("600x800")
    win.mainloop()


if __name__ == "__main__":
    run()

