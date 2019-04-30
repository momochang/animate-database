#update sql query
def upd_num(table_name, col_name):
    sql = """Update """ + table_name + " set "
    ins = input("Enter your update data(set):")
    upd_whe = input("Enter your requirement(where): ")
    #sql = sql + " " + "where" + " " + sel_whe
    sql = sql + ins + " " +  "where" + " " + upd_whe
    
    return sql
       
#update your database data
def update(cursor, mysqldb, table_name, col_na):
    print("語法: Update table_name set xxx where xxx")
    sql = upd_num(table_name, col_na)
    try:
        print(sql)
        cursor.execute(sql)
        mysqldb.commit()
        print("Update successul")
    except:
        print("Update error")
        mysqldb.rollback()


