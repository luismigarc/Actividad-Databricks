# Actividad de Ingeniería de Datos con Databricks

Repositorio académico con los cuatro puntos de una actividad desarrollada en Databricks sobre ventas ficticias de una tienda de videojuegos. El proyecto cubre almacenamiento, consulta, limpieza, automatización y procesamiento mediante un pipeline declarativo.

## Objetivo general

Construir un flujo de datos reproducible en Databricks, conservando los datos originales, aplicando reglas de calidad y comprobando la ejecución automatizada de las transformaciones.

## Tecnologías utilizadas

Databricks, Apache Spark, PySpark, Delta Lake, Unity Catalog, Databricks Jobs, Serverless compute y Lakeflow Spark Declarative Pipelines.

## Estructura de carpetas

```text
.
├── README.md
├── Punto_1/
│   ├── notebooks/
│   └── evidencias/
├── Punto_2/
│   ├── notebooks/
│   └── evidencias/
├── Punto_3/
│   ├── evidencias/
│   └── EJERCICIO_3.md
└── Punto_4/
    ├── notebooks/
    └── evidencias/
```

## Desarrollo de los puntos

### Punto 1 — Almacenamiento y consulta

Los notebooks [`01_cargar_ventas.ipynb`](Punto_1/notebooks/01_cargar_ventas.ipynb) y [`01_a_consultar_ventas.ipynb`](Punto_1/notebooks/01_a_consultar_ventas.ipynb) crean y consultan la tabla Delta `workspace.ingenieria_datos_luismiguel.ventas_bronze`. Se cargaron 15 registros iniciales y se comprobó la consulta desde otro notebook. La evidencia está en [`tabla_ventas_bronze.png`](Punto_1/evidencias/tabla_ventas_bronze.png).

### Punto 2 — Transformación y calidad

El notebook [`02_transformar_ventas.ipynb`](Punto_2/notebooks/02_transformar_ventas.ipynb) elimina duplicados y registros inválidos, calcula el total de cada venta y genera el resumen por categoría. Los resultados fueron 15 registros Bronze, 12 registros Silver válidos y 4 categorías. La validación está en [`validacion_limpieza.png`](Punto_2/evidencias/validacion_limpieza.png).

### Punto 3 — Automatización mediante Jobs

La explicación completa se conserva en [`EJERCICIO_3.md`](Punto_3/EJERCICIO_3.md). El Job `job_ventas_luismi` contiene las tareas `cargar_ventas` y `transformar_ventas`; la segunda depende de la primera. Se documentaron tres ejecuciones: exitosa en 59 segundos, fallo controlado en 39 segundos y ejecución corregida en 37 segundos. El error fue `UNRESOLVED_COLUMN.WITH_SUGGESTION`, causado por consultar una columna inexistente. Las capturas se encuentran en [`Punto_3/evidencias/`](Punto_3/evidencias/).

### Punto 4 — Pipeline declarativo

[`04_validacion_pipeline.ipynb`](Punto_4/notebooks/04_validacion_pipeline.ipynb) y [`pipeline_luismi.py`](Punto_4/notebooks/pipeline_luismi.py) implementan un pipeline con Lakeflow Spark Declarative Pipelines. Se generan las vistas materializadas `pipeline_ventas_limpias` y `pipeline_ventas_por_categoria`.

| Indicador | Inicial | Después de la nueva venta |
|---|---:|---:|
| Ventas válidas | 12 | 13 |
| Categorías | 4 | 4 |
| Total vendido | $14.126.900 COP | $14.686.700 COP |
| Incremento | — | $559.800 COP |

La actualización de las ventas limpias fue incremental. Las evidencias están en [`Punto_4/evidencias/`](Punto_4/evidencias/), incluyendo los grafos inicial y final y la comparación de totales.

## Ejecución

Los notebooks deben abrirse y ejecutarse en Databricks en este orden:

1. `Punto_1/notebooks/01_cargar_ventas.ipynb`
2. `Punto_1/notebooks/01_a_consultar_ventas.ipynb`
3. `Punto_2/notebooks/02_transformar_ventas.ipynb`

El Punto 3 se ejecuta desde el Job `job_ventas_luismi`, configurando primero `cargar_ventas` y luego `transformar_ventas` como tarea dependiente. El pipeline del Punto 4 se ejecuta desde Lakeflow Spark Declarative Pipelines usando `Punto_4/notebooks/pipeline_luismi.py`; el notebook de validación documenta la inserción de la nueva venta y la comparación de resultados.

No se deben ejecutar los archivos `.ipynb` o el pipeline desde un entorno local, porque dependen de Spark, Unity Catalog y objetos configurados en Databricks.

## Conclusión

La actividad demuestra un flujo completo de ingeniería de datos: los datos se almacenan en Bronze, se limpian en Silver, se automatizan mediante Jobs y finalmente se procesan con un pipeline declarativo que actualiza sus resultados ante cambios en el origen.
