'''
Ruben Philip

Description:
I intially started using graphics.py but then I realized it was impossible to use it because it was missing some functions that was neccessary to build a calculator.
So, I made the calculator using tkinter and I used plenty of sources to help me construct this program(references are below). In this program, the user is first
supposed to select an operation, then the user will enter the numbers and finally press the solve button to get the answer.
There is also a RESET, HELP and ABOUT button for this calculator.
'''

import random
from tkinter import* # importing tkinter 
from tkinter import messagebox # importing messagebox from tkinter 

calculator = Tk() # create a window
calculator.resizable(0,0) # makes the window not resizable 
calculator.geometry("1000x700+180+20") # shows the dimensions for the window 
calculator.title("THE ULTIMATE CALCULATOR") # sets the title for the window 
calculator.configure(background='black') # sets the main window background colour as black  

# Create three different frames (sections) of the window # 
Top_Frame = Frame(calculator, width=1000, height=50, bd=16, relief='raise') # creates frame with the specify requirements 
Top_Frame.pack(side=TOP) # constructs the frame and states where it should be located  
Top_Frame.configure(background='snow3') # sets the blue background colour for the frame 

Left_Frame = Frame(calculator, width=600, height=600, bd=16, relief='raise') # creates frame with the specify requirements 
Left_Frame.pack(side=LEFT) # constructs the frame and states where it should be located  

Right_Frame = Frame(calculator, width=400, height=600, bd=16, relief='raise') # creates frame with the specify requirements 
Right_Frame.pack(side=RIGHT) # constructs the frame and states where it should be located
Right_Frame.configure(background='black') # sets the black background colour for the frame 

# Create the title in the top called The Ultimate Calculator #
Program_Title = Label(Top_Frame, font=('arial',50,'bold'), text="     The Ultimate Calculator     ",
                      bd=16, anchor=CENTER, bg="snow4", fg="black").grid(row = 0, column = 0)


var = IntVar() # makes var into a integer value 
Total = StringVar() # makes var into a string value 
firstnum = StringVar() # makes var into a string value 
secondnum = StringVar() # makes var into a string value 

def Operation(): 
    if  str(var.get()) == '1': # If user selects option 1, addition
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 + num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '2': # If user selects option 2
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 - num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '3': # If user selects option 3
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 * num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '4': # If user selects option 4
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 / num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '5': # If user selects option 5
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 % num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '6': # If user selects option 6 
        num1 = float(firstnum.get()) # gets the number entered as a float 
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 ** num2 # solves 
        Total.set(Sum) # print answer
    elif str(var.get()) == '7': # If user selects option 6 
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = num1 // num2 # solves 
        Total.set(Sum) # print answer 
    elif str(var.get()) == '8': # If user selects option 6 
        num1 = float(firstnum.get()) # gets the number entered as a float
        num2 = float(secondnum.get()) # gets the number entered as a float
        Sum = random.randint(num1, num2) # solves 
        Total.set(Sum) # print answer
    else:
        Total.set("0") # If a number is not written then the default answer is 0 

def Reset(): # Sets all the number to 0 
    firstnum.set("0")
    secondnum.set("0")
    Total.set("0")

def Help(): # displays a help message 
    messagebox.showinfo("Help","Instructions: 1. Select the math operation you want to perform 2. Enter the two numbers 3. Click the Solve button to get the answer            \
Option:                                                                                                                    \
Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. Ex. 9//2 = 4                                                                                                                   \
Exponent - The first number inputed should be the base and the second number inputed should be the power                                                \
Modulus - Divides first number inputed by the second number inputed and returns the remainder                                                                                 \
Random Num - The first number inputed should be the lowest range number to generate random number and the second number should be the highest range number to generate random number.")

def About(): # displays an about message
    messagebox.showinfo("About", "Creator: Ruben Philip                                                                \
                        References: Tutorialspoint, Pythonprogramming, Effbot and Pythonspot")
    
# Creates the Select Operation Label
Label_Firstnum = Label(Left_Frame, font=('Helvetica', 22, 'bold'), text="Select Operation:",
                    fg="dark slate blue", bd=16).grid(row=0, column=0, sticky=W)
# Creates all the RadioButtons (choice option botton)
Botton1 = Radiobutton(Left_Frame, text = "Addition", variable=var, value =1,
                  font=('Helvetica', 22, 'bold')).grid(row=1, column=0, sticky=W)
Botton2 = Radiobutton(Left_Frame, text = "Substraction", variable=var, value =2,
                  font=('Helvetica', 22, 'bold')).grid(row=2, column=0, sticky=W)
Botton3 = Radiobutton(Left_Frame, text = "Multiplication", variable=var, value =3,
                  font=('Helvetica', 22, 'bold')).grid(row=3, column=0, sticky=W)
Botton4 = Radiobutton(Left_Frame, text = "Division", variable=var, value =4,
                  font=('Helvetica', 22, 'bold')).grid(row=4, column=0, sticky=W)
Botton5 = Radiobutton(Left_Frame, text = "Modulus", variable=var, value =5,
                  font=('Helvetica', 22, 'bold')).grid(row=1, column=1, sticky=W)
Botton6 = Radiobutton(Left_Frame, text = "Exponent", variable=var, value =6,
                  font=('Helvetica', 22, 'bold')).grid(row=2, column=1, sticky=W)
Botton7 = Radiobutton(Left_Frame, text = "Floor Division", variable=var, value =7,
                  font=('Helvetica', 22, 'bold')).grid(row=3, column=1, sticky=W)
Botton8 = Radiobutton(Left_Frame, text = "Random Num", variable=var, value =8,
                  font=('Helvetica', 22, 'bold')).grid(row=4, column=1, sticky=W)

# Displays the labels and textboxes 
Label_Firstnum = Label(Left_Frame, font=('Helvetica', 22, 'bold'), text="Enter First Number",
                    fg="midnight blue", bd=25).grid(row=5, column=0, sticky=W)
Textbox_Firstnum = Entry(Left_Frame, font=('Helvetica', 22, 'bold'), bd=6, width=15,bg="#F2EAED", fg="midnight blue",
                    textvariable=firstnum).grid(row=5, column=1)
Label_Secondnum = Label(Left_Frame, font=('Helvetica', 22, 'bold'), text = "Enter Second Number",
                    fg="midnight blue", bd=25).grid(row=6, column=0, sticky=W)
Textbox_Secondnum = Entry(Left_Frame, font=('Helvetica', 22, 'bold'), bd=6, width=15,bg="#F2EAED", fg="midnight blue",
                     textvariable=secondnum).grid(row=6, column=1)
Label_Total = Label(Left_Frame, font=('Helvetica', 22, 'bold'), text = "Answer: ", fg="#888C46", bd=25,).grid(row=7, column=0, sticky=W)

Label_Answer = Label(Left_Frame, font=('Helvetica', 22, 'bold'), bd=4, width=15,bg="#888C46",
                  textvariable=Total, relief='sunken').grid(row=7, column=1, sticky=W)

# Creates the buttons on the right side
Botton_Total = Button(Right_Frame, pady=8, bd=8, fg="black", font=('Helvetica', 25, 'bold'), width=16, height=2, 
                  text = "Solve", bg="#888C46", command=Operation).grid(row=1, column=0)
Botton_Reset = Button(Right_Frame, bd=8, fg="black", font=('Helvetica', 25, 'bold'), width=16, height=2,
                  text = "Reset", pady=8, bg="#A4A4BF",command=Reset).grid(row=2, column=0)
Botton_Help = Button(Right_Frame, pady=8, bd=8, fg="black", font=('Helvetica', 25, 'bold'), width=16, height=2,
                  text = "Help", bg="#2A3457", command=Help).grid(row=3, column=0)
Botton_About = Button(Right_Frame, pady=8, bd=8, fg="black", font=('Helvetica', 25, 'bold'), width=16, height=2,
                  text = "About", bg="#16235A", command=About).grid(row=4, column=0)

calculator.mainloop() # Necessary for the program to work

'''
Notes: 
width = x -> gives the width
height = x -> gives the height
relief = x -> specifies the type of the border
bd = x -> size of border
bg = x -> background colour
fg = x -> text colour
font = x -> font type, letter size
command = x -> Function or method to be called when the button is clicked
textvariable = x -> sets the number inputed as x
grid(row=6, column=1) -> where the widget is located in the frame
'''

'''
References:
https://www.tutorialspoint.com/python/tk_relief.htm
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/
http://effbot.org/tkinterbook/grid.htm
http://effbot.org/tkinterbook/radiobutton.htm
https://pythonspot.com/tk-message-box/
https://www.tutorialspoint.com/python/python_basic_operators.htm
https://wiki.tcl.tk/37701
http://blog.visme.co/color-combinations/
'''
    
