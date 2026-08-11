# ROADMAP - sis_control_ganadero

_Este archivo es el plan del proyecto: qué está hecho, qué sigue, y qué 
decisiones ya se tomaron aunque todavía no estén construidas. Se va 
actualizando a medida que se avanza._

## ✅ HECHO (MVP)

- [x] Estructura del proyecto (setup_db.py, cli.py, models/)
- [x] Tablas: animales (caravana PK, sexo, lote) y pesadas (id PK, 
      caravana FK, fecha, peso, estado_corporal)
- [x] animal.py: save(), create_table(), find_by_caravana(), hay_animales()
- [x] pesada.py: save() (con lastrowid), create_table(), fecha default a hoy
- [x] cli.py: cargar_animales_nuevos() y cargar_pesadas(), con validaciones 
      (caravana duplicada, animal inexistente, tabla vacía)
- [x] Menú principal (bienvenida + opciones + redirección automática a 
      cargar animal nuevo si no hay ninguno cargado)

## 🔄 CLI - pendiente antes de lo visual

- [x] Listar pesadas de una caravana puntual
- [x] Listar todos los animales cargados (se puede filtar por caravana, lote,   sexo, y ver todos)
- [x] Listar todos los pesajes
- [ ] Filtrar los pesajes listados (por fecha, caravana, lote, sexo)
- [ ] Comparar dos pesadas (resta simple de peso)
- [ ] Probar todo con datos ficticios (3-4 animales, varias pesadas c/u)

## 🎨 CLI - checkpoints de lo visual

- [ ] Comparar pesadas: de resta simple a % de ganancia de peso
- [ ] Ranking de animales por % ganado
- [ ] Cerrar decisión de "lote" (texto libre vs. automático por peso — 
      inclinación actual: manual). Bloquea el filtro por lote.
- [x] Filtros de consulta (por caravana, por lote)
- [ ] Mostrar resultados en tabla prolija de consola
- [ ] Gráfico real (opcional — probablemente se resuelve directo en la web)

## 🌐 WEB (v2)

### Secciones
- Inicio (bienvenida + resumen rápido)
- Consultas con filtros (caravana, lote, fecha)
- Apartado general (gráficos por lote, rendimiento en variables)
- Carga de animales

### Carga automática — decisión cerrada
Conversor automático desde archivo exportado de balanza (no tabla 
manual). Motivo: evitar manipulación de datos por parte de encargados 
(robo de kilos), garantizar legitimidad del dato para el productor 
jefe. Se resuelve con config por marca (mapeo de columnas: caravana, 
peso, etc.) + parser genérico — no un parser distinto por cada balanza.

### Seguridad y roles — decisión cerrada
- Login: por defecto, solo el productor entra con acceso completo 
  (ver + editar + cargar).
- Encargado: acceso a todo lo de consulta (ver, filtrar, usar todas 
  las funciones de lectura) — la sección de Carga y Edición queda 
  reservada solo al productor.
- Auditoría de carga: quién cargó cada pesaje y cuándo.
- Alerta de pesaje faltante: default 2 meses, configurable.

### Extras
- Exportar reportes en PDF/Excel.

## 🔭 Más adelante (anotado, sin tocar)

- Reporting: % de engorde óptimo por lote/sexo vs. objetivo del productor
- Mapa del campo con carga de animales por lote (Folium u similar)
## 🐄 Módulo Reproductivo (celo + preñez)

Reemplaza y amplía la nota anterior de "Detección de celo" — se agrupa 
todo el ciclo reproductivo del animal en un solo apartado, no como 
funciones sueltas.

### Carga
- Celo detectado (caravana, fecha)
- Servicio — monta natural o inseminación artificial (caravana, fecha, tipo)
- Diagnóstico de preñez (caravana, fecha, resultado: preñada / vacía)
- Fecha probable de parto (calculada a partir del servicio confirmado)

### Visualización
- Historial reproductivo completo por animal (celo → servicio → 
  diagnóstico → parto)
- Listado de animales próximos a parir
- Listado de animales pendientes de diagnóstico (a tactar)

### Métricas del rodeo
- Tasa de preñez (% de servidas que quedaron preñadas)
- Intervalo entre partos por animal

## 🌾 Modelo de datos: lotes con hectáreas (calculo de la carga del campo)

Se agrega tabla `lotes`, reemplazando el texto libre actual de 
`animales.lote`:

- lotes: nombre TEXT PRIMARY KEY, hectareas REAL

`animales.lote` pasa de ser texto suelto a FK contra `lotes.nombre` — 
mismo patrón que caravana → animales en la tabla pesadas.

Con esto, "cantidad de animales por hectárea" en un lote se calcula 
cruzando animales y lotes (JOIN: contar animales de ese lote, dividido 
las hectáreas del lote).
