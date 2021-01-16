from tkinter import *

window = Tk()
window.title("hello") #제목

"""           
window.geometry("400x100")      #크기 지정
window.resizable(width=True, height=True) #변환 가능 여부


label1 = Label(window, text="good morning")
label2 = Label(window, text="good afternoon", font=("궁서체",30), fg="blue")
label3 = Label(window, text="good afternoon", bg="blue", width=20, height=5, anchor=SE)
label1.pack()
label2.pack()
label3.pack()
"""

photo = PhotoImage(file = "sample.gif")
lable = Label(window, image=photo)
lable.pack()

window.mainloop()