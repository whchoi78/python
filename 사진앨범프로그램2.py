from tkinter import*
from tkinter.filedialog import *

def open():
    filename = askopenfilename(parent=window, filetype=(("GIF파일","*.gif"), ("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    label.configure(image=photo)
    label.image_names = photo

def exit():
    window.quit()
    window.destroy()    

window = Tk()
window.geometry("700x500")
window.title("사진앨범 테스트")

photo = PhotoImage()
label = Label(window, image=photo)
label.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu)
mainmenu.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=open)
filemenu.add_separator()
filemenu.add_command(label="종료", command=exit)

window.mainloop()