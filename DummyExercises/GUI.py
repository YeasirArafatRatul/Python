from tkinter import*
myGui = Tk()
myGui.title("Hellow")
myGui.geometry("500x500+1000+100")
myLabel1=Label(text='Yeasir Arafat Ratul',fg = 'red',bg='black')
myLabel2=Label(text='Student of CSE',fg = 'White',bg='black').place(x=10,y=30)
myLabel3=Label(text='Daffodil Institute of IT',fg = 'red',bg='black').place(x=100,y=100)
myLabel4=Label(text='Yeasir Arafat Ratul',fg = 'red',bg='black').grid(row=3,column=2)

myGui.mainloop()
