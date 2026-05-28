import os
import matplotlib.pyplot as plt

from dominio.articulos import Articulo
from dominio.categoria import Categoria
from grafo.grafoarticulocategoria import GrafoArticuloCategoria
from lector.lector_datos import LectorArch


def main():
    
    #Print de bienvenida
    print("Bienvenido al programa de análisis de artículos y categorías de Wikipedia.\n")
    
    # Crear carpeta resultados automáticamente si no existe
    carpeta_resultados = "../resultados"
    os.makedirs(carpeta_resultados, exist_ok=True)
    grafo = GrafoArticuloCategoria()
    enlaces = LectorArch.leer_mtx_filtrado("../datos/wiki-topcats.mtx",limite=10000)
    relaciones = LectorArch.leer_mtx_categorias( "../datos/wiki-topcats_Categories.mtx",limite=10000)

    nombres_articulos = LectorArch.leer_nombres_articulos("../datos/wiki-topcats_pagenames.txt")

    nombres_categorias = LectorArch.leer_nombres_categorias("../datos/wiki-topcats_Category_names.txt")

    articulo_por_id = {
        i + 1: nombre
        for i, nombre in enumerate(nombres_articulos)
    }

    categoria_por_id = {
        i + 1: nombre
        for i, nombre in enumerate(nombres_categorias)
    }

    # Construcción del grafo
    for origen, destino in enlaces:
        if origen not in grafo.articulos:
            grafo.agregar_articulo(
                Articulo(
                    origen,
                    articulo_por_id.get(origen, f"Articulo {origen}")
                )
            )

        if destino not in grafo.articulos:
            grafo.agregar_articulo(
                Articulo(
                    destino,
                    articulo_por_id.get(destino, f"Articulo {destino}")))

        grafo.agregar_enlace(origen, destino)


    # Asociación artículo-categoría
    for id_articulo, id_categoria in relaciones:
        if id_articulo not in grafo.articulos:
            grafo.agregar_articulo(Articulo(id_articulo,articulo_por_id.get(id_articulo, f"Articulo {id_articulo}")))

        if id_categoria not in grafo.categorias:
            grafo.agregar_categoria(Categoria(id_categoria,categoria_por_id.get(id_categoria, f"Categoria {id_categoria}")))

        grafo.asociar_articulo_categoria(id_articulo, id_categoria)


    # ======================================
    # VALIDACION DE CARGA
    # ======================================

    cantidad_articulos = len(grafo.articulos)
    cantidad_categorias = len(grafo.categorias)
    cantidad_enlaces = len(enlaces)
    cantidad_relaciones = len(relaciones)

    print("\nVALIDACION DE CARGA\n")

    print(f"Cantidad de articulos cargados: {cantidad_articulos}")
    print(f"Cantidad de categorias cargadas: {cantidad_categorias}")
    print(f"Cantidad de enlaces procesados: {cantidad_enlaces}")
    print(f"Cantidad de relaciones articulo-categoria: {cantidad_relaciones}")

    # BFS
    inicio = max(
        grafo.articulos.keys(),
        key=lambda id_articulo: grafo.grado_salida(id_articulo)
    )
    nombre_inicio = grafo.articulos[inicio].nombre_articulo
    grado_salida_inicio = grafo.grado_salida(inicio)

    print("\nNodo seleccionado automaticamente para BFS/DFS:")
    print(f"Articulo: {nombre_inicio}")
    print(f"ID: {inicio}")
    print(f"Grado de salida: {grado_salida_inicio}")

    resultado_bfs = grafo.bfs(inicio)
    resultado_dfs = grafo.dfs(inicio)

    print(f"\nPrimeros 10 nodos visitados mediante BFS desde {nombre_inicio}:")

    print(f"{'Orden':<10}{'ID':<10}{'Articulo visitado'}")

    for i, id_articulo in enumerate(resultado_bfs[:10], start=1):
        nombre = grafo.articulos[id_articulo].nombre_articulo

        print(f"{i:<10}{id_articulo:<10}{nombre}")

    print(f"\nPrimeros 10 nodos visitados mediante DFS desde {nombre_inicio}:")

    print(f"{'Orden':<10}{'ID':<10}{'Articulo visitado'}")

    for i, id_articulo in enumerate(resultado_dfs[:10], start=1):
        nombre = grafo.articulos[id_articulo].nombre_articulo

        print(f"{i:<10}{id_articulo:<10}{nombre}")

    # ======================================
    # VERIFICACION DE EXISTENCIA DE CAMINO
    # ======================================

    articulo_origen = resultado_bfs[0]
    articulo_destino = resultado_bfs[1]

    nombre_origen = grafo.articulos[articulo_origen].nombre_articulo
    nombre_destino = grafo.articulos[articulo_destino].nombre_articulo

    camino = grafo.existe_camino(
        articulo_origen,
        articulo_destino
    )

    print("\nPrueba/Resultado:")

    print(
        f"Nodo origen -> {articulo_origen} - {nombre_origen}"
    )

    print(
        f"Nodo destino -> {articulo_destino} - {nombre_destino}"
    )

    if camino:
        print("¿Existe camino? -> Sí")
        print("Camino encontrado ->", camino)

    else:
        print("¿Existe camino? -> No")





    # Camino simple
    lista_articulos = list(grafo.articulos.keys())

    articulo_origen = lista_articulos[0]
    articulo_destino = lista_articulos[1]

    camino = grafo.existe_camino(articulo_origen,articulo_destino)

    print("\nCamino encontrado:", camino)

    # Mayor grado de entrada
    top_articulos = grafo.articulos_mayor_grado_entrada()

    print("\nArticulos con mayor grado de entrada:")

    for articulo, grado in top_articulos:
        nombre = grafo.articulos[articulo].nombre_articulo
        print(nombre, "-", grado)
        
    #Print de carga 
    print("\nProcesando PageRank...")

    # PageRank
    ranks = grafo.pagerank()

    top_pagerank = sorted(ranks.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\nTop PageRank:")

    for id_articulo, valor in top_pagerank:
        nombre = grafo.articulos[id_articulo].nombre_articulo
        print(nombre, "-", format(valor, ".10f"))

    # Guardar ranking PageRank en txt
    with open(f"{carpeta_resultados}/ranking_pagerank.txt","w",encoding="utf-8") as archivo:

        archivo.write("Top PageRank\n\n")

        for id_articulo, valor in top_pagerank:
            nombre = grafo.articulos[id_articulo].nombre_articulo
            archivo.write(f"{nombre} - {format(valor, '.10f')}\n")

    # ======================================
    # RELACION ARTICULO - CATEGORIA
    # ======================================

    print("\nRelación entre artículos destacados y categorías:\n")

    for id_articulo, valor in top_pagerank[:5]:

        articulo = grafo.articulos[id_articulo]

        print(
            f"Articulo: {articulo.nombre_articulo}"
        )

        print(
            f"PageRank: {format(valor, '.10f')}"
        )

        if articulo.categorias:

            print("Categorias asociadas:")

            for id_categoria in articulo.categorias:

                if id_categoria in grafo.categorias:
                    nombre_categoria = grafo.categorias[
                        id_categoria
                    ].nombre_categoria

                    print("-", nombre_categoria)

        else:
            print("Sin categorias asociadas")

        print()

    # =========================
    # GRAFICO TOP GRADO ENTRADA
    # =========================

    nombres_top = []
    grados_top = []

    for articulo, grado in top_articulos:

        nombres_top.append(
            grafo.articulos[articulo].nombre_articulo
        )

        grados_top.append(grado)

    plt.figure(figsize=(12, 5))

    plt.bar(
        nombres_top,
        grados_top,
        edgecolor="black",
        width=0.8,
    )

    plt.title("Top articulos con mayor grado de entrada")

    plt.xlabel("Articulos")

    plt.ylabel("Cantidad de enlaces entrantes")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        f"{carpeta_resultados}/top_grado_entrada.png"
    )

    plt.close()

    # ======================================
    # TOP GRADO DE SALIDA
    # ======================================

    grados_salida = []

    for id_articulo in grafo.articulos:
        grado = grafo.grado_salida(id_articulo)

        grados_salida.append(
            (id_articulo, grado)
        )

    grados_salida.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_salida = grados_salida[:10]

    print("\nTop articulos con mayor grado de salida:\n")

    for id_articulo, grado in top_salida:
        nombre = grafo.articulos[id_articulo].nombre_articulo

        print(f"{nombre} - {grado}")

    # =========================
    # GRAFICO TOP GRADO SALIDA
    # =========================

    nombres_salida = []
    valores_salida = []

    for id_articulo, grado in top_salida:
        nombres_salida.append(
            grafo.articulos[id_articulo].nombre_articulo
        )

        valores_salida.append(grado)

    plt.figure(figsize=(12, 5))

    plt.bar(
        nombres_salida,
        valores_salida,
        edgecolor="black",
        width=0.8,
    )

    plt.title("Top articulos con mayor grado de salida")

    plt.xlabel("Articulos")

    plt.ylabel("Cantidad de enlaces salientes")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        f"{carpeta_resultados}/top_grado_salida.png"
    )

    plt.close()


    # =========================
    # GRAFICO TOP PAGERANK
    # =========================

    nombres_pagerank = []
    valores_pagerank = []

    for id_articulo, valor in top_pagerank:

        nombres_pagerank.append(
            grafo.articulos[id_articulo].nombre_articulo
        )

        valores_pagerank.append(valor)

    plt.figure(figsize=(12, 5))

    plt.bar(
        nombres_pagerank,
        valores_pagerank,
        edgecolor="black",
        width=0.8
    )

    plt.title("Top articulos segun PageRank")

    plt.xlabel("Articulos")

    plt.ylabel("Valor PageRank")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        f"{carpeta_resultados}/top_pagerank.png"
    )

    plt.close()

    # =========================
    # HISTOGRAMA DISTRIBUCION
    # =========================

    grados_totales = []

    for id_articulo in grafo.articulos:

        grados_totales.append(
            grafo.grado_entrada(id_articulo)
        )

    plt.figure(figsize=(10, 5))

    plt.hist(grados_totales, bins=30)

    plt.title("Distribucion de grados")

    plt.xlabel("Cantidad enlaces entrantes")

    plt.ylabel("Cantidad articulos")

    plt.tight_layout()

    plt.savefig(
        f"{carpeta_resultados}/histograma_grados.png"
    )

    plt.close()

    # ======================================
    # DISTRIBUCION DE GRADOS
    # ======================================

    rangos = {
        "0": 0,
        "1-2": 0,
        "3-5": 0,
        "6-10": 0,
        "11-20": 0,
        "21-50": 0,
        "51+": 0
    }

    for grado in grados_totales:

        if grado <= 0:
            rangos["0"] += 1

        elif grado <= 2:
            rangos["1-2"] += 1

        elif grado <= 5:
            rangos["3-5"] += 1

        elif grado <= 10:
            rangos["6-10"] += 1

        elif grado <= 20:
            rangos["11-20"] += 1

        elif grado <= 50:
            rangos["21-50"] += 1

        else:
            rangos["51+"] += 1

    plt.figure(figsize=(8, 5))

    plt.bar(
        rangos.keys(),
        rangos.values(),
        edgecolor="black",
        width=0.8,
    )

    plt.title("Distribucion de grados")
    plt.xlabel("Rangos de enlaces entrantes")
    plt.ylabel("Cantidad de articulos")

    plt.tight_layout()

    plt.savefig(
        f"{carpeta_resultados}/distribucion_grados.png"
    )

    plt.close()

    # ======================================
    # COMPARACION PAGERANK VS GRADO ENTRADA
    # ======================================

    print("\nComparacion PageRank vs grado de entrada:\n")

    for id_articulo, valor in top_pagerank:
        nombre = grafo.articulos[id_articulo].nombre_articulo

        grado = grafo.grado_entrada(id_articulo)

        print(
            f"{nombre} | "
            f"PageRank: {format(valor, '.10f')} | "
            f"Grado entrada: {grado}"
        )

    # ======================================
    # PRUEBA CAMINO MAS EXTENSO
    # ======================================

    origen = resultado_bfs[0]
    destino = resultado_bfs[9]

    nombre_origen = grafo.articulos[origen].nombre_articulo
    nombre_destino = grafo.articulos[destino].nombre_articulo

    camino_extenso = grafo.existe_camino(
        origen,
        destino
    )

    print("\nPrueba de camino mas extensa:\n")

    print(f"Origen -> {origen} - {nombre_origen}")
    print(f"Destino -> {destino} - {nombre_destino}")

    if camino_extenso:

        print("Existe camino -> Sí")

        print("Camino encontrado:")

        for nodo in camino_extenso:
            nombre = grafo.articulos[nodo].nombre_articulo

            print(f"- {nodo} - {nombre}")

    else:
        print("Existe camino -> No")

    # ======================================
    # EXPORTAR RESULTADOS PAGERANK
    # ======================================

    with open(
            f"{carpeta_resultados}/ranking_pagerank.txt",
            "w",
            encoding="utf-8"
    ) as archivo:

        archivo.write("TOP PAGERANK\n\n")

        for id_articulo, valor in top_pagerank:

            articulo = grafo.articulos[id_articulo]

            archivo.write(
                f"Articulo: {articulo.nombre_articulo}\n"
            )

            archivo.write(
                f"Valor PageRank: {format(valor, '.10f')}\n"
            )

            archivo.write("Categorias:\n")

            if articulo.categorias:

                for id_categoria in articulo.categorias:

                    if id_categoria in grafo.categorias:
                        nombre_categoria = (
                            grafo.categorias[id_categoria]
                            .nombre_categoria
                        )

                        archivo.write(
                            f"- {nombre_categoria}\n"
                        )

            else:
                archivo.write("- Sin categorias\n")

            archivo.write("\n")


if __name__ == "__main__":
    main()
    
    #Print de carga finalizada
    
    print("\nAnálisis completado. Resultados guardados en la carpeta 'resultados'.")
    
    #Print de despedida
    
    print("\nGracias por utilizar el programa. ¡Hasta luego!")