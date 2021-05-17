import DBToolsMySQL as MYSQL

db = MYSQL.DBTools("localhost","root","root","3307")
db1 = db.executeQuery("controleasydb","SELECT * FROM apartamento")
print(db1)