from tkinter import*
from tkinter.filedialog import *

window = Tk()
window.geometry("700x500")
window.title("대화상자 테스트")


label = Label(window, text="test")
label.pack()

save = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetype=(("GIF파일", "*.gif"), ("모든파일","*.*")))
label.configure(text=save)
save.close()

window.mainloop()