import conn
import show
import sel
import insert as ins
import update as up
import delete as de

def sh_col(cursor, mysqldb):
    col_name = show.colselect(cursor, table_name)
    show.colprint(col_name)
    return col_name

def switchDefault():
    print("input error...")
    
def switch(cursor, mysqldb, option, table_name):
   
    switchDic = {
            "1": sel.mysqlsel(cursor, mysqldb, table_name),
            "2": ins.insert(cursor, mysqldb, table_name),
            "3": up.update(cursor, mysqldb, table_name),
            "4": de.delete(cursor, mysqldb, table_name)
            }
    return switchDic.get(option, switchDefault())

#main
mysqldb, cursor, database = conn.mysqlconn()
print("table name: ", end = '')
show.list_table(cursor, mysqldb)
table_name = input("Enter you want table: ")
col_name = sh_col(cursor, mysqldb)
#ins.insert(cursor, mysqldb, table_name, col_name)
sel.mysqlsel(cursor, mysqldb, table_name)
#up.update(cursor, mysqldb, table_name, col_name)
#de.delete(cursor, mysqldb, table_name, col_name)

    