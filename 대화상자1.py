from tkinter import*
#from tkinter.simpledialog import*
from tkinter.filedialog import *

window = Tk()
window.geometry("700x500")
window.title("대화상자 테스트")

label = Label(window, text="test")
label.pack()

filename = askopenfilename(parent=window, filetype=(("GIF파일", "*.gif"), ("모든파일","*.*")))
label.configure(text=str(filename))

window.mainloop()

'''
label = Label(window, text="test")
label.pack()

value = askinteger("주사위 게임","숫자를 입력하세요(1-6).",minvalue=1, maxvalue=6)
#askstring, askfloat
label.configure(text=str(value))
'''
