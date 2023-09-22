
#fetching data from the dabase to the pycharm
from mysql import connector
myDbConnection = connector.connect(host='localhost', user='root', password='Amyra262017', database="pythonclass")

c1 = myDbConnection.cursor()
c1.execute("select * from Stationary ")

#result = c1.fetchall()  # or fetchone or fetchmany(size=2)
#result = c1.fetchmany(size=2)
result = c1.fetchone()
for i in result:
    print(i)
myDbConnection.close()
