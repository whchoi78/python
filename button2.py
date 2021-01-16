
from tkinter import *
from tkinter import messagebox

def Func():
    if var.get() == 1:
        label.configure(text="python")
    elif var.get() == 2:
        label.configure(text="cpp")
    elif var.get() == 3:
        label.configure(text="c")
    elif var.get() == 4:
        label.configure(text="java")   
                
window = Tk()
window.title("hello") #제목

var = IntVar()
rb1 = Radiobutton(window, text="python", variable=var, value=1, command=Func)
rb2 = Radiobutton(window, text="cpp", variable=var, value=2, command=Func)
rb3 = Radiobutton(window, text="c", variable=var, value=3, command=Func)
rb4 = Radiobutton(window, text="java", variable=var, value=4, command=Func)
button = Button(window, text="종료하기", command=quit)
label = Label(window, text="선택한 언어", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
label.pack()
button.pack()

window.mainloop()

"""
def func():
    if chk.get() == 0:
        messagebox.showinfo("","꺼짐")
    else:
        messagebox.showinfo("","켜짐")    

window = Tk()
window.title("hello") #제목

chk = IntVar()
cb = Checkbutton(window, text="클릭하세요", variable=chk, command=func)
cb.pack()
"""