from tkinter import*

#Okamto(配列宣言)
memory={"ans":["0"],
        "formula":["0"]}
#'''

def calc():
    form=formEntry.get()
    global ans
    global roll_count  # Okamoto
    buff = eval(form)  # Okamoto
    ans.set(eval(form))
    print(ans.get())
#'''(Okamoto)
    remember(buff,form)
    roll_count=0
#'''

#'''(miyagawa)
def ac():
    formEntry.delete(0, END)
    ans.set("")
#'''

#'''(Okamoto)
def remember(answer,former):
    global memory
    memory["ans"].append(answer)
    memory["formula"].append(former)

def rollback():
    global memory
    global roll_count
    roll_count -= 1
    if(roll_count < 1 - len(memory["ans"])): #memory の中の"ans"の要素数
        roll_count = 0
    formEntry.delete(0, END)
    ans.set(memory["ans"][roll_count])
    formEntry.insert(END, memory["formula"][roll_count])
    # ans.set(roll_count)

def rollforward():
    global memory
    global roll_count
    roll_count += 1
    if(roll_count > 0): #memory の中の"ans"の要素数
        roll_count = 1 - len(memory["ans"])
    formEntry.delete(0,END)
    ans.set(memory["ans"][roll_count])
    formEntry.insert(END,memory["formula"][roll_count])
#'''

#window設定
window = Tk()
window.title("calculator")

#grid 設定(Okamoto)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)

#'''(miyagawa)
window.configure(background="#FFFFFF")
window.geometry("400x60+200+200")
#'''

ans = StringVar()

#widget生成
formEntry=Entry()
eqalButton=Button(text="=",command=calc)
ansLabel=Label(foreground='#000000', background='#FFFFFF',textvariable=ans)
#Okamoto
rollfButton=Button(text="<",font=20,command=rollback)
rollbButton=Button(text=">",font=20,command=rollforward)
#'''
#'''(miyagawa)
ACbutton=Button(text="AC",command=ac)
#'''

#widget 配置
formEntry.grid(row=0,column=0,columnspan=5,sticky=(W,E))
eqalButton.grid(row=1,column=0,sticky=(W,E))
ansLabel.grid(row=1,column=4,sticky=(W,E))
#'''(miyagawa)
ACbutton.grid(row=1,column=1,sticky=(W,E))
#'''
#'''(Okamoto)
rollfButton.grid(row=1,column=2,sticky=(W,E))
rollbButton.grid(row=1,column=3,sticky=(W,E))
#'''
window.mainloop()