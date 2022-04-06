
from tkinter import *

gui = Tk()
gui.geometry('400x400')
gui.resizable(0,0)
gui.title('Odd or Even checker')
#Background color
gui.config(background="blue")


#Checks if number is even or odd   
def Odd_or_even():   


    integer1= input.get()
    try:  
        
        number = int(integer1)
        if number%2==0:
            
            number=str(number)
            result= Label(gui,text="{} is an even number!".format(number))
             
                
        else:
            
            number=str(number)
            result=Label(gui,text="{} is an odd number!".format(number))
           
        
    except:
        
        result=Label(gui,text="Invalid input!",fg="red")
        
    result.place(y=70,width=400)
    

    

#First label
label=Label(gui,text="Enter an integer: ")
label.place(y=10)



#Text box
input = Entry(gui, bg="white",fg="blue")
input.place(y=40,height=25,width=200)


#button
submit=Button(gui,text="Submit",command=Odd_or_even)
submit.place(x=210,y=40)


gui.mainloop()


