'''
Created on Jun 16, 2016

@author: arunanramalingam
'''
from Tkinter import *
from matplotlib.pyplot import title
from _sqlite3 import Row
from Finder.Type_Definitions import column
from matplotlib.cbook import Null


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
        
    
        frame1 = Frame(self.parent)
        frame1.grid(row=0)
        frame2 = Frame(self.parent)
        frame2.grid(row=1)
        
        self.parent.title("Site level task completion (TCS)")
        l1=Label(frame1, text='Enter the SR id you want to complete')
       # l1.pack(side=LEFT)
        l1.grid(row=0, column=0)
        self.input1=Entry(frame1,justify=CENTER)
        
        #self.input1.pack(side=RIGHT)
        self.input1.grid(row=0 , column=1)
        l2=NONE
        b1=Button(frame2,text="Submit",fg="black" ,command=self.on_button)
        b1.grid(row=1, column=1)
        #b1.pack()
       

       
        
        
    def on_button(self):
        frame3 = Frame(self.parent)
        frame3.grid(row=2)    
        We_entered = self.input1.get()
        l2=Label(frame3, text="                                                                       ")
        l2.grid(row=2)
        l2=Label(frame3, text=We_entered)
        l2.grid(row=2)
       
        
        
        
        #first= Entry(root,width=10)

def main():
  
    root = Tk()
    root.geometry("500x350")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()

    

