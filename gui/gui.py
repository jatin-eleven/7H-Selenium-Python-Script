from itertools import count
from tkinter import *



root = Tk()
root.title("Free Paid Segregation System")

root.resizable(0,0)
root.configure(background='black')


#create submit function for the database...
def submit():
    link = a.get()
    free = b.get()
    paid = c.get()
    
    count = d.get()
    
    return link,free,paid,count


#create text boxes
a = Entry(root, width = 30, borderwidth=0)
a.grid(row=0, column=1, padx=40, pady=(15, 0))

b = Entry(root, width = 30, borderwidth=0)
b.grid(row=1, column=1, pady=(5, 0))

c = Entry(root, width = 30, borderwidth=0)
c.grid(row=2, column=1, pady=(5, 0))

d = Entry(root, width = 30, borderwidth=0)
d.grid(row=3, column=1, pady=(5, 0))



# create text box label 
a_label = Label(root, text="Project Link", bg="black", fg="white")
a_label.grid(row=0, column=0, pady=(20, 5))

b_label = Label(root, text="Free Project Name" , bg="black", fg="white")
b_label.grid(row=1, column=0, pady=(10, 10), padx=(34, 0))

c_label = Label(root, text="Paid Project Name" , bg="black", fg="white")
c_label.grid(row=2, column=0, pady=(10, 10), padx=(34, 0))

d_label = Label(root, text="Project Count" , bg="black", fg="white")
d_label.grid(row=3, column=0, pady=(10, 10), padx=(10, 0))

 

#create submit button
submit_btn = Button(root, text="Start Automation", command=submit, pady=3, padx=15, bg="white")
submit_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=20, ipadx=100)


root.mainloop()