# Tic Tac Toe Game using Tkinter

from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")
btnclick = True
btnc = 0

def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)



def btnClick(bs):
    global btnclick, btnc
    if bs["text"] == " " and btnclick == True:
        bs["text"] = "X"
        btnclick = False
        check()
        btnc += 1


    elif bs["text"] == " " and btnclick == False:
        bs["text"] = "O"
        btnclick = True
        check()
        btnc += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def check():
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
        b7['text'] =='X' and b8['text'] == 'X' and b9['text'] == 'X' or
        b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
        b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
        b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
        b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
        b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
        b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "X wins!")

    elif(btnc == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "O wins!")


bs = StringVar()
b1 = Button(tk, text=" ", font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b1))
b1.grid(row=3, column=0)

b2 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b2))
b2.grid(row=3, column=1)

b3 = Button(tk, text=' ',font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b3))
b3.grid(row=3, column=2)

b4 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b4))
b4.grid(row=4, column=0)

b5 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b5))
b5.grid(row=4, column=1)

b6 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b6))
b6.grid(row=4, column=2)

b7 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b7))
b7.grid(row=5, column=0)

b8 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b8))
b8.grid(row=5, column=1)

b9 = Button(tk, text=' ', font='Times 16', bg='white', fg='red', height=4, width=8, command=lambda: btnClick(b9))
b9.grid(row=5, column=2)

tk.mainloop()
