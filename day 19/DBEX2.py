#complete dynamic way from mysql import connector
from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='Amyra262017', database = "pythonclass")

print(myDbConnection)
c1 = myDbConnection.cursor()
vempno = int(input("Enter the employee number: "))
vempname = input("Enter the name of employee: ")
vempsalary = int(input("Enter the salary of employee: "))
c1.execute("insert into employee (empno, empname, sal) values(%s,%s,%s)",(vempno, vempname, vempsalary))
c1.execute("delete from emp where emp_no=105")
c1.execute("delete from employee where emp_no=104")
myDbConnection.commit()
myDbConnection.close()
