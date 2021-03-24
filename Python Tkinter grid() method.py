from tkinter import*



parent = Tk()
name = Label(parent,text = "What's your name").grid(row= 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Label(parent, text = "what's your password").grid( row= 1, column = 0)
e2 = Entry(parent).grid(row = 1, column =1)
submit = Button(parent, text = "Submit").grid( row = 4, column = 0)
parent.mainloop()



#Python Tkinter grid() method

#The grid() geometry manager organizes the widgets in the tabular form. We can specify the rows and columns as the options in the method call. We can also specify the column span (width) or rowspan(height) of a widget.

#This is a more organized way to place the widgets to the python application. The syntax to use the grid() is given below.

#Syntax
#widget.grid(options)  
#A list of possible options that can be passed inside the grid() method is given below.

#Column
#The column number in which the widget is to be placed. The leftmost column is represented by 0.
#Columnspan
#The width of the widget. It represents the number of columns up to which, the column is expanded.
#ipadx, ipady
#It represents the number of pixels to pad the widget inside the widget's border.
#padx, pady
#It represents the number of pixels to pad the widget outside the widget's border.
#row
#The row number in which the widget is to be placed. The topmost row is represented by 0.
#rowspan
#The height of the widget, i.e. the number of the row up to which the widget is expanded.
#Sticky
#If the cell is larger than a widget, then sticky is used to specify the position of the widget inside the cell. It may be the concatenation of the sticky letters representing the position of the widget. It may be N, E, W, S, NE, NW, NS, EW, ES.


#Python Tkinter
#Python Tkinter place() method
#The place() geometry manager organizes the widgets to the specific x and y coordinates.

#Syntax
#widget.place(options)  
#A list of possible options is given below.

#Anchor: It represents the exact position of the widget within the container. The default value (direction) is NW (the upper left corner)
#bordermode: The default value of the border type is INSIDE that refers to ignore the parent's inside the border. The other option is OUTSIDE.
#height, width: It refers to the height and width in pixels.
#relheight, relwidth: It is represented as the float between 0.0 and 1.0 indicating the fraction of the parent's height and width.
#relx, rely: It is represented as the float between 0.0 and 1.0 that is the offset in the horizontal and vertical direction.
#x, y: It refers to the horizontal and vertical offset in the pixels.
#Example
# !/usr/bin/python3  
from tkinter import *  
top = Tk()  
top.geometry("400x250")  
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)  
top.mainloop()  
