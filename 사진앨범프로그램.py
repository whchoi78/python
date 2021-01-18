from tkinter import*
import time

#전역변수
fnameList = ["sample.gif","sample2.gif","sample3.gif","sample4.gif","sample5.gif","sample6.gif"]
num = 0

#함수 선언
def clickNext():
    global num 
    num +=1
    if num > 5:
        num = 0
    Photo = PhotoImage(file=fnameList[num])
    plable.configure(image=Photo)
    plable.image = Photo

def clickPrev():
    global num 
    num -=1
    if num < 0:
        num = 5
    Photo = PhotoImage(file=fnameList[num])
    plable.configure(image=Photo)
    plable.image = Photo

#메인
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="이전", command=clickPrev)
btnNext = Button(window, text="다음", command=clickNext)

Photo = PhotoImage(file=fnameList[0])
plable = Label(window, image=Photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=300, y=10)
plable.place(x=15, y=50)

window.mainloop()