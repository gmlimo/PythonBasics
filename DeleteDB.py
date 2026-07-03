import pymysql

db = pymysql.connect(host = 'localhost',user = 'testuser',password = 'test123',db = 'sakila')

cursor = db.cursor()

sql = "DELETE FROM TEST_TABLE"

try:
    cursor.execute(sql)
    
    db.commit() #It will make data permanent
        
    print("Data deleted successfully!")
    
except:
    print('Something went wrong!!')
    db.rollback()


db.close()