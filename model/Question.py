from model.Model import Model


class Question(Model):
    def __init__(self):
        super().__init__()

    def create(self):
        pass

    def getQuestions(self):
        self.connectMysql(True)
        self.cur.execute(
            "SELECT * FROM questions ORDER BY RAND ( ) LIMIT 10;")
        data = self.cur.fetchall()
        self.disconnectMysql()
        return data

    def getAlternatives(self, questionId):
        query_alternatives = f"(select * from alternatives where is_right = true and id_question = {questionId}) union (select * from alternatives where is_right = false and id_question = {questionId} order by rand() limit 3) order by rand();"
        data = self.executeCommand(query_alternatives)
        return data
