from flask import Flask
from flask import request
import DBToolsMySQL as MYSQL

app = Flask(__name__)

@app.route("/query", methods = ['POST'])
def GETQuery():
    if(request.method == 'POST'):
        db = MYSQL.DBTools("localhost","root","root","3307")
        query =request.form["query"]
        db1 = db.executeQuery("controleasydb",query)
        
        return str(db1)
if __name__ == "__main__":
    app.run()