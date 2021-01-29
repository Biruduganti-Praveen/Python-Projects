# Made by Biruduganti Praveen
from tkinter import *


# from tkinter import ttk
# from PIL import Image
import math
cal =Tk()
cal.title("Calculator Created By Praveen")
operator=''
text_input=StringVar()
txtdisplay=Entry(cal, font=('arial',20,'bold'), textvariable=text_input,bd=9,width=23,bg='light green',justify='right')
txtdisplay.grid(row=0,columnspan=4)

# # photo=PhotoImage(file="Dog.jpg")
# label=ttk.Label(cal,Image=PhotoImage(file="Dog.png"))
# label.pack()


def btnclick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)

def btnCleardisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualinput():
    global operator
    add=str(eval(operator))
    text_input.set(add)
    operator=""


#===Buttons==========================<<<<<

btn1=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='1',command=lambda: btnclick(1))
btn1.grid(row=1,column=0,sticky=W)

btn2=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='2',command=lambda: btnclick(2))
btn2.grid(row=1,column=1,sticky=W)

btn3=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='3',command=lambda: btnclick(3))
btn3.grid(row=1,column=2,sticky=W)

addition=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='+',command=lambda: btnclick('+'))
addition.grid(row=1,column=3,sticky=W)

btn4=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='4',command=lambda: btnclick(4))
btn4.grid(row=2,column=0,sticky=W)

btn5=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='5',command=lambda: btnclick(5))
btn5.grid(row=2,column=1,sticky=W)

btn6=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='6',command=lambda: btnclick(6))
btn6.grid(row=2,column=2,sticky=W)

subtract=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='-',command=lambda: btnclick('-'))
subtract.grid(row=2,column=3,sticky=W)

btn7=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='7',command=lambda: btnclick(7))
btn7.grid(row=3,column=0,sticky=W)

btn8=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='8',command=lambda: btnclick(8))
btn8.grid(row=3,column=1,sticky=W)

btn9=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='9',command=lambda: btnclick(9))
btn9.grid(row=3,column=2,sticky=W)

multiply=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='*',command=lambda: btnclick('*'))
multiply.grid(row=3,column=3,sticky=W)

btn0=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='0',command=lambda: btnclick(0))
btn0.grid(row=4,column=0,sticky=W)

btnclear=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='C',command=btnCleardisplay)
btnclear.grid(row=4,column=1,sticky=W)

btnequals=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='=',command=btnEqualinput)
btnequals.grid(row=4,column=2,sticky=W)

divide=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='/',command=lambda: btnclick('/'))
divide.grid(row=4,column=3,sticky=W)

bracket1=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='(',command=lambda: btnclick('('))
bracket1.grid(row=5,column=0,sticky=W)

bracket2=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text=')',command=lambda: btnclick(')'))
bracket2.grid(row=5,column=1,sticky=W)

btndot=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='.',command=lambda: btnclick('.'))
btndot.grid(row=5,column=2,sticky=W)

#============Scientific================<<<<<

def trignometric():
    sin=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='sin',command=lambda: btnclick('math.sin'))
    sin.grid(row=6,column=0)

    sinh=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='sinh',command=lambda: btnclick('math.sinh'))
    sinh.grid(row=6,column=1)

    cos=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='cos',command=lambda: btnclick('math.cos'))
    cos.grid(row=6,column=2)

    cosh=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='cosh',command=lambda: btnclick('math.cosh'))
    cosh.grid(row=6,column=3)

    # cosec=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='cosec',command=lambda: btnclick('math.cosec'))
    # cosec.grid(row=7,column=0)

    # cosech=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='cosech',command=lambda: btnclick('math.cosech'))
    # cosech.grid(row=7,column=1)

    tan=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='tan',command=lambda: btnclick('math.tan'))
    tan.grid(row=7,column=2)

    tanh=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='tanh',command=lambda: btnclick('math.tanh'))
    tanh.grid(row=7,column=3)

    # sec=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='sec',command=lambda: btnclick('math.sec'))
    # sec.grid(row=8,column=0)

    # sech=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='sech',command=lambda: btnclick('math.sech'))
    # sech.grid(row=8,column=1)

    # cot=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='cot',command=lambda: btnclick('math.cot'))
    # cot.grid(row=8,column=2)

    # coth=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='coth',command=lambda: btnclick('math.coth'))
    # coth.grid(row=8,column=3)


scientific=Button(cal,width=9, bd=2, bg='powder blue', font='arial',text='>',command=trignometric)
scientific.grid(row=5,column=3)

#============================================================================================


cal.mainloop()
