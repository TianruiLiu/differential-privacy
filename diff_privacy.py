'''
File Description:
This file contains an implementation of differential privacy. 
It takes a database and a query from the user.

Author: 
Tianrui Liu; Qingru Zhang
'''
#IMPORT PACKAGES

from tkinter import filedialog
import tkinter as tk 
from tkinter import ttk 
from process_query import *


  #--constant declaration
LARGEFONT =("Verdana", 25) 
HEIGHT=1000
WIDTH=800

class tkinterApp(tk.Tk): 


    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 

        canvas=tk.Canvas(self,height=HEIGHT,width=WIDTH) 
        canvas.pack()

        # creating a container 
        container = tk.Frame(canvas,bg="#ebdada")    
        container.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (StartPage, Page1, Page2, Page3): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)
   
        self.show_frame(StartPage) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   
# first window frame startpage: import a file
   
class StartPage(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
          
        # label of frame Layout 2 
        label = ttk.Label(self, text ="Import a CSV File", font = LARGEFONT) 
          
        # putting the grid in its place by using 
        # grid 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
        
        # create an input button
        def file_opener():
            global df
            input = filedialog.askopenfile(initialdir="/")
            df=pd.read_csv(input)


        import_button= tk.Button(self, text="Select An Input File",command = lambda:file_opener(), bg='#d7c6cf',fg='#a2798f')
        import_button.place(relx=0.3,rely=0.4,relwidth=0.4,relheight=0.2)

        # a button that connects to the next page
        button1 = ttk.Button(self, text ="Next Page", 
        command = lambda : controller.show_frame(Page1)) 
      
        # putting the button in its place by 
        # using grid 
        button1.place(relx=0.2,rely=0.8,relwidth=0.2,relheight=0.1)
   
           
   
   
# second window frame page1: choose query type and lambda
class Page1(tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Choose Query Type and Lambda", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        # layout2 
        button2 = ttk.Button(self, text ="Next Page", 
                            command = lambda : controller.show_frame(Page2)) 
      
        # putting the button in its place by  
        # using grid 
        button2.place(relx=0.2,rely=0.8,relwidth=0.2,relheight=0.1)

        # pick query type
        def set_query_min():
            global query_type
            query_type="Min"
            print(query_type)
            newlabel=tk.Label(self,text="Query Type Min Selected!")
            newlabel.place(relx=0.5,rely=0.2,relwidth=0.4,relheight=0.1)

        def set_query_max():
            global query_type
            query_type="Max"
            print(query_type)
            button_min['bg']='red'
            newlabel=tk.Label(self,text="Query Type Max Selected!")
            newlabel.place(relx=0.5,rely=0.2,relwidth=0.4,relheight=0.1)

        def set_query_mean():
            global query_type
            query_type="Mean"
            print(query_type)
            button_min['bg']='red'
            newlabel=tk.Label(self,text="Query Type Mean Selected!")
            newlabel.place(relx=0.5,rely=0.2,relwidth=0.4,relheight=0.1)

        def set_query_count():
            global query_type
            query_type="Count"
            print(query_type)
            button_min['bg']='red'
            newlabel=tk.Label(self,text="Query Type Count Selected!")
            newlabel.place(relx=0.5,rely=0.2,relwidth=0.4,relheight=0.1)

        def set_query_sum():
            global query_type
            query_type="Sum"
            print(query_type)
            button_min['bg']='red'
            newlabel=tk.Label(self,text="Query Type Sum Selected!")
            newlabel.place(relx=0.5,rely=0.2,relwidth=0.4,relheight=0.1)

        label1=ttk.Label(self,text="What's your query Type?")
        label1.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.1)

        button_min=tk.Button(self,text="Min",command=set_query_min, font=30)
        button_min.place(relx=0.2,rely=0.2,relwidth=0.2,relheight=0.05)

        button_max=tk.Button(self,text="Max",command=set_query_max, font=30)
        button_max.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.05)

        button_mean=tk.Button(self,text="Mean",command=set_query_mean, font=30)
        button_mean.place(relx=0.2,rely=0.3,relwidth=0.2,relheight=0.05)

        button_count=tk.Button(self,text="Count",command=set_query_count, font=30)
        button_count.place(relx=0.2,rely=0.35,relwidth=0.2,relheight=0.05)

        button_sum=tk.Button(self,text="Sum",command=set_query_sum, font=30)
        button_sum.place(relx=0.2,rely=0.4,relwidth=0.2,relheight=0.05)
   
        # create an entry for lambda
        def save_lambda():
            global lambda_value
            lambda_value=entry_lambda.get()
            print(lambda_value)
            newlabel=tk.Label(self,text="Lambda= "+lambda_value + " is Saved!")
            newlabel.place(relx=0.5,rely=0.75,relwidth=0.4,relheight=0.1)

        label_lambda=ttk.Label(self,text="Type in an arbitrary value for lambda")
        label_lambda.place(relx=0.1,rely=0.5,relwidth=0.6,relheight=0.1)

        entry_lambda=tk.Entry(self)
        entry_lambda.place(relx=0.1,rely=0.65,relwidth=0.6,relheight=0.1)

        save_entry_button=tk.Button(self,text="Save", command=save_lambda, font=30)
        save_entry_button.place(relx=0.8,rely=0.65,relwidth=0.15,relheight=0.1)

# third window frame page2: enter target column and condition(s)
class Page2(tk.Frame):  
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Enter Target Column and Condition(s)", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        # button to show frame 2 with text 
        # layout2 
        button3 = ttk.Button(self, text ="Next Page", 
                            command = lambda : controller.show_frame(Page3)) 
      
        # putting the button in its place by  
        # using grid 
        button3.place(relx=0.2,rely=0.8,relwidth=0.2,relheight=0.1) 

        # create an entry for target column
        label_column=ttk.Label(self,text="What's your target column?")
        label_column.place(relx=0.1,rely=0.2,relwidth=0.6,relheight=0.1)

        def save_column():
            global target_column
            target_column=entry_column.get()
            print(target_column)
            newlabel=tk.Label(self,text="Target column is set as "+entry_column.get())
            newlabel.place(relx=0.1,rely=0.4,relwidth=0.6,relheight=0.1)

        entry_column=tk.Entry(self)
        entry_column.place(relx=0.1,rely=0.3,relwidth=0.6,relheight=0.1)

        save_column_button=tk.Button(self,text="Save", command=save_column, font=30)
        save_column_button.place(relx=0.8,rely=0.3,relwidth=0.15,relheight=0.1)

        # create an entry for condition(s)
        label_condition=ttk.Label(self,text="What's your query condition(s)?")
        label_condition.place(relx=0.1,rely=0.5,relwidth=0.6,relheight=0.1)

        def save_condition():
            global query_condition
            query_condition=entry_condition.get().split(";")
            print(query_condition)
            newlabel=tk.Label(self,text="Query condition is set as "+entry_condition.get())
            newlabel.place(relx=0.1,rely=0.7,relwidth=0.6,relheight=0.1)

        entry_condition=tk.Entry(self)
        entry_condition.place(relx=0.1,rely=0.6,relwidth=0.6,relheight=0.1)

        save_condition_button=tk.Button(self,text="Save", command=save_condition, font=30)
        save_condition_button.place(relx=0.8,rely=0.6,relwidth=0.15,relheight=0.1)
        
# second window frame page1: choose query type and lambda
class Page3(tk.Frame):

    def __init__(self, parent, controller):
        global df, query_condition, target_column, query_type, lambda_value
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Result Display!", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        def see_result():
            global df, query_condition, target_column, query_type, lambda_value
            result = processOneQuery(df, query_condition, target_column, query_type, lambda_value)
            result = result.item(0)
            label_result = ttk.Label(self, text="The calculated result is: "+ str(result),font=30)
            label_result.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)

        result_button = tk.Button(self, text="See the final result", command=see_result, font=30)
        result_button.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)

   
# Driver Code
app = tkinterApp() 
app.mainloop() 