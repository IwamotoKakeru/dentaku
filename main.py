from tkinter import*

def calc():
    form=formEntry.get()
    global ans
    ans.set(eval(form))
    print(ans)

#window設定
window = Tk()
window.title("calculator")

ans = StringVar()

#widget生成
formEntry=Entry()
eqalButton=Button(text="=",command=calc)
ansLabel=Label(foreground='#000000', background='#FFFFFF',textvariable=ans)

#widget配置
formEntry.grid(row=0,column=0)
eqalButton.grid(row=1,column=0)
ansLabel.grid(row=1,column=1)

window.mainloop()
