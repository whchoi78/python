from tkinter import*

def clickmouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:    
        txt += "마우스 오른쪽 버튼이 ("
    txt += str(event.x) + "," + str(event.y) + ")에서 클릭됨"
    label.configure(text=txt)

window = Tk()
window.geometry("700x500")
window.title("마우스 테스트")

label = Label(window, text="test")
window.bind("<Button>", clickmouse)
label.pack()

window.mainloop()