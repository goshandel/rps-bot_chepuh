import sqlite3
class Database:
    def __init__(self):
        self.connect = sqlite3.connect('102.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS event 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_name TEXT,
                        nickname TEXT,
                        human_score INTEGER,
                        bot_score INTEGER)""")
        self.connect.commit()

    def check_user_exists(self, id, user_name, nickname):
        self.cursor.execute( """SELECT id, user_name, nickname FROM event
                             WHERE id = ?
                             OR user_name = ?
                             OR nickname = ?""",
                             (id, user_name, nickname))
        data = self.cursor.fetchone()
        return data is not None
    def add_user(self, id, user_name, nickname):
        self.cursor.execute("INSERT INTO event VALUES(?,?,?,?,?);",
                            (id, user_name, nickname, '', ''))
        self.connect.commit()
    def close(self):
        self.connect.close()


class Delete:
    def __init__(self):
        self.connect = sqlite3.connect('102.db')
        self.cursor = self.connect.cursor()
    def delete_user(self, id_to_delete):
        self.cursor.execute("SELECT id, FROM event WHERE id = ?", (id_to_delete))
    def close(self):
        self.connect.close()

class Score:
    def __init__(self):
        self.connect = sqlite3.connect('102.db')
        self.cursor = self.connect.cursor()

    def find_score(self, id, human_score, bot_score):
        self.cursor.execute(
            "SELECT id, human_score, bot_score FROM event WHERE id = ? AND COALESCE(human_score, -1) = ? AND COALESCE(bot_score, -1) = ?",
            (id, human_score, bot_score))
        result = self.cursor.fetchone()
        if result:
            id, stored_human_score, stored_bot_score = result
            if stored_human_score != human_score or stored_bot_score != bot_score:
                self.add_score(human_score, bot_score, id)
        else:
            self.add_score(human_score, bot_score, id)
    def add_score(self, human_score, bot_score, id):
        self.cursor.execute("UPDATE event SET human_score = ?, bot_score = ? WHERE id = ?",
                            (human_score, bot_score, id))
        self.connect.commit()
    def close(self):
        self.connect.close()

class Your_Leadbord:
    def __init__(self):
        self.connect = sqlite3.connect('102.db')
        self.cursor = self.connect.cursor()
    def event_human(self, user_id):
        self.cursor.execute("SELECT human_score FROM event WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    def event_bot(self, user_id):
        self.cursor.execute("SELECT bot_score FROM event WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    def close(self):
        self.connect.close()

class Leadbord:
    def __init__(self):
        self.connect = sqlite3.connect('102.db')
        self.cursor = self.connect.cursor()
    def top_three_users(self):
        self.cursor.execute("SELECT user_name, human_score, bot_score FROM event ORDER BY human_score DESC LIMIT 3")
        results = self.cursor.fetchall()
        return results
    def close(self):
        self.connect.close()