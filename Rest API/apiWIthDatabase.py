from flask import Flask
import DBToolsMySQL as MYSQL

app = Flask(__name__)

@app.route("/query")
def hello():
    db = MYSQL.DBTools("localhost","root","root","3307")
    
    return str(db.executeQuery("controleasydb","SELECT * FROM apartamento"))

if __name__ == "__main__":
    app.run()