from tkinter import*
from tkinter import messagebox

def clickimage(event):
    messagebox.showinfo("마우스","왼쪽")

window = Tk()
window.geometry("700x500")
window.title("마우스 테스트")

#window.bind("<Button-1>", clickLeft)
photo = PhotoImage(file="sample.gif")
label = Label(window, image=photo)
label.bind("<Button-1>",clickimage)
label.pack()
window.mainloop()