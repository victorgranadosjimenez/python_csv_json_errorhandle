import pyodbc
import json

class North_Wind:
    def __init__(self):
        self.server = "localhost,1433"
        self.database_name = "NorthWind"
        self.user_name = "SA"
        self.password = "Passw0rd2018"
        self.connection = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                                        'SERVER=' + self.server + ';'
                                                        'DATABASE=' + self.database_name + ';'
                                                        'UID=' + self.user_name + ';'
                                                        'PWD=' + self.password)
        self.my_northwind_cursor = self.connection.cursor()


    def print_result_set(self, result_set):
        for item in result_set:
            print(item)


class CRUD(North_Wind):
    def __init__(self, table_name):
        super().__init__()
        self.name = table_name

    def create_operation(self,table_name):
        if table_name == "Region":
            region_id = int(input("Enter the Region ID"))
            region_desc = input("Enter the Region Description")
            sql = "INSERT INTO {}(regionid,regiondescription) Values('{}','{}')".format(table_name, region_id,region_desc)
        elif table_name == "Categories":
            CategoryID = int(input("Enter the Category ID"))
            CategoryName = input("Enter the Category Name")
            Description = input("Type the description")
            sql = "INSERT INTO {}(CategoryID,CategoryName) Values('{}','{}','{}')".format(table_name, CategoryID,CategoryName, Description)
        elif table_name == "CustomerDemographics":
            CustomerTypeID = int(input("Enter the customer type ID"))
            CustomerDesc = input("Enter the Customer Description")
            sql = "INSERT INTO {}(CustomerTypeID,customerDescription) Values('{}','{}')".format(table_name, CustomerTypeID, CustomerDesc)
        elif table_name == "Shippers":
            ShipperID = int(input("Enter the Shipper ID"))
            CompanyName = input("Enter the Company Name")
            Phone = int(input("Enter the phone number"))
            sql = "INSERT INTO {}(ShipperID,CompanyName,phone) Values('{}','{}','{}')".format(table_name, ShipperID,CompanyName, Phone)
        else:
            print("name of table not valid, please try again")
            table_choosen = input("introduce table name")
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()
    def read_operation(self, table_name):
        result_set = self.my_northwind_cursor.execute("SELECT * FROM {}".format(table_name))
        return result_set
    def update_operation(self, table_name):
        column_changed = input("Enter column name you want to change")
        new_values = input("Enter new value")
        column_condition = input("Enter the column after where condition")
        column_condition_value = input("Enter the value for the condition")
        sql = "UPDATE {} SET {} ='{}' WHERE {} ={}".format(table_name, column_changed, new_values, column_condition, column_condition_value)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()
    def delete_operation(self, table_name):
        condition = str(input("Enter the Where condition"))
        sql = "DELETE FROM {} WHERE {}".format(table_name, condition)
        result_set = self.my_northwind_cursor.execute(sql)
        result_set.commit()

    def print_result_set(self, result_set):
        items = {}
        sql = self.my_northwind_cursor.execute("SELECT * FROM region")
        for row in sql:
            print(type(result_set))
            for value in row:
                items[value[0]] = value[1]
                print(items)

        with open("Region.JSON", "w") as json_files:
            json.dump(items, json_files)
