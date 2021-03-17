import mysql.connector as con

def designationdata():

    connection = con.connect(host = "localhost", user = 'root', password = '', database = 'crud tkinter')
    mycursor = connection.cursor()
    mycursor.execute("select edesignation from designation")
    courses = mycursor.fetchall()

    courselist = []

    for course in courses:
        courselist.append(course[0])
    
    # l=courselist
    # print(l)

