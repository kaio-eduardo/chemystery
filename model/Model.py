import mysql.connector


class Model():
    def __init__(self, host="localhost", user="root", password="admin", db="chemystery"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connectMysql(self, dicti=False):
        self.con = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password, database=self.db)
        self.cur = self.con.cursor(dictionary=dicti)

    def disconnectMysql(self):
        self.con.close()

    def executeCommand(self, sql):
        self.connectMysql()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.disconnectMysql()
        return res

    def commitCommand(self, sql):
        self.connectMysql()
        self.cur.execute(sql)
        self.con.commit()
        self.disconnectMysql()
