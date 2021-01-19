from tkinter import*
from tkinter import messagebox

def keyevent(event):
    messagebox.showinfo("", chr(event.keycode))

window = Tk()
window.geometry("700x500")
window.title("키보드테스트")

window.bind("<Return>", keyevent)

window.mainloop()