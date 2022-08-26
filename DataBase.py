from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from os import remove
from sqlite3.dbapi2 import Cursor, connect

root = Tk()
root.title("DataBase System")
root.iconbitmap("E:/Python Tkinter/images/portfolio1.jpg")
root.resizable(0,0)
# root.geometry("400x600")

# create a database or connect to one
conn = sqlite3.connect("database.db")

# create cursor
# any operation on database is done by cursor
c = conn.cursor()


# #this is important part of the system......
# create tables
# c.execute("""CREATE TABLE addresses ( 
#     first_name text, 
#     last_name text, 
#     address text, 
#     city text, 
#     state text,
#     zipcode integer
# )""")


# getting wierd formatting because every time u call query() from "Show records" you create a new label on top of the old one.
# to avoid this problem we declare the label global here and in fun we just update the msg 
query_label = Label(root, text="")


#create query fun
def query():
    # we have to connect the database and create the Cursor inside the function also
    # otherwise it will not give the desired output...
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    # query the database
    c.execute("SELECT *, oid FROM addresses")   #oid is the primary key...
    records = c.fetchall()
    # print(records)

    # loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t"*2 + str(record[6]) + "\n"
    
    query_label.config(text=print_records)
    # query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2 )

    conn.commit()
    conn.close()

    status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
    status.grid(row=13, column=0, columnspan=3, sticky=W+E)

    # clearing the select ID entry...
    delete_box.delete(0, END)



def update():

    if len(f_name_editor.get()) != 0 or len(l_name_editor.get()) != 0 or len(address_editor.get()) != 0 or len(city_editor.get()) != 0 or len(state_editor.get()) != 0 or len(zipcode_editor.get()) != 0: 

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        print("its runnning")
        record_id = delete_box.get()
        c.execute("""UPDATE addresses SET
                first_name = :first, 
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                
                WHERE oid = :oid""",
                {
                "first" : f_name_editor.get(),
                "last" : l_name_editor.get(),
                "address" : address_editor.get(),
                "city" : city_editor.get(),
                "state" : state_editor.get(),
                "zipcode" : zipcode_editor.get(),

                "oid" : record_id

                })

        conn.commit()
        conn.close()
        query()

        status = Label(root, text="ID Updated", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)
    
    else:
        print("error occured")
        status = Label(root, text="Records can't be Empty", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)

        # clearing the select ID entry...
    delete_box.delete(0, END)
    editor.destroy()


# create a function to update a record...
def edit():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    # if select ID is empty then update window will not open
    if delete_box.get().isnumeric():
        #--------------------------------
        c.execute("SELECT *, oid FROM addresses")   #oid is the primary key...
        records = c.fetchall()
        for record in records:
            if delete_box.get() == str(record[6]):
                find_records = 1
                break
            else:
                find_records = 2

        if find_records == 1:
            #--------------------------------
            global editor
            editor = Tk()
            editor.title("Update A Record")
            editor.iconbitmap("E:/Python Tkinter/images/portfolio1.jpg")
            # editor.geometry("400x600")

            # conn = sqlite3.connect("database.db")
            # c = conn.cursor()

            record_id = delete_box.get()
            # query the database
            c.execute("SELECT *, oid FROM addresses WHERE oid = " + record_id) #oid is the primary key...
            records = c.fetchall()
                

            #create global variables for text box names
            global f_name_editor
            global l_name_editor
            global address_editor
            global city_editor
            global state_editor
            global zipcode_editor


            #create text boxes
            f_name_editor = Entry(editor, width = 30, borderwidth=3)
            f_name_editor.grid(row=0, column=1, padx=20, pady=(20, 0))

            l_name_editor = Entry(editor, width = 30, borderwidth=3)
            l_name_editor.grid(row=1, column=1, pady=(5, 0))

            address_editor = Entry(editor, width = 30, borderwidth=3)
            address_editor.grid(row=2, column=1, pady=(5, 0))

            city_editor = Entry(editor, width = 30, borderwidth=3)
            city_editor.grid(row=3, column=1, pady=(5, 0))

            state_editor = Entry(editor, width = 30, borderwidth=3)
            state_editor.grid(row=4, column=1, pady=(5, 0))

            zipcode_editor = Entry(editor, width = 30, borderwidth=3)
            zipcode_editor.grid(row=5, column=1, pady=(5, 10))


            # create text box label 
            f_name_label = Label(editor, text="First Name")
            f_name_label.grid(row=0, column=0, pady=(20, 0))

            l_name_label = Label(editor, text="Last Name")
            l_name_label.grid(row=1, column=0)

            address_label = Label(editor, text="Address")
            address_label.grid(row=2, column=0)

            city_label = Label(editor, text="City")
            city_label.grid(row=3, column=0)

            state_label = Label(editor, text="State")
            state_label.grid(row=4, column=0)

            zipcode_label = Label(editor, text="Zipcode")
            zipcode_label.grid(row=5, column=0, pady=(0, 10))

        
            # loop through results
            for record in records:
                f_name_editor.insert(0, record[0])    
                l_name_editor.insert(0, record[1])    
                address_editor.insert(0, record[2])    
                city_editor.insert(0, record[3])    
                state_editor.insert(0, record[4])    
                zipcode_editor.insert(0, record[5])    

            # create a Save button 
            edit_btn = Button(editor, text="Save Record", command=update, pady=3)
            edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=143)

            # conn.commit()
            # conn.close()
            # print("numeric")
            status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
            status.grid(row=13, column=0, columnspan=3, sticky=W+E)
            
        else:
            statustext = "ID Not Found"
            status = Label(root, text=statustext, bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
            status.grid(row=13, column=0, columnspan=3, sticky=W+E)
        conn.commit()
        conn.close()
    # we have to use if-elif-else here otherwise it will prints the else condition too
    # even 'if' conition is true...
    elif len(delete_box.get()) == 0:
        # shows the status...
        status = Label(root, text="Select ID First", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)

    else:
        # shows the status...
        status = Label(root, text="Enter Numerics Only", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)



# create a function to delete a record
def delete():
    # we have to connect the database and create the Cursor inside the function also
    # otherwise it will not give the desired output...
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    if delete_box.get().isnumeric():
        # #--------------------------------
        c.execute("SELECT *, oid FROM addresses")   #oid is the primary key...
        records = c.fetchall()
        for record in records:
            if delete_box.get() == str(record[6]):
                find_records = 1
                break
            else:
                find_records = 2

        if find_records == 1:
        #--------------------------------
            c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())
            statusText = "ID Deleted"
        else:
            statusText = "ID Not Found"


    elif len(delete_box.get()) == 0:
        statusText = "Select ID First"
            
    else:
        statusText = "Enter Numerics Only"
            
    conn.commit()
    conn.close()

    # updating the remaning list...
    query()

    status = Label(root, text=statusText, bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
    status.grid(row=13, column=0, columnspan=3, sticky=W+E)

    # clearing the select ID entry...
    delete_box.delete(0, END)



#create submit function for the database...
def submit():
    # we have to connect the database and create the Cursor inside the function also
    # otherwise it will not give the desired output...
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    #insert into Table
    # checking if it is Empty or not
    if len(f_name.get()) == 0 and len(l_name.get()) == 0 and len(address.get()) == 0 and len(city.get()) == 0 and len(state.get()) == 0 and len(zipcode.get()) == 0 :
        status = Label(root, text="Enter the Information", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)

    else :
        #insert into Table
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
                {
                    "f_name" : f_name.get(),
                    "l_name" : l_name.get(),
                    "address" : address.get(),
                    "city" : city.get(),
                    "state" : state.get(),
                    "zipcode" : zipcode.get()
                })
        
        status = Label(root, text="Information Added", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
        status.grid(row=13, column=0, columnspan=3, sticky=W+E)

    conn.commit()
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # clearing the select ID entry...
    delete_box.delete(0, END)



#create text boxes
f_name = Entry(root, width = 30, borderwidth=3)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width = 30, borderwidth=3)
l_name.grid(row=1, column=1, pady=(5, 0))

address = Entry(root, width = 30, borderwidth=3)
address.grid(row=2, column=1, pady=(5, 0))

city = Entry(root, width = 30, borderwidth=3)
city.grid(row=3, column=1, pady=(5, 0))

state = Entry(root, width = 30, borderwidth=3)
state.grid(row=4, column=1, pady=(5, 0))

zipcode = Entry(root, width = 30, borderwidth=3)
zipcode.grid(row=5, column=1, pady=(5, 0))

delete_box = Entry(root, width=30, borderwidth=3)
delete_box.grid(row=9, column=1, pady=5)


# create text box label 
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(5, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0, pady=(5, 0))

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0, pady=(5, 0))

city_label = Label(root, text="City")
city_label.grid(row=3, column=0, pady=(5, 0))

state_label = Label(root, text="State")
state_label.grid(row=4, column=0, pady=(5, 0))

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0, pady=(5, 0))

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)


#create submit button
submit_btn = Button(root, text="Add Record to the DataBase", command=submit, pady=3)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


#create a query button
query_btn = Button(root, text="Show Records", command=query, pady=3)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)


# create a delete button 
delete_btn = Button(root, text="Delete Record", command=delete, pady=3)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# create a Update button 
edit_btn = Button(root, text="Edit Record", command=edit, pady=3)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=143)

# shows the status...
status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W, padx=10, pady=3)
status.grid(row=13, column=0, columnspan=3, sticky=W+E)


# commit connection 
conn.commit()

# close connection
conn.close()

root.mainloop()