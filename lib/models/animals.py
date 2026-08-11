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
    @classmethod
    def mostrar_animales(cls, caravana=None, lote=None, sexo=None):
        sql = "SELECT * FROM animals"
        CURSOR.execute(sql)
        if caravana:
            sql = "SELECT * FROM animals WHERE caravana = ?"
            CURSOR.execute(sql, (caravana,))
            animal = CURSOR.fetchone()
            if animal:
                print(f"Animal encontrado: Caravana: {animal[0]}, Sexo: {animal[1]}, Lote: {animal[2]}")
            else:
                print(f"No se encontró un animal con la caravana {caravana}.")
        elif lote:
            sql = "SELECT * FROM animals WHERE lote = ?"
            CURSOR.execute(sql, (lote,))
            animal = CURSOR.fetchall()
            if animal:
                print(f"Animales en el lote {lote}:")
                for animal in animal:
                    print(f"Caravana: {animal[0]}, Sexo: {animal[1]}, Lote: {animal[2]}")
            else:
                print(f"No se encontraron animales en el lote {lote}.")
        elif sexo:
            sql = "SELECT * FROM animals WHERE sexo = ?"
            CURSOR.execute(sql, (sexo,))
            animal = CURSOR.fetchall()
            if animal:
                print(f"Animales con sexo {sexo}:")
                for animal in animal:
                    print(f"Caravana: {animal[0]}, Sexo: {animal[1]}, Lote: {animal[2]}")
            else:
                print(f"No se encontraron animales con sexo {sexo}.")
        else:
            print("Todos los animales registrados:")
            CURSOR.execute("SELECT * FROM animals")
            for row in CURSOR.fetchall():
                print(f"Caravana: {row[0]}, Sexo: {row[1]}, Lote: {row[2]}")
