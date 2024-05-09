from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk


root = Tk()
root.geometry("800x800")
root.title("Employee Management System")
root.minsize(800, 800)
root.maxsize(800, 800)


# ------------All Function Connection.-------------------------

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="arshad123",
        database="mini_project"
    )
    return conn


# -------------Register function -------------------------------

def register():
    deptno = num1.get()
    dname = num2.get()
    loc = num3.get()

    conn = connect()
    c = conn.cursor()
    c.execute("insert into project values(" + deptno + ",'" + dname + "','" + loc + "')")
    conn.commit()
    tree.insert('', 'end', values=(deptno,dname,loc))

    num1.configure(state=NORMAL)
    num1.delete(0, END)
    num2.delete(0, END)
    num3.delete(0, END)
    messagebox.showinfo("Information", "Record Interested Successfully....")
    conn.close()


# -------------Show All Function --------------------------------


def showall():
    for i in tree.get_children():
        tree.delete(i)

    conn = connect()
    c = conn.cursor()
    c.execute("select * from project")
    res = c.fetchall()

    for i in res:
        tree.insert('', 'end', values=(i[0], i[1], i[2]))
    # btnS.configure(state=DISABLED)
    conn.commit()
    conn.close()

# ---------------Update Function -----------------------------------------------------------------------------


def update():
    deptno = num1.get()
    dname = num2.get()
    loc = num3.get()

    conn = connect()
    c = conn.cursor()
    c.execute("update project set dname= '%s', loc='%s' where deptno= '%s'" %(dname, loc,deptno))
    conn.commit()

    select_item = tree.selection()
    if len(select_item) == 1:
        item = select_item[0]
        tree.item(item, values=(deptno,dname,loc))
    messagebox.showinfo("info", "Update data Successfully....")
    conn.close()

    num1.configure(state=NORMAL)
    num1.delete(0, END)
    num2.delete(0, END)
    num3.delete(0, END)  

#  ------------------Show selected row -------------------------------------------------------


def show_selected_row(event):
    selected_item = tree.focus()
    values = tree.item(selected_item, 'values')

    if values:
        num1.configure(state=NORMAL)
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num1.insert(0, values[0])
        num1.configure(state=DISABLED)
        num2.insert(0, values[1])
        num3.insert(0, values[2])


# ------------- ------ Delete Function ------------------------------------------------------------------------


def delete():
    print("deleted ")
    conn = connect()
    c = conn.cursor()
    select_del = tree.focus()
    if select_del:
        values = tree.item(select_del, 'values')
        query = "delete from project where deptno = %s"
        c.execute(query, (values[0],))
        conn.commit()
        tree.delete(select_del)
    messagebox.showinfo("info", "Data delete Successfully...")
    conn.close()

    # num1.delete(0, END)
    # num2.delete(0, END)
    # num3.delete(0, END)

# ------------Clear Function ---------------------------------------------------------------------------------


def clear():
    for i in tree.get_children():
        tree.delete(i)
    num1.configure(state=NORMAL)
    num1.delete(0,END)
    num2.delete(0,END)
    num3.delete(0,END)


# --------------Search Function ------------------------------------------------------------------------------

def search():
    tree.delete(*tree.get_children())
    conn = connect()
    c = conn.cursor()
    kgn = nums.get()
    Query = "select deptno, dname, loc from project where deptno LIKE '%"+kgn+"%'"
    c.execute(Query)

    res = c.fetchall()
    for i in res:
        tree.insert('',END,values=i)
    nums.delete(0, END)

     
def exit():
    root.destroy()

# --------------------------------------------------------------------------------------------------------------

labelm = Label(root, text="Employee Management System", fg="green", font="times 15 bold", bg="yellow", bd="4", relief="raised").pack(pady=10)

lbl1 = Label(root, text="Enter Dept No : ", bg="blue", fg="white", font="times 15 bold", bd="4", relief="raised", width=20)
lbl2 = Label(root, text="Enter Department Name : ", bg="blue", fg="white", font="time 15 bold", bd="4", relief="raised", width=20)
lbl3 = Label(root, text="Enter Location : ", bg="blue", fg="white", font="times 15 bold", bd="4", relief="raised", width=20)

lbld = Label(root, text="Please select one record below to update or delete", fg="white", bg="blue", bd="4", relief="raised", font="times 15 bold").pack(pady=270)

lbls = Label(root, text="Please Enter Dept No", bg="blue", fg="white", font="times 15 bold", bd="4", relief="raised")

btnR = Button(root, text="Register", bg="yellow", font="times 10 bold", width=9, command=register)
btnU = Button(root, text="Update", bg="yellow", font="times 10 bold", width=9, command=update)
btnD = Button(root, text="Delete", bg="yellow", font="times 10 bold", width=9, command=delete)
btnC = Button(root, text="clear", bg="yellow", font="times 10 bold", width=9, command=clear)
btnS = Button(root, text="Show All", bg="yellow", font="times 10 bold", width=9, command=showall)
btnSearch = Button(root, text="Search", bg="yellow", font="times 10 bold", width=9, command=search)
btnExit = Button(root, text="Exit", bg="yellow", font="times 10 bold", width=9, command=exit)


num1 = Entry(root, width=30, bd=3, font="Arial 10 bold", fg="red")
num2 = Entry(root, width=30, bd=3, font="Arial 10 bold", fg="red")
num3 = Entry(root, width=30, bd=3, font="Arial 10 bold", fg="red")
nums = Entry(root, width=30, bd=3, font="Arial 8 bold", fg="red")   # Search Entry

lbl1.place(x=120, y=100)
num1.place(x=390, y=100, height=35)

lbl2.place(x=120, y=140)
num2.place(x=390, y=140, height=35)

lbl3.place(x=120, y=180)
num3.place(x=390, y=180, height=35)


# buttons name Register, Update, Delete, Clear, ShowAll --------

btnR.place(x=100, y=250)
btnU.place(x=230, y=250)
btnD.place(x=360, y=250)
btnC.place(x=490, y=250)
btnS.place(x=620, y=250)

# btn search and exit place..---------------------------------

btnSearch.place(x=620, y=630)
btnExit.place(x=100, y=630)

# please enter deptno label and entry place...----------------

lbls.place(x=200, y=630)
nums.place(x=420, y=630, height=35)

# ------------TreeView ----------------------------

# style = ttk.Style()
# style.configure("Treeview.heading", font=("Arial bold 15"))

columns = ('deptno', 'dname', 'loc')
tree = ttk.Treeview(root, columns=columns, show='headings')

tree.heading('deptno', text='DeptNo')
tree.heading('dname', text='DName')
tree.heading('loc', text='Location')

tree.place(x=100, y=370)
tree.bind("<<TreeviewSelect>>",show_selected_row)

# ------Vertical Scroll bar--------------------------------

vsb = ttk.Scrollbar(root, orient="vertical")
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y, side=RIGHT)
vsb.place(x=710, y=370)


root.mainloop()