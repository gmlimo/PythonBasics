import pymysql

db = pymysql.connect(host = 'localhost',user = 'testuser',password = 'test123',db = 'sakila')

cursor = db.cursor()

sql1 = """INSERT INTO TEST_DATA (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Wyatt', 'Limon', 9, 'M', 500)"""

sql2 = """INSERT INTO TEST_DATA (FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES('Billy', 'Lee', 44, 'M', 2200)"""

try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()
    print('Data inserted correctly!')
except:
    db.rollback()
    print('Something went wrong!! Check syntax...')


db.close()