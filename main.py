from tkinter import*

def calc():
    form=formEntry.get()
    global ans
    ans.set(eval(form))
    print(ans)

#'''(miyagawa)
def ac():
    formEntry.delete(0, END)
    ans.set("")
#'''

#window設定
window = Tk()
window.title("calculator")

#'''(miyagawa)
window.configure(background="#FFFFFF")
window.geometry("400x60+200+200")
#'''

ans = StringVar()

#widget生成
formEntry=Entry()
eqalButton=Button(text="=",command=calc)
ansLabel=Label(foreground='#000000', background='#FFFFFF',textvariable=ans)

#'''(miyagawa)
ACbutton=Button(text="AC",command=ac)
#'''

#widget配置
formEntry.grid(row=0,column=0)
eqalButton.grid(row=1,column=0)
ansLabel.grid(row=1,column=2)

#'''(miyagawa)
ACbutton.grid(row=1,column=1)
#'''

window.mainloop()