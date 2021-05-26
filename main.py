from tkinter import*

def calc():
    form=formEntry.get()
    global ans
    ans = eval(form)
    print(ans)

#window設定
window = Tk()
window.title("calculator")

ans = '0'

#widget生成
formEntry=Entry()
eqalButton=Button(text="=",command=calc)
ansLabel=Label(foreground='#FFFFFF', background='#48D1CC',textvariable=ans)

#widget配置
formEntry.grid(row=0,column=0)
eqalButton.grid(row=1,column=0)
ansLabel.grid(row=1,column=1)

window.mainloop()
