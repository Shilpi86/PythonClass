from mysql import connector

class Table:
    def __init__(self, host, user, password, database):
        self.myDbConnection = connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.c1 = self.myDbConnection.cursor()

    #def create_table(self):
        #self.c1.execute("CREATE TABLE School (name VARCHAR(20), class INT, grades INT)")
        #self.myDbConnection.commit()

    def insert(self):
        self.c1.execute("INSERT INTO School VALUES ('wik', 7, 90)")
        self.c1.execute("INSERT INTO School VALUES ('Sam', 5, 92)")
        self.myDbConnection.commit()
        print(f"{self.c1}")

    def update(self):
        self.c1.execute("update stud set marks=92 where name='wik'")
        self.myDbConnection.commit()


    def alter(self):
         self.c1.execute("alter table stud add age")
         self.myDbConnection.close()

    def select(self):
        self.c1.excecute("select * from stud")
        result = self.c1.fetchall()
        print(result)
        self.myDbConnection.close()
    def close_connection(self):
        self.myDbConnection.close()

# Initialize the Table class with your database credentials
db = Table(host='localhost', user='root', password='Amyra262017', database='pythonclass') # Create the "School" table
#db.create_table()

# Insert data into the "School" table
db.insert()

# Close the database connection when done
db.close_connection()
