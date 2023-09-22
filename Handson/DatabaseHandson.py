from mysql import connector
class Table: #within the class not outside of the class.
    global myDbConnection
    myDbconnection=connector.connect (host="Localhost", user= "root", password= "Amyra262017", database= "pythonclass")
    global c1 #when you want to access the variable outside of the function (globally) this should be used
    c1=myDbconnection.cursor()
    def create(self): # create is DDL operation not DRL , you do not need commit or close function
        c1. execute("create Table BUS (name varchar (20), class int, school varchar(20))")

    def insert(self):
        c1.insert("insert into BUS values ('wik', 7, 'nelson')")
        c1.insert("insert into BUS values('Sam', 8, 'carriage')")
        myDbConnection.commit()
        myDbConnection.close()

    def select(self):
        c1.excecute("select * from BUS")
        result=fetchall()
        print(result)

obj1 = Table()
obj1.create ()