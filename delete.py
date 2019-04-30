#delete sql query
def del_num(table_name, col_name):
    sql = """Delete from """ + table_name
    del_whe = input("Enter your requirement(where): ")
    #sql = sql + " " + "where" + " " + sel_whe
    sql = sql + " " + "where" + " " + del_whe
    
    return sql

#delete your database data
def delete(cursor, mysqldb, table_name, col_na):
    print("語法: Delete table_name where xxx")
    sql = del_num(table_name, col_na)
    try:
        print(sql)
        cursor.execute(sql)
        mysqldb.commit()
        print("Delete successul")
    except:
        print("Delete error")
        mysqldb.rollback()
        


