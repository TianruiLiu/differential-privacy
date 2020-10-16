'''
File Description:
This file contains an implementation of differential privacy. 
It takes a database and a query from the user.

Author: 
Tianrui Liu; Qingru Zhang
'''
#IMPORT PACKAGES
import csv
import pandas as pd
import sys
import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import filedialog

#DECLARE CONSTANTS
HEIGHT = 700
WIDTH = 800

#INITIATION OF A GUI APP
app = tk.Tk()

#--- Create a basic frame and canvas for the GUI
canvas = tk.Canvas(app,height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(app,bg='#ebdada')
frame.place(relx=0.1,rely=0.1,relwidth=0.9,relheight=0.9)

#--- Create a first page for user to import their data file
def import_data(data):
    app.filename=filedialog.askopenfilename(initialdir="/user",
                                            title="Select A File",
                                            filetypes=(("excel files","*.xlsx"),("csv file","*.csv")))
    df=pd.read_csv(app.filename)
    if(len(df) == 0):       
                tk.messagebox.showinfo('No Rows Selected', 'CSV has no rows') 
                
import_button= tk.Button(frame, text="Import Data",command=import_data, bg='#d7c6cf',fg='#a2798f')
import_button.pack()
app.mainloop()