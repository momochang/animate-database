def ins_cond(table_name, sql, valist):
    if (table_name == "ships"):
        sql = sql % (valist[0], valist[1], valist[2])
    if (table_name == "outcomes"):
        sql = sql % (valist[0], valist[1], valist[2])
    if (table_name == "company"):
        sql = sql % (valist[0], valist[1])
    if (table_name == "animate"):
        sql = sql % (valist[0], valist[1],valist[2],valist[3], valist[4], valist[5],valist[6], valist[7], valist[8])
    return sql
#insert sql query
def ins_num(table_name, col_name):
    valist = []
    sql = """Insert into """ + table_name + " ("
    for i in range(0, len(col_name)):
        sql = sql + col_name[i]
        if ((i+1) == len(col_name)):
            sql = sql + ") values ("
        else:
            sql = sql + ", "
    #sql = sql + "'%s', '%s', '%s') " % ('cc', 'dd', 1902)      
    for i in range(0, len(col_name)):
        sql = sql + "'%s'"
        if ((i+1) == len(col_name)):
            sql = sql + ") "
        else:
            sql = sql + ", "
    
    for i in range(0, len(col_name)):
        ins = input("Enter your " + str(i+1) + " column data: ")
        valist.append(ins)
    sql = ins_cond(table_name, sql, valist)
    
    return sql

#insert data to table of database
def insert(cursor, mysqldb, table_name, col_na):
    print("語法: Insert into table_name values ('%s'..) % (xxx..)")
    sql = ins_num(table_name, col_na)  
    try:
        print(sql)
        cursor.execute(sql)
        mysqldb.commit()
        print("Insert successul")
    except:
        print("Insert error")
        mysqldb.rollback()


