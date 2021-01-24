###################################################
#<><><><><><<><><><><><><><><><><><><><><><><><><>#
#                                                 #
#        CRUDE (Create,Read,Update,Delete)        #
#                Employee_Master                  #
#                                                 #
#<><><><><><<><><><><><><><><><><><><><><><><><><>#
###################################################

import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
# import designationtb
# from designationtb import designationdata
# import sys



#################################
#      Create Window Strat      #
#################################
win = tk.Tk()
win.title("CRUD")
win.geometry("481x620")
win.resizable(0, 0)
win.configure(bg='#FFDB58')
#################################
#      Create Window End        #
#################################



##############################################
#      Connection With database Start        #
##############################################
import mysql.connector as con 

my_connection = con.connect(host = "localhost", user = 'root', password = '', database = 'crud tkinter')
mycursor = my_connection.cursor()

# my_connection.execute("Create database crud tkinter")

# my_connection.execute("CREATE TABLE employee_master (id INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(255), eaddress VARCHAR(255), ecity VARCHAR(255), ebdate VARCHAR(255), emonthlysalary VARCHAR(255) , eclass VARCHAR(255) , egender VARCHAR(255) , edesignation VARCHAR(255))")

# my_connection.execute("CREATE TABLE designation (id INT AUTO_INCREMENT PRIMARY KEY, edesignation VARCHAR(255))")



##############################################
#        Connection With database End        #
##############################################



########################################
#     sql code for combo box  Start    #
########################################
mycursor.execute("select edesignation from designation")
courses = mycursor.fetchall()
courselist = []
cuslit = courselist

for course in courses:
    courselist.append(course[0])
########################################
#     sql code for combo box  End      #
########################################



# get emp value #
empid            = tk.StringVar()
empname          = tk.StringVar()
empaddress       = tk.StringVar()
empcity          = tk.StringVar()
empbday          = tk.StringVar()
empmonthlysalary = tk.StringVar()
empclass         = tk.StringVar()
empgender        = tk.StringVar()
skill            = tk.StringVar()

# empclassss = empclass.get()
# print(empclassss) 

#################################
#      Insert Data Start        #
#################################
def insertData():
    # deleteBtn.configure(state=DISABLED)
    
    iidd = empid.get()
    name    = empname.get()
    address =empaddress.get()
    city = empcity.get()
    bday = empbday.get()
    monthlysalary = empmonthlysalary.get()
    classs = empclass.get()
    gender = empgender.get()  
    cl = skill.get()
    # print(classs)
    # if (name == '' and address == '' and city == '' and bday == '' and monthlysalary == '' or
        #     name == name and address == '' and city == '' and bday == '' and monthlysalary == '' or
        #     name == name and address == address and city == '' and bday == '' and monthlysalary == '' or
        #     name == name and address == address and city == city and bday == '' and monthlysalary == '' or
        #     name == name and address == address and city == city and bday == bday and monthlysalary == '' or
        #     name == '' and address == address and city == city and bday == bday and monthlysalary == monthlysalary or
        #     name == '' and address == '' and city == city and bday == bday and monthlysalary == monthlysalary or
        #     name == '' and address == '' and city == '' and bday== bday and monthlysalary == monthlysalary or
        #     name == '' and address == '' and city == '' and bday == '' and monthlysalary == monthlysalary or
        #     name == name and address == '' and city == city and bday == bday and monthlysalary == monthlysalary or
        #     name == name and address == address and city == '' and bday == bday and monthlysalary == monthlysalary or
        #     name == name and address == address and city == city and bday == '' and monthlysalary == monthlysalary or
        #     name == name and address == address and city == city and bday == bday and monthlysalary == '' or
        #     name == '' and address == address and city == ''  and bday == '' and monthlysalary == '' or
        #     name == name and address == '' and city == city and bday == '' and monthlysalary == monthlysalary or
        #     name == '' and address == address and city == '' and bday == '' and monthlysalary == '' or
        #     name == '' and address == '' and city == city and bday == '' and monthlysalary == '' or
        #     name == '' and address == '' and city == '' and bday == bday and monthlysalary == '' or
        #     name == '' and address == '' and city == city and bday == '' and monthlysalary == monthlysalary or
        #     name == name and address == '' and city == city and bday == '' and monthlysalary == '' or 
        #     name == name and address == address and city == city and bday == bday and monthlysalary == monthlysalary and cl == "select skill"):
    if (name == '' or address == '' or city == '' or bday == '' or monthlysalary == '' or cl == "select skill" or classs == '' or gender == '' ):
        messagebox.showinfo("opps!", "please entry value..")
    
    elif (idonoff['text'] == 'Off' or iidd != ''):
        messagebox.showwarning("Warning", "Trun off Id Button and Clear Employee Id Value")


    else:
        mycursor.execute('INSERT INTO employee_master (ename, eaddress, ecity, ebdate, emonthlysalary, eclass, egender, edesignation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (name, address, city, bday, monthlysalary, classs, gender, cl))
        messagebox.showinfo("wow!", "Emplopyee data Entered Successfully..")
        addBtn.configure(state=DISABLED)
        my_connection.commit()

        # mycursor.execute('select Firstname from student ORDER BY id DESC LIMIT 1')
        # firststudent = mycursor.fetchone()
        # setsucess = labels.set("Data Insert Sucessfully of :"+str(firststudent))
#################################
#      Insert Data End          #
#################################



######################################
#        Clear Entry Box Start       #
######################################
def clearall():
    empid.set("")
    empname.set("")
    empaddress.set("")
    empcity.set("")
    empbday.set("")
    empmonthlysalary.set("")
    empclass.set("")
    empgender.set("")
    skill.set("select skill")
    addBtn.configure(state=NORMAL)
#####################################
#        Clear Entry Box Start      #
#####################################



########################################
#        Display Frist Data Start      #
########################################
def fDisplay():

    addBtn.configure(state=DISABLED)
    try: 
        mycursor.execute("SELECT id FROM employee_master ORDER BY id ASC LIMIT 1")
        ei = mycursor.fetchone()
        empid.set(str(ei[0]))

        mycursor.execute("SELECT ename FROM employee_master ORDER BY id ASC LIMIT 1")
        en = mycursor.fetchone()
        empname.set(str(en[0]+' '))
        
        mycursor.execute("SELECT eaddress FROM employee_master ORDER BY id ASC LIMIT 1")
        ea = mycursor.fetchone()
        empaddress.set(str(ea[0]+' '))
        
        mycursor.execute("SELECT ecity FROM employee_master ORDER BY id ASC LIMIT 1")
        eci = mycursor.fetchone()
        empcity.set(str(eci[0]+' '))
        
        mycursor.execute("SELECT ebdate FROM employee_master ORDER BY id ASC LIMIT 1")
        ebd = mycursor.fetchone()
        empbday.set(str(ebd[0]+' '))
        
        mycursor.execute("SELECT emonthlysalary FROM employee_master ORDER BY id ASC LIMIT 1")
        ems = mycursor.fetchone()
        empmonthlysalary.set(str(ems[0]+' '))
        
        mycursor.execute("SELECT eclass FROM employee_master ORDER BY id ASC LIMIT 1")
        ecl = mycursor.fetchone()
        empclass.set(ecl)
        
        mycursor.execute("SELECT egender FROM employee_master ORDER BY id ASC LIMIT 1")
        eg = mycursor.fetchone()
        empgender.set(eg)
        
        mycursor.execute("SELECT edesignation FROM employee_master ORDER BY id ASC LIMIT 1")
        edes = mycursor.fetchone()
        skill.set(str(edes[0]+' '))

        my_connection.commit()

    except:
        messagebox.showinfo("opps!!", "No Data Found..")
########################################
#        Display Frist Data Start      #
########################################



########################################
#       Display Last Data Start        #
########################################
def lDisplay():
    addBtn.configure(state=DISABLED)
    try:
        mycursor.execute("SELECT id FROM employee_master ORDER BY id DESC LIMIT 1")
        ei = mycursor.fetchone()
        empid.set(str(ei[0]))
        
        mycursor.execute("SELECT ename FROM employee_master ORDER BY id DESC LIMIT 1")
        en = mycursor.fetchone()
        empname.set(str(en[0]+' '))
        
        mycursor.execute("SELECT eaddress FROM employee_master ORDER BY id DESC LIMIT 1")
        ea = mycursor.fetchone()
        empaddress.set(str(ea[0]+' '))
        
        mycursor.execute("SELECT ecity FROM employee_master ORDER BY id DESC LIMIT 1")
        eci = mycursor.fetchone()
        empcity.set(str(eci[0]+' '))
        
        mycursor.execute("SELECT ebdate FROM employee_master ORDER BY id DESC LIMIT 1")
        ebd = mycursor.fetchone()
        empbday.set(str(ebd[0]+' '))
        
        mycursor.execute("SELECT emonthlysalary FROM employee_master ORDER BY id DESC LIMIT 1")
        ems = mycursor.fetchone()
        empmonthlysalary.set(str(ems[0]+' '))
        
        mycursor.execute("SELECT eclass FROM employee_master ORDER BY id DESC LIMIT 1")
        ecl = mycursor.fetchone()
        empclass.set(ecl)
        
        mycursor.execute("SELECT egender FROM employee_master ORDER BY id DESC LIMIT 1")
        eg = mycursor.fetchone()
        empgender.set(eg)
        
        mycursor.execute("SELECT edesignation FROM employee_master ORDER BY id DESC LIMIT 1")
        edes = mycursor.fetchone()
        skill.set(str(edes[0]+' '))

        my_connection.commit()

    except:
        messagebox.showinfo("opps!!", "No Data Found..")
########################################
#        Display Last Data End         #
########################################





########################################
#        Delete Emp Data Start         #
########################################
def deletee():
    idd = empid.get()
    dname = empname.get()
    my_var = messagebox.askyesno("Delete ?", "Delete id: "+str(idd), icon='warning', default='no')

    if  idd !='' and my_var: # True if yes button is clicked
        mycursor.execute("DELETE FROM employee_master WHERE id= " + str(idd) )
        if dname != '':
            messagebox.showinfo("Deleted","Employee Id : "+ str(idd) + "   Employee Name :  " + str(dname) + "  Delete Successfully..")
        else:
            messagebox.showinfo("Deleted", "Employee Id :" + str (idd) + " Delete Successfully..")
        my_connection.commit()
    else:
        pass      
########################################
#        Delete Emp Data End           #
########################################



########################################
#        UPadate Emp Data Star         #
########################################
def updateData():
    sql_cmd  = """UPDATE employee_master SET ename = %s, eaddress = %s, ecity = %s, ebdate = %s, emonthlysalary = %s, eclass = %s, egender = %s, edesignation = %s WHERE id =  %s"""

    uname    = empname.get()
    uaddress =empaddress.get()
    ucity = empcity.get()
    ubday = empbday.get()
    umonthlysalary = empmonthlysalary.get()
    uclasss = empclass.get()
    ugender = empgender.get()  
    ucl = skill.get()
    uiidd = empid.get()

    inputs = (uname, uaddress, ucity, ubday, umonthlysalary, uclasss, ugender, ucl, uiidd)
    mycursor.execute(sql_cmd, inputs)

    messagebox.showinfo("Update", "Data Update Successfully")
    my_connection.commit()
########################################
#        UPadate Emp Data Star         #
########################################



#########################
#      MenuBar          #
#########################
def exitshorcut(self):
    print("quitting...")
    # sys.exit(0) # win.exit()
    win.destroy()
# Menubar #
menubar = Menu(win) 
menubar.add_cascade(label ='Exit', command=win.destroy, accelerator="Ctrl+i",underline=2) #add menu
win.config(menu=menubar) #display menu on screen
win.bind_all("<Control-i>",exitshorcut) # Shortcut 
#########################
#      MenuBar          #
#########################


###############################
#     On Off Id Btn Strat     #
###############################
def onOff(buttons):
    if buttons["text"] == "On":
        inputempid.configure(state=NORMAL)
        buttons["text"] = "Off"
    elif buttons ["text"] == "Off":
        buttons["text"] = "On"
        inputempid.configure(state=DISABLED)
################################
#      On Off Id Btn  End      #
################################
        


buttons = StringVar()
idonoff = Button(win, text = "On",command=lambda : onOff(idonoff), font="arial 11 normal", bg="green", bd=0) 
idonoff.place(x=415, y=52)



# Employee Title, Name, ADdress, City, Birth-Date, Monthly-Salary, Class, Gender, Designationdata Lable #
Label(win, text="Employee Master" ,width=40, height=1 , fg='#0C090A', bg='#FDD017', font='Times 20 ').pack()
Label(win, text="Employee Id           : "            , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=50)
Label(win, text="Employee Name     : "                , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=100)
Label(win, text="Employee Address : "                 , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=150)
Label(win, text="City                        : "     , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=200)
Label(win, text="Birth Date              : "          , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=250)
Label(win, text="Monthly Salary      : "              , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=300)
Label(win, text="Class                     : "      , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=350)
Label(win, text="Gender                  : "         , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=400)
Label(win, text="Designation           : "           , fg='#0C090A', bg='#FFDB58', font='Times 15 ').place(x=10, y=450) 

# Employee Name, ADdress, City, Birth-Date, Monthly-Salary Inputbox #
inputempid      = Entry(win, textvariable=empid,           width="20",font="arial 15 normal", bg="#FFDB58", bd=1, state=DISABLED) 
inputempid.place(x=190, y=52)
inputempname    = Entry(win, textvariable=empname,         width="20",font="arial 15 normal", bg="#FFDB58", bd=1) 
inputempname.place(x=190, y=102)
inputempadd     = Entry(win, textvariable=empaddress,      width="20",font="arial 15 normal", bg="#FFDB58", bd=1) 
inputempadd.place(x=190, y=152)
inputempcity    = Entry(win, textvariable=empcity,         width="20",font="arial 15 normal", bg="#FFDB58", bd=1) 
inputempcity.place(x=190, y=202)
inputempbday    = Entry(win, textvariable=empbday,         width="20",font="arial 15 normal", bg="#FFDB58", bd=1) 
inputempbday.place(x=190, y=252)
inputempmsalary = Entry(win,textvariable=empmonthlysalary, width="20",font="arial 15 normal", bg="#FFDB58", bd=1) 
inputempmsalary.place(x=190, y=302)

# Employee Class #
Radiobutton(win, text="Class I",   bg='#FFDB58', variable=empclass, activebackground="#ffdc58", value='Class_I',   font='arial 11', command=None).place(x=190, y=343)
Radiobutton(win, text="Class II",  bg='#FFDB58', variable=empclass, activebackground="#ffdc58", value='Class_II',  font='arial 11', command=None).place(x=280, y=343)
Radiobutton(win, text="Class III", bg='#FFDB58', variable=empclass, activebackground="#ffdc58", value='Class_III', font='arial 11', command=None).place(x=190, y=366)
Radiobutton(win, text="Class IV",  bg='#FFDB58', variable=empclass, activebackground="#ffdc58", value='Class_IV',  font='arial 11', command=None).place(x=280, y=366)

# Employee Gender #
Radiobutton(win, text="Male",   bg='#FFDB58', variable=empgender, activebackground="#ffdc58", value='Male',   font='arial 11', command=None).place(x=190, y=403)
Radiobutton(win, text="Female", bg='#FFDB58', variable=empgender, activebackground="#ffdc58", value='Female', font='arial 11', command=None).place(x=260, y=403)
Radiobutton(win, text="Other",  bg='#FFDB58', variable=empgender, activebackground="#ffdc58", value='Other',  font='arial 11', command=None).place(x=350, y=403)

#combo box
mycombo = Combobox(win, width=20,font='Times 15 ', textvariable = skill)
mycombo['values'] = courselist
mycombo.current(0)
mycombo.place(x=190, y=452)

# Employee Data Frist, Previous, Next, Last Button #
Button(win, command=fDisplay, text="First",    font=("times",14), width=8, bg="#41A317", activeforeground="#fff", activebackground="#52D017", foreground="white",  bd=0).place(x=15, y=510)
Button(win, command=None, text="Next", font=("times",14), width=8, bg="#41A317", activeforeground="#fff", activebackground="#52D017", foreground="white",  bd=0).place(x=135, y=510)
Button(win, command=None, text="Previous",     font=("times",14), width=8, bg="#41A317", activeforeground="#fff", activebackground="#52D017", foreground="white",  bd=0).place(x=255, y=510)
Button(win, command=lDisplay, text="Last",     font=("times",14), width=8, bg="#41A317", activeforeground="#fff", activebackground="#52D017", foreground="white",  bd=0).place(x=375, y=510)

# Employee Data Add, Update, Delete, Clear Button #
addBtn = Button(win, command=insertData, text="Add New", font=("ARIAL",14), width=8, activebackground="#FFF380", bg="#FFF8C6",bd=0)
addBtn.place(x=10,  y=570)

updateBtn = Button(win, command=updateData, text="Update",  font=("ARIAL",14), width=8, activebackground="#FFF380", bg="#FFF8C6",bd=0)
updateBtn.place(x=130, y=570)

deleteBtn = Button(win, command=deletee, text="Delete",  font=("ARIAL",14), width=8, activebackground="#FFF380", bg="#FFF8C6",bd=0)
deleteBtn.place(x=250, y=570)

clearbtn = Button(win, command=clearall, text="Clear",   font=("ARIAL",14), width=8, activebackground="#ffffff", bg="#FF2400",bd=0, foreground="white",activeforeground="#FF0000")
clearbtn.place(x=370, y=570)





win.mainloop()
