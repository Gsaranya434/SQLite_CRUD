import sqlite3
from datetime import datetime

# class for only SQL
class SQlite_crud():
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname+'.db')
        self.curr = self.connection.cursor()
        self.contact_info = {}

    # function get_user_info() will collect data from the terminal
    def get_user_info(self):
        fields = ['Name', 'Gmail', 'Location', 'Mobile_Number']
        for x in fields:
            get = input(x + ': ')
            self.contact_info.update({x: get})

# function create_sql_table() will create the SQL and dictionary values will append into database
    def create_sql_table(self):
        try:
            self.connection.execute('''CREATE TABLE Contact
                     (Id INTEGER NOT NULL CONSTRAINT Contact PRIMARY KEY AUTOINCREMENT,
                      Name          TEXT    NOT NULL,
                      Gmail         TEXT    NOT NULL,
                      Area          CHAR,
                      Phone_Number   INT,
                      Date           INT);''')
        except Exception as err:
            return err
        finally:
            tuple_conv = tuple(self.contact_info.values())
            self.now = datetime.now()
            date_new = self.now.strftime('%D:%H:%M')
            new = 'INSERT INTO Contact(Name, Gmail, Area, Phone_Number, Date) VALUES (?,?,?,?,?);'
            self.curr.execute(new, (tuple_conv[0], tuple_conv[1], tuple_conv[2], tuple_conv[3], date_new))
            self.connection.commit()
            return True

    def repeated_act(self):
        self.curr.execute('SELECT * FROM Contact')
        print(self.curr.fetchall())
        Id = input('enter the particular ID,which you want :')
        return Id

    # read_sql_table() will reads the all ROW and based on the ID it will print the row data
    def read_sql_table(self):
        try:
            result = self.repeated_act()
            rows = self.curr.execute(f'SELECT * FROM Contact WHERE Id={result}').fetchall()
        except Exception as err:
             return err
        finally:
            return rows

# based on the user entered ID ,it will delete the ROW from the database table
    def delete_sql_table(self):
        try:
            result = self.repeated_act()
            self.curr.execute(f'DELETE FROM Contact WHERE Id = {result}')
            self.connection.commit()
        except Exception as err:
            return err
        finally:
            return True

# get_update() function will update/set the specific row based on the ID
    def get_update(self,tuple_data, Id):
        try:
            date_new = self.now.strftime('%D:%H:%M')
            self.curr.execute('UPDATE Contact SET Name = ?, Gmail = ?, Area = ?, Phone_Number = ?, Date = ? WHERE Id = ?;',(tuple_data[0], tuple_data[1], tuple_data[1], tuple_data[2], date_new, Id))
            self.connection.commit()
        except Exception as err:
            return err
        finally:
            return True

# this function will does the getting user info and converted into a tuple_data format and given to get_update()
    def update_sql_table(self):
        try:
            result = self.repeated_act()
            self.get_user_info()
            tuple_conv = tuple(self.contact_info.values())
            self.get_update(tuple_conv, result)
        except Exception as err:
            return err


class GoogleContact(SQlite_crud):
    def get_user_info(self):
        pass
