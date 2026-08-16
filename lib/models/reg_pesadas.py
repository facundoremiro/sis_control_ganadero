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
    @classmethod
    def mostrar_pesajes(cls, fecha= None, caravana= None, lote = None):
        sql = "SELECT * FROM reg_pesadas ORDER by fecha"
        CURSOR.execute(sql)
        if fecha:
            sql = "SELECT * FROM reg_pesadas WHERE fecha = ? ORDER BY fecha"
            CURSOR.execute(sql, (fecha,))
            print(f"Pesajes del día {fecha}:")
            for row in CURSOR.fetchall():
                print(f"Caravana: {row[1]}, Peso: {row[3]}, Estado corporal: {row[4]}")
        elif caravana:
            sql = "SELECT * FROM reg_pesadas WHERE caravana = ? ORDER BY fecha"
            CURSOR.execute(sql, (caravana,))
            print(f"Pesajes del animal con caravana {caravana}:")
            for row in CURSOR.fetchall():
                print(f"Fecha: {row[2]}, Peso: {row[3]}, Estado corporal: {row[4]}")
        elif lote:
            sql = """
                SELECT rp.fecha, rp.caravana, rp.peso, rp.estado_corporal
                FROM reg_pesadas rp
                JOIN animals a ON rp.caravana = a.caravana
                WHERE a.lote = ? ORDER BY fecha
            """
            CURSOR.execute(sql, (lote,))
            print(f"Pesajes de los animales en el lote {lote}:")
            for row in CURSOR.fetchall():
                print(f"Fecha: {row[0]}, Caravana: {row[1]}, Peso: {row[2]}, Estado corporal: {row[3]}")
        else:
            print("Datos de animales y sus pesadas:")
            for row in CURSOR.fetchall():
                print(f"Fecha: {row[2]}, Caravana: {row[1]}, Peso: {row[3]}, Estado corporal: {row[4]}")
    @classmethod
    def comparar_pesajes(cls, caravana):
        CURSOR.execute("SELECT * FROM reg_pesadas WHERE caravana = ? ORDER by fecha", (caravana,))
        pesajes = CURSOR.fetchall()
        if len(pesajes) < 2:
            print("No hay suficientes pesajes cargados para esa caravana.")
            return
        primero = pesajes[0]
        segundo = pesajes[-1]
        peso_viejo = primero[3]
        peso_nuevo = segundo[3]
        diferencia = (peso_nuevo - peso_viejo)/peso_viejo * 100
        print(f"Caravana {caravana}: {peso_viejo}kg -> {peso_nuevo}kg ({diferencia:.2f}% de ganancia)")

