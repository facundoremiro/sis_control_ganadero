
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
