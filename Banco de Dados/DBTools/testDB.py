from DBToolsMySQL import DBTools

db = DBTools("localhost","root","root","3307")
db1 = db.executeQuery("controleasydb","INSERT INTO apartamento(idApartamento,numeroApartamento,blocoApartamento) values('a51','51','1')")
db2 = db.executeQuery("controleasydb","SELECT * FROM apartamento")
db3 = db.executeQuery("controleasydb", "DELETE FROM apartamento WHERE idApartamento='a51'")
print(db2)