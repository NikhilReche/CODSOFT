from tkinter import *

THEME_COLOR = "#313631"
FONT_NAME = "Courier"


def press(x):
    input_entry.insert(END, str(x))


def clear():
    input_entry.delete(0, END)


def evaluate():
    try:
        input_expression = input_entry.get()
        output = eval(input_expression)
        input_entry.delete(0, END)
        input_entry.insert(0, f"{output:.2f}")
    except (SyntaxError, ZeroDivisionError):
        input_entry.delete(0, END)
        input_entry.insert(0, "WRONG ENTRY")



def evaluate_on_enter(event):
    evaluate()


window = Tk()

input_entry = Entry(font=(FONT_NAME, 25))
input_entry.focus_set()
input_entry.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

b0 = Button(text="0", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(0))
b0.grid(row=4, column=0, pady=15)
b0.configure(bg="#f0f097")


b1 = Button(text="1", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(1))
b1.grid(row=3, column=0, pady=15 )
b1.configure(bg="#f0f097")


b2 = Button(text="2", height=1,width=2, font=(FONT_NAME, 25), command=lambda: press(2))
b2.grid(row=3, column=1, pady=15,)
b2.configure(bg="#f0f097")


b3 = Button(text="3", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(3))
b3.grid(row=3, column=2, pady=15)
b3.configure(bg="#f0f097")


b4 = Button(text="4", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(4))
b4.grid(row=2, column=0, pady=15)
b4.configure(bg="#f0f097")


b5 = Button(text="5", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(5))
b5.grid(row=2, column=1, pady=15)
b5.configure(bg="#f0f097")


b6 = Button(text="6", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(6))
b6.grid(row=2, column=2, pady=15)
b6.configure(bg="#f0f097")


b7 = Button(text="7", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(7))
b7.grid(row=1, column=0, pady=15)
b7.configure(bg="#f0f097")


b8 = Button(text="8", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(8))
b8.grid(row=1, column=1, pady=15)
b8.configure(bg="#f0f097")


b9 = Button(text="9", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press(9))
b9.grid(row=1, column=2, pady=15)
b9.configure(bg="#f0f097")


clear_btn = Button(text="CLEAR", height=1, width=18, font=(FONT_NAME, 25), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=15)
clear_btn.configure(bg="#f7615e")


divide = Button(text="/", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("/"))
divide.grid(row=1, column=3)
divide.configure(bg="#f0f097")


multiply = Button(text="*", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("*"))
multiply.grid(row=2, column=3)
multiply.configure(bg="#f0f097")


addition = Button(text="+", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("+"))
addition.grid(row=3, column=3)
addition.configure(bg="#f0f097")


subtract = Button(text="-", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("-"))
subtract.grid(row=4, column=3)
subtract.configure(bg="#f0f097")


equal = Button(text="=", height=1, width=2, font=(FONT_NAME, 25), command=evaluate)
equal.grid(row=4, column=2)
equal.configure(bg="#66fa7a")


point= Button(text=".", height=1, width=2, font=(FONT_NAME, 25), command=lambda: press("."))
point.grid(row=4, column=1)
point.configure(bg="#f0f097")


window.bind("<Return>", evaluate_on_enter)

window.title("CALCULATOR")
window.config(padx=20, pady=20, bg=THEME_COLOR)
window.geometry("+575+125")
window.minsize(width=325, height=500)
window.resizable(False, False)
window.mainloop()