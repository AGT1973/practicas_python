#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  borrar.py
#  
#  Copyright 2019 Ariel H Garcia Traba <AGT@AGT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
 
class BackGroundFrame(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
         
        self.frames ={}
         
        for F in (StartPage,ManualPage):    
            frame= F(container,self)
            self.frames[F]= frame
            frame.grid(row = 0, column=0,sticky="nsew")
             
        self.show_frame(StartPage)
         
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
         
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        instruction = tk.Label(self,text="Welcome to Dispensing GUI")
        instruction.grid(row=0 , column =0,columnspan=3, sticky = "W")
         
        self.action1 = tk.Button(self, text="Retrieve Solution Name",command=lambda:self.retrievesolutions )
        self.action1.grid(row = 0, column = 4,columnspan = 2,sticky= "W")
         
        tk.Label(self,text = "        ").grid(row =1, column = 0,sticky = "W")
         
        tk.Label(self,text = "Solutions to Pumps Allocations").grid(row =2, column = 0,columnspan=10,sticky = "W")
         
        self.typeofsolution1 = tk.Entry(self,width=12) #tk.Entry widget function 
        self.typeofsolution1.grid(row =3, column = 0,sticky = "W")
        tk.Label(self,text = "Pump 1").grid(row =4, column = 0,columnspan=2,sticky = "W") 
         
          
        tk.Label(self,text = "    ").grid(row =3, column = 1,sticky = "W")
         
        self.typeofsolution2 = tk.Entry(self,width=12) #tk.Entry widget function 
        self.typeofsolution2.grid(row =3, column = 2, sticky = "W")
        tk.Label(self,text = "Pump 2").grid(row =4, column = 2,sticky = "W")
         
        tk.Label(self,text = "    ").grid(row =3, column = 3,sticky = "W")
         
         
        self.typeofsolution3 = tk.Entry(self,width=12)
        self.typeofsolution3.grid(row =3, column = 4,sticky = "W")
        tk.Label(self,text = "Pump 3").grid(row =4, column = 4,columnspan=2,sticky = "W") 
         
        tk.Label(self,text = "    ").grid(row =3, column = 5,sticky = "W")
         
        self.typeofsolution4 = tk.Entry(self,width=12)
        self.typeofsolution4.grid(row =3, column = 6,sticky = "W")
        tk.Label(self,text = "Pump 4").grid(row =4, column = 6,columnspan=2,sticky = "W")
         
        self.submitManual = tk.Button(self,text="Manual",command=lambda:controller.show_frame(ManualPage))
        self.submitManual.grid(row =8,rowspan=5, column = 0, columnspan = 4,sticky = "W")
         
        self.submitAutomatic = tk.Button(self,text="Automatic")
        self.submitAutomatic.grid(row =8,rowspan=5, column = 1, columnspan = 2,sticky = "W")
         
    def retrievesolutions(self):
        global name1
        global name2
        global name3
        name1 = self.typeofsolution1.get()
        name2 = self.typeofsolution2.get()
        name3 = self.typeofsolution3.get()  
        print(name1,name2,name3)
             
         
class ManualPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
          
        self.manualtitle = tk.Label(self, text="Welcome to Manual Dispensing")
        self.manualtitle.grid(row=0 , column =0, columnspan=6, sticky="W")
         
        tk.Label(self,text = "Solution Name    ").grid(row =1, column = 0,sticky="W")
        tk.Label(self,text = "Time Input(s)     ").grid(row =1, column = 2,sticky="w")
        tk.Label(self,text = "Dispense").grid(row =1, column = 5,sticky="W")
     
        
        self.text1 = tk.Text(self, width =10, height = 1)
        self.text1.grid(row = 2, column = 0,columnspan= 10,sticky= "W")
        tk.Label(self,text = "        ").grid(row =3, column = 0,sticky="W")
         
        self.text2 = tk.Text(self, width =10, height = 1)
        self.text2.grid(row = 4, column = 0,columnspan= 10,sticky= "W")
        tk.Label(self,text = "        ").grid(row =5, column = 0,sticky="W")
         
        self.text3 = tk.Text(self, width =10, height = 1)
        self.text3.grid(row = 6, column = 0,columnspan= 10,sticky= "w")
        tk.Label(self,text = "        ").grid(row =7, column = 0,sticky="W")
         
        self.text4 = tk.Text(self, width =10, height = 1)
        self.text4.grid(row = 8, column = 0,columnspan= 10,sticky= "w")
        tk.Label(self,text = "        ").grid(row =9, column = 0,sticky="W")
            
         
        self.submitlol = tk.Button(self,text="Back to Main Menu",command=lambda:controller.show_frame(StartPage))
        self.submitlol.grid(row =10,rowspan=5, column = 0, columnspan = 4,sticky = "W")
         
         
         
        self.timepump1 = tk.Entry(self,width = 10) #entry widget function 
        self.timepump1.grid(row =2, column = 1,columnspan=10,sticky="w")
         
        self.timepump2 = tk.Entry(self,width = 10) #entry widget function 
        self.timepump2.grid(row =4, column = 1,columnspan=10,sticky="w")
         
        self.timepump3 = tk.Entry(self,width = 10) #entry widget function 
        self.timepump3.grid(row =6, column = 1,columnspan=10,sticky="w")
         
        self.timepump4 = tk.Entry(self,width = 10) #entry widget function 
        self.timepump4.grid(row =8, column = 1,columnspan=10,sticky="w")
         
         
        self.submit1 = tk.Button(self, text="Dispense 1")
        self.submit1.grid(row =2, column = 3, columnspan = 10,sticky="w")
         
        self.submit2= tk.Button(self, text="Dispense 2")
        self.submit2.grid(row =4, column = 3, columnspan = 10,sticky="w")
         
        self.submit3 = tk.Button(self, text="Dispense 3")
        self.submit3.grid(row =6, column = 3, columnspan = 10,sticky="w")
         
        self.submit4= tk.Button(self, text="Dispense 4")
        self.submit4.grid(row =8, column = 3, columnspan = 10,sticky="w")
         
        global name1
        global name2
        global name3
         
        self.text1.delete(0.0)
        self.text1.insert(0.0, name1)
             
        self.text2.delete(0.0)
        self.text2.insert(0.0, name2)
             
        self.text3.delete(0.0)
        self.text3.insert(0.0, name3)
        
app = BackGroundFrame()
app.mainloop()
