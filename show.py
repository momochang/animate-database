#select all tables of database
def list_table(cursor, mysqldb):
    cursor.execute("show tables")
    #using for loop to fetch all of database tables.
    #Why using table[0], Not table? Because table result is ('table_name',),
    #but I want ('table_name') that I'm using table[0] to fetch ('table_name')   
    table_list = [table[0] for table in cursor.fetchall()]
    print(table_list)
#select database version function
def verselect(cursor, mysqldb):
    #select database version
    cursor.execute("SELECT VERSION()")
    #fetch one result
    data = cursor.fetchone()
    #print database's version
    print("Database version : %s " % data)

#select table columns
def colselect(cursor, table_name):
    cursor.execute("show columns from" + " " + table_name)
    columns_list = [columns[0] for columns in cursor.fetchall()]
    return columns_list

#show table columns
def colprint(col_name):
    print("========================================")
    print("Yout table columns: ", end = '')
    for i in range(0,len(col_name)):
        if ((i + 1) == len(col_name)):
            print(col_name[i])
        else:
            print(col_name[i] + ',', end = '')
    print("========================================")

