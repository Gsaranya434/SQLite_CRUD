from table_creation import GoogleContact


class call:
    def __init__(self, object):
        self.obj = object

    def main(self):
        get_user = input('what operation we need to perform on database [1.create, 2.read, 3.update,4.delete] : ')
        if get_user == '1':
            get_data = self.obj.get_user_info()
            create_row = self.obj.create_sql_table()
            if create_row:
                print('Success')
        elif get_user == '2':
            read_row = self.obj.read_sql_table()
            print(read_row)
        elif get_user == '3':
            update_row = self.obj.update_sql_table()
        elif get_user == '4':
            delete_row = self.obj.delete_sql_table()
        else:
            print('Process Finished')
        return self.main()


if __name__ == '__main__':
    DBName = input("Enter DB Name: ")
    sqlobj = GoogleContact(DBName)
    obj = call(sqlobj)
    obj.main()

