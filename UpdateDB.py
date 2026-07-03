import pymysql

db = pymysql.connect(host = 'localhost',user = 'testuser',password = 'test123',db = 'sakila')

cursor = db.cursor()

sql = "UPDATE TEST_TABLE SET INCOME = INCOME + 500 WHERE SEX = '%c'" %('F')

try:
    cursor.execute(sql)
    
    db.commit() #It will make data permanent
        
    print("Data updated successfully!")
    
except:
    print('Something went wrong!!')
    db.rollback()


db.close()