import mysql.connector;
class DBTools:
    def __init__(self, host, user, pwd, port):
       self.host = host
       self.user = user
       self.pwd = pwd
       self.port = port
       print(self)

    def executeQuery(self,database,query):
        _host = self.host
        _user = self.user
        _pwd = self.pwd
        _port = self.port
        _database = database
        bd_connect = mysql.connector.connect(user=_user, password=_pwd, host=_host, port=_port, database=_database)
        try:
            #inicia a conexão
            cursor = bd_connect.cursor()
            #prepara a query
            cursor.execute(query);
            #se a transação não for um select
            if(query[0:6]!="SELECT"):
                bd_connect.commit()
            #se a transação retornar que afetou uma linha [sucesso]
            
                if(cursor.rowcount > 0):
                    return 0;
            #/////////////////////////////////////
            #Se a transação for um select, busca os dados (preenche as tuplas)
            data = cursor.fetchall()
            if(len(data)>0):
                return data;
                bd_connect.close();
                return bd_connect
        #se a query der erro
        except mysql.connector.Error as err:
            print("Não foi possível efetuar a query:" + err.msg + " - \nCódigo de Erro:"+str(err.errno))
            bd_connect.close()