from tkinter import*
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

root=Tk()
conn = sqlite3.connect('DataBase.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Product (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name_of_product TEXT NOT NULL, AQ REAL NOT NULL, MD REAL NOT NULL )")
conn.commit()
query = "SELECT * FROM Product "
result = c.execute(query)

    


date = datetime.datetime.now().date()
    
class Inventory_System:
    def __init__(self, master, *args, **kwargs ):
        self.master = master
        #self.Sbar = Scrollbar(root)
        
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Reset", command=self.Reset)
        
       
        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
     
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.Help)
        helpmenu.add_command(label="About...", command=self.About)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)
        
        #self.Sbar.pack(side = RIGHT, fill = "y")
        self.left = Frame(master, width=700, height=700)
        self.left.pack(side=LEFT)
        
        self.right = Frame(master, width=666, height=700, bg='lightblue')
        self.right.pack(side=RIGHT, expand=0, fill= BOTH)

       
        
        
        self.tree = ttk.Treeview(self.right, height=768)
        self.tree.pack(padx=10, pady=30)
        
        self.tree["columns"]=("one","two","three")
        self.tree.column('#0', width= 0)
        self.heading = Label(self.right, text="Stock", font=('arial 15 bold'), fg='steelblue', bg='lightblue')
        self.heading.place(x=260, y=0)
        self.tree.heading("one", text="Product Name")
        self.tree.heading("two", text="Available quantity*")
        self.tree.heading("three", text="Monthly Demand*")
        
        #self.list.insert(END, c.fetchall())
        
        #self.tbox = Text(self.right, width=300, height=768, yscrollcommand = self.Sbar.set)
        #self.tbox.place(x=0, y=0)
        #self.Sbar.config(command=self.tbox.yview)
        
        self.heading = Label(self.left, text="ADD/UPDATE/DELETE/ PRODUCTS", font=('arial 30 bold'), fg='steelblue')
        self.heading.place(x=20, y=30)
        self.heading = Label(self.left, text="*Product quantity based product type value of 1 unit is( 1KG or 1 PACK or 1 LITER)", font=('arial 10 bold'), fg='steelblue')
        self.heading.place(x=20, y=500)
        self.heading = Label(self.left, text="*** or ** Mandatory fields For Add and Update operation ", font=('arial 10 bold'), fg='steelblue')
        self.heading.place(x=20, y=520)
        self.heading = Label(self.left, text="*** Mandatory fields For Search and Delete operation ", font=('arial 10 bold'), fg='steelblue')
        self.heading.place(x=20, y=540)
        self.heading = Label(self.left, text="RL stands for Requirement List which saved in RequirementList folder ", font=('arial 10 bold'), fg='steelblue')
        self.heading.place(x=20, y=560)

        #self.id_1 = Label(self.left, text="Enter Product Id", font=('arial 18 bold'))
        #self.id_1.place(x=10, y=70)
                
        self.name_1 = Label(self.left, text="Enter Product Name***", font=('arial 18 bold'))
        self.name_1.place(x=10, y=120)
        
        self.AQ_1 = Label(self.left, text="Enter Available quantity**", font=('arial 18 bold'))
        self.AQ_1.place(x=10, y=170)
        
        #self.vendor_1 = Label(self.left, text="Enter Vendor Name", font=('arial 18 bold'))
        #self.vendor_1.place(x=10, y=220)
        
        self.MD_1 = Label(self.left, text="Enter Monthly Demand**", font=('arial 18 bold'))
        self.MD_1.place(x=10, y=220)
        
      #  self.tproduct = Label(self.right, text="Product", font=('arial 18 bold'), bg='lightblue', fg='white')
       # self.tproduct.place(x=0, y=60)
        
       # self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='lightblue', fg='white')
      #  self.tquantity.place(x=300, y=60)
        
      #  self.tAQ = Label(self.right, text="AQ", font=('arial 18 bold'), bg='lightblue', fg='white')
      #  self.tAQ.place(x=580, y=60)
        
       # self.id_e = Entry(self.left, width=25, font=('arial 18 bold'))
       # self.id_e.place(x=360, y=70)

        self.name_e = Entry(self.left, width=25, font=('arial 18 bold'))
        self.name_e.place(x=360, y=120)
        
        self.AQ_e = Entry(self.left, width=25, font=('arial 18 bold'))
        self.AQ_e.place(x=360, y=170)
        
       # self.vendor_e = Entry(self.left, width=25, font=('arial 18 bold'))
       # self.vendor_e.place(x=360, y=220) 
        
        self.MD_e = Entry(self.left, width=25, font=('arial 18 bold'))
        self.MD_e.place(x=360, y=220) 
       
        self.btn_add = Button(self.left, text="Add Product", width=15, height=2, bg='steelblue', fg='white', command=self.get_Product)
        self.btn_add.place(x=540, y=280)
        
        self.btn_clear = Button(self.left, text="Clear all Fields", width=15, height=2, bg='steelblue', fg='white', command=self.clear_all)
        self.btn_clear.place(x=360, y=280)
        self.btn_search = Button(self.left, text="Search", width=15, height=2, bg='orange', fg='white', command=self.search)
        self.btn_search.place(x=360, y=340)
        self.btn_update = Button(self.left, text="Update", width=15, height=2, bg='steelblue', fg='white', command=self.update)
        self.btn_update.place(x=540, y=340)
        self.btn_Requirement = Button(self.left, text="Generate RL", width=15, height=2, bg='steelblue', fg='white', command=self.Requirement)
        self.btn_Requirement.place(x=540, y=400)
        self.btn_Delete = Button(self.left, text="Delete", width=15, height=2, bg='red', fg='white', command=self.Delete)
        self.btn_Delete.place(x=360, y=400)
        
        self.Refresh(self) 
    def Refresh(self, k, *args, **kwargs):
        query2 = "SELECT count(*) FROM Product"
        result2 = c.execute(query2)
        for r in result2:
            Product_count = r[0]
        x = Product_count
        if x != 0:
            result=c.execute("SELECT * FROM Product")
            rows = c.fetchall()
            for row in rows:
                self.get_name = row[1]
                self.get_AQ = row[2]
                self.get_MD = row[3]
                self.tree.insert("", END, values=(str(self.get_name), str(self.get_AQ), str(self.get_MD)))
    
    def get_Product(self, *args, **kwargs):

        #self.id = self.id_e.get()
        self.name = self.name_e.get()
        self.AQ = self.AQ_e.get()
        self.MD = self.MD_e.get()
        query = "SELECT * FROM Product WHERE Name_of_product=?"
        result = c.execute(query, (self.name,))
        records = c.fetchall()
        x = len(records)
        result = c.execute(query, (self.name,))
        for self.r in result:
                 self.get_name = self.r[1]
                 self.get_AQ = self.r[2]
                 self.get_MD = self.r[3]
        
        if self.name == '' or self.AQ == '' or self.MD == '':
            tkinter.messagebox.showinfo('Error', 'Please Fill all the entries.')
            
        elif x != 0 :
            tkinter.messagebox.showinfo('Error', 'Product already exists')
            
        else :
            sql = "INSERT INTO Product (Name_of_product, AQ, MD) VALUES(?, ?, ?)"
            c.execute(sql, (self.name, self.AQ, self.MD))
            conn.commit()
            
            tkinter.messagebox.showinfo('Success', 'Successfully added')
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.Refresh(self)
            self.clear_all(self)
           
    def clear_all(self, *args, **kwargs):
        
        #self.id_e.delete(0, END)
        self.name_e.delete(0, END)
        self.AQ_e.delete(0, END)
        #self.vendor_e.delete(0, END)
        self.MD_e.delete(0, END)
        

    def update(self, *args, **kwargs):
        
        self.name = self.name_e.get()
        self.AQ = self.AQ_e.get()
        self.MD = self.MD_e.get()
        if self.name == '' or self.AQ == '' or self.MD == '':
            tkinter.messagebox.showinfo('Error', 'Please Fill all the entries.')
        else:
            query = " UPDATE Product SET Name_of_product=?, AQ=?, MD=? WHERE Name_of_product=?"
            c.execute(query, (self.name, self.AQ, self.MD, self.name_e.get()))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Update the database")
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.Refresh(self) 
        
        
    def search(self, *args, **kwargs):
        x = self.name_e.get()
        sql = "SELECT * FROM Product WHERE Name_of_product=?"
        result = c.execute(sql,  (x,) )
        for r in result:
            self.n1 = r[1]
            self.n2 = r[2]
            self.n3 = r[3]
            
        conn.commit()
        
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))
        
        self.AQ_e.delete(0, END)
        self.AQ_e.insert(0, str(self.n2))
        
        
        self.MD_e.delete(0, END)
        self.MD_e.insert(0, str(self.n3))
        
    def Delete(self, *args, **kwargs):
        self.name = self.name_e.get()
        ans = tkinter.messagebox.askquestion("Delete Product", "Do you really want to Delete")
        if self.name == '':
            tkinter.messagebox.showinfo('Error', 'Please Fill all the entries.')
        
        elif ans == 'yes':
            
            query = "SELECT * FROM Product WHERE Name_of_product=?"
            conn = sqlite3.connect("DataBase.db")
            c = conn.cursor()
            result = c.execute(query, (self.name,))
            records = c.fetchall()
            x = len(records)
            result = c.execute(query, (self.name,))
            for self.r in result:
                self.get_name = self.r[1]
                self.get_AQ = self.r[2]
                self.get_MD = self.r[3]
            if x == 0 :
                tkinter.messagebox.showinfo('Error', 'No Product exists')
            else:
                self.name = self.name_e.get()
                conn = sqlite3.connect("DataBase.db")
                c = conn.cursor()
                c.execute("DELETE FROM Product WHERE Name_of_product=?",(self.name, ))
                conn.commit()
                conn.close()
                info = tkinter.messagebox.showinfo("Success", "         Deleted         ")
                for i in self.tree.get_children():
                    self.tree.delete(i)
                self.Refresh(self)
                self.clear_all(self) 
    def Reset(self, *args, **kwargs):
        answer = tkinter.messagebox.askquestion("Reset", "Do you really want to reset")
        print(answer)
        if answer == 'yes':
               conn = sqlite3.connect("DataBase.db")
               c = conn.cursor()
               c.execute("DELETE FROM Product")
               conn.commit()
               conn.close()
               info = tkinter.messagebox.showinfo("Success", "        Reset     ")
               for i in self.tree.get_children():
                    self.tree.delete(i)
               self.Refresh(self) 
               
        
    def Help(self, *args, **kwargs):
        tkinter.messagebox.showinfo("Help", "######################################################################??????????????????????????????????? ")
    def About(self, *args, **kwargs):
        tkinter.messagebox.showinfo("About", "Created By: Shivendra Singh Thakur")
    
    def Requirement(self, *args, **kwargs):
        ans = tkinter.messagebox.askquestion("Generate Requirement List", "Do you really want to Generate Requirement List")
        if ans == 'yes':
            directory = "RequirementList/" + str(date) + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            RequirementList = "\t\t\t\t\t*Requirement List*\n\n"
            dt = "\t" + str(date)
        
            table_header = "\n\n\t---------------------------------------------------------\n\t\tSN.\t\t\t\tProducts\t\t\tQty\n\t---------------------------------------------------------\n"
        
            final = RequirementList + dt + "\n" + table_header
        
            file_name =str(directory) + str (random.randrange(5000, 10000)) + ".rtf"
            f = open(file_name, 'w')
            f.write(final)
            result=c.execute("SELECT * FROM Product where MD > AQ") 
            rows = c.fetchall()
            j = 1
            for row in rows:
                self.get_name = row[1]
                self.get_AQ = row[2]
                self.get_MD = row[3]
                f.write("\n\t\t" + str(j) + "\t\t\t\t" + str(self.get_name) + "\t\t\t\t" + str(self.get_MD - self.get_AQ) + "\n")
                j += 1
            f.close()
            
            
obj=Inventory_System(root)

root.title('Household Inventory')
root.geometry('1350x700+0+0')
root.mainloop() 
