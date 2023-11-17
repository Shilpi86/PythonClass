#to establish connection : pip install mysql-connector-python

from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='rootroot')
print(myDbConnection)