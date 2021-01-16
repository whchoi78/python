
from tkinter import *
from tkinter import messagebox

def func():
    messagebox.showinfo("버튼 예제", "이미지 확인 하세요")
    

window = Tk()
window.title("hello") #제목


photo = PhotoImage(file = "sample.gif")
button = Button(window, image=photo, command=func) #변수 지정
button.pack()   #함수 호출




window.mainloop()