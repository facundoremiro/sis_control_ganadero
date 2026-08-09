from .import CONN, CURSOR
class Animal:
    def __init__(self, caravana, sexo, lote):
        self.caravana = caravana
        self.sexo = sexo
        self.lote = lote
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
                caravana TEXT PRIMARY KEY,
                sexo TEXT,
                lote TEXT)
            """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql = """
                INSERT INTO animals (caravana, sexo, lote)
                VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.caravana, self.sexo, self.lote))
        CONN.commit()
    @classmethod
    def hay_animales(cls):
        sql = "SELECT 1 FROM animals LIMIT 1"
        CURSOR.execute(sql)
        return CURSOR.fetchone() is not None
    @classmethod
    def find_by_caravana(cls, caravana):
        sql = "SELECT * FROM animals WHERE caravana = ?"
        CURSOR.execute(sql, (caravana,))
        return CURSOR.fetchone()
