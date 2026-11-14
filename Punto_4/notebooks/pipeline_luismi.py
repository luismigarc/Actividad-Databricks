
from pyspark import pipelines as dp
from pyspark.sql.functions import col, sum as spark_sum

# Vista materializada con ventas limpias
@dp.materialized_view(
    name="pipeline_ventas_limpias",
    comment="Ventas limpias de la tienda de videojuegos"
)
def pipeline_ventas_limpias():

    df = spark.read.table(
        "workspace.ingenieria_datos_luismiguel.ventas_bronze"
    )

    return (
        df.dropDuplicates()
        .filter(
            col("producto").isNotNull() &
            (col("cantidad") > 0) &
            (col("precio_unitario") > 0)
        )
        .withColumn(
            "total_venta",
            col("cantidad") * col("precio_unitario")
        )
    )


# Vista materializada con ventas por categoria
@dp.materialized_view(
    name="pipeline_ventas_por_categoria",
    comment="Resumen de ventas por categoria"
)
def pipeline_ventas_por_categoria():

    df = spark.read.table("pipeline_ventas_limpias")

    return (
        df.groupBy("categoria")
        .agg(
            spark_sum("total_venta").alias("total_vendido")
        )
    )
