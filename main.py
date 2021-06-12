"""
文字入力電卓
member:岩本,井上,岡本,宮川
GitHub URL : https://github.com/IwamotoKakeru/dentaku
ソースコードはこのmain.pyのみ
"""

from tkinter import*
from datetime import datetime


#Okamto(配列宣言)
memory={"ans":["0"],
    "formula":["0"]}
#'''

#Iwamoto(文字入力計算)
def calc():
    form=formEntry.get()    #エントリーに入力された文字列を変数formへ代入
    global ans
    global roll_count #Okamoto
    buff=eval(form) #Okamoto
    ans.set(eval(form))     #変数formをeval関数によって式として処理し，変数ansへ代入
    print(ans.get())        #デバック用にansの内容を表示
#

#'''(Okamoto)
    remember(buff,form)
    roll_count=0
#'''

#'''(miyagawa ACボタン
def ac():
    formEntry.delete(0, END)#エントリーの内容を削除
    ans.set("")             #ansを削除
#'''

#'''(inoue)
def chk_time(window, ltext):
    now=datetime.now()
    stime="{0:%H：%M %S}".format(now)
    ltext.set(stime)
    window.after(1000,lambda:chk_time(window,ltext))

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
    formEntry.delete(0,END)
    ans.set(memory["ans"][roll_count])
    formEntry.insert(END,memory["formula"][roll_count])
    #ans.set(roll_count)
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

#window 設定(Iwamoto)
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

#widget 生成(Iwamoto)
formEntry=Entry(font=20)                                            #式入力エントリーをフォントサイズ20で生成
eqalButton=Button(text="=",font=20,command=calc)                    #イコールボタンを生成
ansLabel=Label(foreground='#000000',
background='#ffffff',textvariable=ans,width=20,font=20, anchor="e") #答えラベルを生成し，変数ansを表示
#Okamoto
rollfButton=Button(text="<",font=20,command=rollback)
rollbButton=Button(text=">",font=20,command=rollforward)
#'''

#inoue
ltext = StringVar()
clockLabel=Label(foreground='#000000',
background='gray83',textvariable=ltext,font=20)
window.after(5,lambda:chk_time(window,ltext))
#'''

#'''(miyagawa)
ACbutton=Button(text="AC",font=20,command=ac)
#'''

#widget 配置(Iwamoto)
formEntry.grid(row=0,column=0,columnspan=5,sticky=(W,E))    #式入力エントリーを(0,0)に幅5で配置
eqalButton.grid(row=1,column=0,sticky=(W,E))                #イコールボタンを(1,0)に配置
ansLabel.grid(row=1,column=4,sticky=(W,E))                  #答えラベルを(1,4)に配置
#sticky=(W,E):左右に引き伸ばす
#""

#'''(miyagawa)
ACbutton.grid(row=1,column=1,sticky=(W,E))
#'''

#'''(Okamoto)
rollfButton.grid(row=1,column=2,sticky=(W,E))
rollbButton.grid(row=1,column=3,sticky=(W,E))
#'''

#inoue
clockLabel.grid(row=0,column=4,sticky=(W,E))
#'''

#Iwamoto
window.mainloop()       #ウィンドウ表示