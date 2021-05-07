# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

from OR.module import Graph, Drawing

root = Tk()
root.title("Network App")
root.geometry("260x230")

inputFrame = LabelFrame(root, text="Input Field")
inputFrame.grid(row=0, column=0, ipadx=10, ipady=5, columnspan=4)

menuFrame = LabelFrame(root)
menuFrame.grid(row=1, column=0, columnspan=4)

a_Label = Label(inputFrame, text="a =")
b_Label = Label(inputFrame, text="b =")
c_Label = Label(inputFrame, text="c =")
d_Label = Label(inputFrame, text="d =")

a_Label.grid(row=0, column=0)
b_Label.grid(row=0, column=2)
c_Label.grid(row=0, column=4)
d_Label.grid(row=0, column=6)

a_Entry = Entry(inputFrame, width=4)
b_Entry = Entry(inputFrame, width=4)
c_Entry = Entry(inputFrame, width=4)
d_Entry = Entry(inputFrame, width=4)

a_Entry.grid(row=0, column=1, padx=3)
b_Entry.grid(row=0, column=3, padx=3)
c_Entry.grid(row=0, column=5, padx=3)
d_Entry.grid(row=0, column=7, padx=3)

# def create_func():
#     g = Graph(12,23,43,12)
# def draw_func():
#     if g is not None:
#         g.drawing.draw_graph()
g = Graph(1, 2, 3, 4)


# g.draw()
def create_func():
    g.drawing.close()

    # Обработать исключение здесь
    try:
        a = int(a_Entry.get())
        b = int(b_Entry.get())
        c = int(c_Entry.get())
        d = int(d_Entry.get())
    except ValueError:
        return messagebox.showerror("Ошибка", "Пустые ячейки!")
    g.__init__(a, b, c, d)
    # g.__reduce__()

    dfsButton.configure(state=NORMAL)
    showButton.configure(state=NORMAL)
    drawButton.configure(state=NORMAL)


def draw_func():
    g.drawing.close()
    g.draw()


def dfs_func():
    # Установить возможность выбора начального узла
    g.drawing.close()
    # dfsButton.configure(relief=RIDGE)
    g.depth_first_search(spin_var.get(), draw_mode=True, pause_set=1)
    # dfsButton.configure(relief=GROOVE)


def print_func():
    # Установить вохможность выбора вывода(3) и сделать виджет для вывода информации
    choice = r.get()
    if choice == 1:
        g.print_edge_list()
    elif choice == 2:
        g.print_adjacency_list()
    elif choice == 3:
        g.print_adjacency_matrix()
    else:
        raise AssertionError


def error_func():
    g.__reduce__()


setButton = Button(menuFrame, text="Set", width=34, command=create_func, overrelief=GROOVE)
drawButton = Button(menuFrame, text="Draw", width=34, command=draw_func, state=DISABLED, overrelief=GROOVE)
showButton = Button(menuFrame, text="Print", width=34, command=print_func, state=DISABLED, overrelief=GROOVE)
dfsButton = Button(menuFrame, text="Depth First Search", width=34, command=dfs_func, state=DISABLED, overrelief=GROOVE)

setButton.grid(row=0, column=0, columnspan=3)
drawButton.grid(row=1, column=0, columnspan=3)
showButton.grid(row=2, column=0, columnspan=3)
dfsButton.grid(row=4, column=0, columnspan=3)

# Добавить close кнопку
closeButton = Button(menuFrame, text="Exit", width=34, state=NORMAL, command=sys.exit, overrelief=GROOVE)
closeButton.grid(row=6, column=0, columnspan=3)

r = IntVar()
r.set(1)

radioButton1 = Radiobutton(menuFrame, text="Option 1", variable=r, value=1)
radioButton2 = Radiobutton(menuFrame, text="Option 2", variable=r, value=2)
radioButton3 = Radiobutton(menuFrame, text="Option 3", variable=r, value=3)

radioButton1.grid(row=3, columnspan=1, column=0)
radioButton2.grid(row=3, columnspan=1, column=1)
radioButton3.grid(row=3, columnspan=1, column=2)
spin_var = IntVar()
spin = Spinbox(menuFrame, from_=0, to=g.n, width=5, textvariable=spin_var)
spinLabel = Label(menuFrame, text="Start node:")
spinLabel.grid(row=5, columnspan=1, column=0)
spin.grid(row=5, columnspan=1, column=1)
# txtFrame = LabelFrame(root,"Out").grid(row=0,column=1)
# txt = Message(txtFrame,text="Suck").grid(row=0,column=0)
# e = Entry(root,width=35,borderwidth=5)
# e.grid(row=0,column=0,columnspan=3)


# clicked = StringVar()
# drop = OptionMenu(root,clicked,"Start","Settings","Exit")
# drop.pack()
# myButton.pack()
root.mainloop()
