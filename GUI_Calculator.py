from tkinter import *

exp = ""


def click(n):
    global exp
    exp = exp + str(n)
    enter.set(exp)


def calc():
    global exp
    result = str(eval(exp))
    enter.set(result)
    exp = result


def clear():
    global exp
    exp = ""
    enter.set(exp)


root = Tk()


root.geometry("500x150")
root.title("My Python Calculator")

enter = StringVar()
entry = Entry(root, textvariable=enter)
entry.grid(columnspan=4, ipadx=186)
button1 = Button(root, text="1", width=1, height=1, command=lambda: click(1))
button1.grid(row=1, column=0, sticky="nsew")
button2 = Button(root, text="2", width=1, height=1, command=lambda: click(2))
button2.grid(row=1, column=1, sticky="nsew")
button3 = Button(root, text="3", width=1, height=1, command=lambda: click(3))
button3.grid(row=1, column=2, sticky="nsew")
button4 = Button(root, text="4", width=1, height=1, command=lambda: click(4))
button4.grid(row=2, column=0, sticky="nsew")
button5 = Button(root, text="5", width=1, height=1, command=lambda: click(5))
button5.grid(row=2, column=1, sticky="nsew")
button6 = Button(root, text="6", width=1, height=1, command=lambda: click(6))
button6.grid(row=2, column=2, sticky="nsew")
button7 = Button(root, text="7", width=1, height=1, command=lambda: click(7))
button7.grid(row=3, column=0, sticky="nsew")
button8 = Button(root, text="8", width=1, height=1, command=lambda: click(8))
button8.grid(row=3, column=1, sticky="nsew")
button9 = Button(root, text="9", width=1, height=1, command=lambda: click(9))
button9.grid(row=3, column=2, sticky="nsew")
button0 = Button(root, text="0", width=1, height=1, command=lambda: click(0))
button0.grid(row=4, column=0, sticky="nsew")
buttonClear = Button(root, text="cls", width=1, height=1, command=clear)
buttonClear.grid(row=1, column=3, sticky="nsew")
buttonSubtract = Button(root, text="-", width=1, height=1, command=lambda: click("-"))
buttonSubtract.grid(row=2, column=3, sticky="nsew")
buttonDiv = Button(root, text="/", width=1, height=1, command=lambda: click("/"))
buttonDiv.grid(row=3, column=3, sticky="nsew")
buttonEqual = Button(root, text="=", width=1, height=1, command=calc)
buttonEqual.grid(row=4, column=3, sticky="nsew")
buttonAdd = Button(root, text="+", width=1, height=1, command=lambda: click("+"))
buttonAdd.grid(row=4, column=1, sticky="nsew")
buttonProduct = Button(root, text="*", width=1, height=1, command=lambda: click("*"))
buttonProduct.grid(row=4, column=2, sticky="nsew")
root.mainloop()
