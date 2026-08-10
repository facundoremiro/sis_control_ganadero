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

- [ ] Listar pesadas de una caravana puntual
- [ ] Listar todos los animales cargados (nuevo — sin decidir si es 
      tarjeta propia o se resuelve solo por caravana)
- [ ] Comparar dos pesadas (resta simple de peso)
- [ ] Probar todo con datos ficticios (3-4 animales, varias pesadas c/u)
- [ ] Actualizar README con el "cómo correrlo" real

## 🎨 CLI - checkpoints de lo visual

- [ ] Comparar pesadas: de resta simple a % de ganancia de peso
- [ ] Ranking de animales por % ganado
- [ ] Cerrar decisión de "lote" (texto libre vs. automático por peso — 
      inclinación actual: manual). Bloquea el filtro por lote.
- [ ] Filtros de consulta (por caravana, por lote)
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
