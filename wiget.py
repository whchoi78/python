from tkinter import*

window = Tk()
window.title("hello")
"""
bt1 = Button(window, text="버튼1")
bt2 = Button(window, text="버튼2")
bt3 = Button(window, text="버튼3")

bt1.pack(side=LEFT) #LEFT, TOP, BOTTON
bt2.pack(side=LEFT)
bt3.pack(side=LEFT)
"""

bt = [0,0,0]
for i in range(3):
    bt[i] = Button(window, text="버튼"+str(i+1))
    bt[i].place(x=10, y=10, width=50, height=50) #pack함수쪽에다 일일이 하기 귀찮으면 미리 place함수에 담아서 필요할때 꺼냄
    bt[i].pack()
   # bt[i].pack(side=TOP, fill=X, padx=10, pady=10, ipadx=10, ipady=10) #fill은 채우기 padx는 가로 여백 pady는 세로 여백 ipad는 버튼 안 여백
    #place(x=x좌표, y=y좌표, width=폭, hegiht=높이)
    
window.mainloop()