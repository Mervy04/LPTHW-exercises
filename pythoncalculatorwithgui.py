from tkinter import *

root = Tk()
root.title("Simple Calculator App")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# creating button functions
def button_click(number):
    #e.delete(0, END) # delete whats already in the box
    curnumber = e.get() #currentnumber variable
    e.delete(0, END) # END deletes everything
    e.insert(0,str( curnumber) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global fnum # creating a global variable
    global math 

    math = "addition"
    fnum = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, fnum + int(second_number))
    if math == "subtraction":
        e.insert(0, fnum - int(second_number))

    if math == "division":
        e.insert(0, fnum / int(second_number))

    if math == "multiplication":
        e.insert(0, fnum * int(second_number))

def button_divide():
    first_number = e.get()
    global fnum 
    global math 

    math = "division"
    fnum = int(first_number)
    e.delete(0, END)
    return

def button_subtract():
    first_number = e.get()
    global fnum 
    global math 

    math = "subtraction"
    fnum = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global fnum 
    global math 

    math = "multiplication"
    fnum = int(first_number)
    e.delete(0, END)
    return

#Define buttons
button1 = Button(root, text=1, padx=40, pady=20, command=lambda:button_click(1)) # you cant pass parameters with buttons right away, so we use a lambda (command=lambda....)
button2 = Button(root, text=2, padx=40, pady=20, command=lambda:button_click(2))
button3 = Button(root, text=3, padx=40, pady=20, command=lambda:button_click(3))
button4 = Button(root, text=4, padx=40, pady=20, command=lambda:button_click(4))
button5 = Button(root, text=5, padx=40, pady=20, command=lambda:button_click(5))
button6 = Button(root, text=6, padx=40, pady=20, command=lambda:button_click(6))
button7 = Button(root, text=7, padx=40, pady=20, command=lambda:button_click(7))
button8 = Button(root, text=8, padx=40, pady=20, command=lambda:button_click(8))
button9 = Button(root, text=9, padx=40, pady=20, command=lambda:button_click(9))
button0 = Button(root, text=0, padx=40, pady=20, command=lambda:button_click(0))
buttonadd =Button(root, text="+", padx=39, pady=20, command= button_add)
buttonsubtract =Button(root, text="-", padx=41, pady=20, command= button_subtract)
buttondivide =Button(root, text="/", padx=41, pady=20, command= button_divide)
buttonmultiply =Button(root, text="*", padx=40, pady=20, command= button_multiply)
buttonequal =Button(root, text="=", padx=91, pady=20, command= button_equal)
buttonclear =Button(root, text="Clear", padx=79, pady=20, command=button_clear)

#put buttons on screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4)
buttonclear.grid(row=4, column=1, columnspan=2)
buttonadd.grid(row=5)
buttonequal.grid(row=5, column=1, columnspan=2)

buttonsubtract.grid(row=6)
buttonmultiply.grid(row=6,column=1)
buttondivide.grid(row=6, column= 2)

root.mainloop()
