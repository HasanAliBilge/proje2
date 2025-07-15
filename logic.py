import sqlite3

class DB_Manager:
    def __init__(self, database):
        self.database = #
        
    def get_random_country(self):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute("#")
            return cur.fetchone()  # None veya tuple döndürür

class Quiz:
    CONTINENT_POINTS = {#}
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def get_question(self):
        return self.#()
    
    def check_answer(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.lower()
    
    def get_points(self, #):
        return self.CONTINENT_POINTS.get(continent_id, 1)