from tkinter import*
from tkinter import messagebox

def open():
    messagebox.showinfo("열기","안녕하세요")
    messagebox.showinfo("열기","반가워요")
    messagebox.showinfo("열기","잘있어요")
    messagebox.showinfo("열기","다시만나요")

window = Tk()
window.geometry("700x500")
window.title("메뉴 테스트")

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu)
mainmenu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_separator()
filemenu.add_command(label="종료", command=quit)

window.mainloop()