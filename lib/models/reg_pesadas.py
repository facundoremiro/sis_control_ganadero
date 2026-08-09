from .import CONN, CURSOR
import datetime
class Regpesadas:
    def __init__(self, caravana, peso, estado_corporal, fecha=None, id=None):
        self.id = id
        self.caravana = caravana
        self.fecha = fecha if fecha else datetime.date.today().isoformat()
        self.peso = peso
        self.estado_corporal = estado_corporal
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reg_pesadas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caravana TEXT,
                fecha TEXT,
                peso REAL,
                estado_corporal TEXT,
                FOREIGN KEY (caravana) REFERENCES animals(caravana))
            """
        CURSOR.execute(sql)
        CONN.commit()
    def save(self):
        sql = """
                INSERT INTO reg_pesadas (caravana, fecha, peso, estado_corporal)
                VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.caravana, self.fecha, self.peso, self.estado_corporal))
        CONN.commit()
        self.id = CURSOR.lastrowid

