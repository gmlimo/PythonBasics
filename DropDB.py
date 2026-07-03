import pymysql

db = pymysql.connect(host = 'localhost',user = 'testuser',password = 'test123',db = 'sakila')

cursor = db.cursor()

sql = "DROP TABLE TEST_TABLE"

try:
    cursor.execute(sql)
    
    #commit is not needed this time!!
        
    print("Table dropped successfully!")
    
except:
    print('Something went wrong!!')


db.close()