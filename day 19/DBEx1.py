from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='Amyra262017', database = "pythonclass")

print(myDbConnection)

#cursor = a pointer which locates processing area or temporary memory area
c1 = myDbConnection.cursor()
#when you do the execution. it connects to the dbase, access the table from there all the rows and columns will be retrieved.
#but where the data will be processed???
#data will not be processed on the dbase directly. Separate processing area will be there and the processing gets copied,
# from there record by record , data will be processed, then that cursor locates the processing area
#c1.execute("drop table if exists emp")
#c1.execute("create table emp(emp_no int, emp_name varchar(20), emp_address varchar(30))") #static way
#c1.execute("insert into employee values (101,'ricky',2000)")
#c1.execute("insert into employee values (102,'pinky',5000)")
#c1.execute("insert into employee values (103,'chicky',10000)") (OR)
sql = "insert into employee values(%s,%s,%s)"
data = (104,'jacky',20000) #partial dynamic way of writing
c1.execute(sql,data)
myDbConnection.commit()
myDbConnection.close()

