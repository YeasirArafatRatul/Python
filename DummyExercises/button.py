from tkinter import*
import tkinter.messagebox

myGui = Tk()
newWin = Tk()
def hello():
    b = to.get()
    myLabel2 = Label(newWin,text= b,fg ='red',bg = 'black').pack()
def newfile():
    myLabel3 = Label(myGui,text= 'New File Created',fg ='Black',bg = 'White').pack()
def msgB():
    tkinter.messagebox.showinfo(title ='SAVE',message ='Are you Sure?')
def Quit():
    check=tkinter.messagebox.askyesno(title ='Quit',message ='Are you Sure?')
    if check == 1:
        myGui.destroy()
        newWin.destroy()

to = StringVar()




myGui.title("Start")
newWin.title("Hello")

myGui.geometry("500x500+100+50")
newWin.geometry("500x500+600+50")

myLabel1 = Label(text='label one',fg ='red',bg = 'black').pack()

text = Entry(textvariable = to).pack()
myButton1 = Button(text ='enter',font = 20,command = hello).pack()
mymenu = Menu(myGui)
listone = Menu()
listone.add_command(label = 'New File',command =newfile)
listone.add_command(label = 'Save File',command = msgB)
listone.add_command(label = 'Open File')
listone.add_command(label = 'Quit',command = Quit)


listtwo = Menu()
listtwo.add_command(label = 'With Photoshop')
listtwo.add_command(label = 'With Picasa')
listtwo.add_command(label = 'With Illustrator')

mymenu.add_cascade(label ='File',menu=listone)
mymenu.add_cascade(label ='Edit',menu = listtwo)
mymenu.add_cascade(label ='Options')
mymenu.add_cascade(label ='Delete')

myGui.config(menu=mymenu)


