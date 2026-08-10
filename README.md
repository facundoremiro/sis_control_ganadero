Estoy armando "sis_control_ganadero", un CLI en Python + SQLite para 
registrar pesadas de rodeo. Aprendo por ingeniería inversa, adaptando 
el proyectos ya echos.

ESTRUCTURA:
sis_control_ganadero/
├── lib/
│   ├── setup_db.py       (crea tablas, se corre una sola vez)
│   ├── cli.py            (menú de uso diario, en construcción)
│   ├── animales.db
│   ├── models/
│   │   ├── __init__.py   (CURSOR, CONN compartidos, DB_PATH vía __file__)
│   │   ├── animal.py
│   │   └── Reg_pesada.py

TABLAS:
- animales: caravana TEXT PRIMARY KEY, sexo TEXT, lote TEXT
- pesadas: id INTEGER PRIMARY KEY, caravana TEXT (FK a animales), 
  fecha TEXT (formato ISO YYYY-MM-DD), peso REAL, estado_corporal INTEGER

DATO IMPORTANTE: la FK no está enforced (nunca corrí 
PRAGMA foreign_keys = ON), así que la integridad se controla 
a mano desde el código, no desde SQLite.

animal.py tiene: __init__, save(), create_table(), 
find_by_caravana() (devuelve fila o None), hay_animales() (bool).

pesada.py tiene: __init__ (fecha default a hoy si no se pasa), 
save() (con self.id = CURSOR.lastrowid), create_table().

cli.py tiene armadas: cargar_animales_nuevos() (chequea duplicado 
con find_by_caravana antes de guardar) y cargar_pesadas() (chequea 
hay_animales() al inicio, y find_by_caravana() por cada caravana 
antes de guardar la pesada). Estoy armando el menú principal 
(mensaje de bienvenida, "+" para animal nuevo, "=" para pesada).

# Sistema de Control Ganadero

CLI en Python para registrar el peso de animales de un rodeo a lo 
largo del tiempo y comparar su evolución.

## Qué hace
- Registra animales (caravana, sexo, lote)
- Registra pesadas (fecha, peso, estado corporal) por animal
- Evita caravanas duplicadas y pesadas de animales no registrados

## Para quién
Para quien ya pesa el rodeo con balanza y bastón, y necesita un 
lugar simple para cargar y comparar esos datos después — no 
reemplaza la captura en el campo, es para después del pesaje.

## Tecnología
Python 3 + SQLite3 (sin dependencias externas)

## Cómo correrlo
\`\`\`bash
git clone https://github.com/facundoremiro/sis_control_ganadero.git
cd sis_control_ganadero
python3 lib/create_db.py   # crea las tablas (una sola vez)
python3 lib/setup.py        # menú para cargar datos
\`\`\`

## Estado
En desarrollo — MVP en construcción.
