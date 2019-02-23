import pymysql
db = pymysql.connect(host="localhost",
                             user = "root",
                             passwd = "Sem123",
                             database = "kp")

print(db)
myc = db.cursor()


sql = "insert into stu values(23,'Ssem')"
myc.execute(sql)

db.commit()
print(myc.rowcount,"record inserted")
