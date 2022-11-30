from model.Model import Model

import mysql.connector


class Game(Model):
    def __init__(self, userId):
        super().__init__()

        self.UserId = userId

    def createGame(self, points, total_time):
        self.commitCommand(
            f"INSERT INTO games VALUES (0, {self.UserId}, {points}, {total_time})")
        self.getLastId()

    def getLastId(self):
        self.connectMysql(True)
        self.cur.execute(
            f"SELECT id FROM games WHERE id_user = {self.UserId} ORDER BY id DESC LIMIT 1")
        self.gameid = self.cur.fetchone()['id']
        self.disconnectMysql()

    def insertQuestions(self, questionid):
        self.commitCommand(
            f"INSERT INTO questions_games VALUES (0, {self.gameid}, {questionid})")

    def getAllGames(self):
        try:
            self.connectMysql(True)
            query = f"SELECT * FROM games WHERE id_user = {self.UserId} ORDER BY id desc;"
            self.cur.execute(query)
            data = self.cur.fetchall()

            return data
        except mysql.connector.Error as err:
            print(err)
