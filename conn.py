import mysql.connector
#connection function
def mysqlconn():
    db = "animate"
    mysqldb = mysql.connector.connect(
            host = '127.0.0.1', #connect host
            user = "root", #connect username
            password = "nana60102", #connect password
            database = db #This database is not database of Mysql，but is schema.
            )
    try:
        #execute connect, and open database 
        cursor = mysqldb.cursor()
        print("connect successful")
    except:
        print("connect failed")
    
    return mysqldb, cursor, db

