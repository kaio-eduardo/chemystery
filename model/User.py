from model.Model import Model

import mysql.connector


class User(Model):
    def __init__(self, id=0):
        super().__init__()

        self.id = id

    def getUser(self, username, password):
        self.connectMysql(True)
        query_user = f"select *, count(*) as userExists from users where username = '{username}' and senha = '{password}' limit 1;"
        self.cur.execute(query_user)
        data = self.cur.fetchone()
        self.disconnectMysql()
        return data

    def createUser(self, user):
        self.connectMysql()
        try:
            addUser = (
                "INSERT INTO users VALUES (0, %(username)s, %(password)s, %(email)s)")
            self.cur.execute(addUser, user)
            self.con.commit()
            self.disconnectMysql()
            return True
        except mysql.connector.Error as err:
            print(err)
            return False

    def getGlobalRank(self):
        try:
            self.connectMysql(True)
            query_rank = f"SELECT ROW_NUMBER() OVER( ORDER BY max(g.points) DESC) as user_rank, max(g.points) as grade, u.username FROM games AS g JOIN users AS u ON u.id = g.id_user GROUP BY u.username ORDER BY user_rank LIMIT 5;"
            self.cur.execute(query_rank)
            data = self.cur.fetchall()
            return data
        except mysql.connector.Error as err:
            print(err)
            return err

    def getPersonalRank(self):
        try:
            self.connectMysql(True)
            query_rank = f"SELECT t.user_rank FROM (SELECT id_user, ROW_NUMBER() OVER (ORDER BY max(g.points) DESC) as user_rank from games g GROUP BY id_user) as t WHERE id_user = {self.id};"
            self.cur.execute(query_rank)
            data = self.cur.fetchone()
            return data
        except mysql.connector.Error as err:
            print(err)
            return err

    def countGames(self):
        try:
            self.connectMysql(True)
            query = f"select count(id_user) as games from games where id_user = {self.id};"
            self.cur.execute(query)
            data = self.cur.fetchone()
            self.disconnectMysql()
            return data
        except mysql.connector.Error as err:
            print(err)

    def getBestGame(self):
        try:
            data = self.executeCommand(
                f"select max(points) from games where id_user = {self.id};")
            return data[0][0]
        except mysql.connector.Error as err:
            print(err)
