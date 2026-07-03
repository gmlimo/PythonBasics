import pymysql

db = pymysql.connect(host = 'localhost',user = 'testuser',password = 'test123',db = 'sakila')

cursor = db.cursor()

sql = "SELECT * FROM TEST_TABLE"

try:
    cursor.execute(sql)
    
    data = cursor.fetchall()
    
    for row in data:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("%s %s, %d, %s, %d" % (fname, lname, age, sex, income))
        
    print("Data retrieved successfully!")
    
except:
    print('Something went wrong!!')


db.close()