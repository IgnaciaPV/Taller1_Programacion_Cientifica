import os
import matplotlib.pyplot as plt
from dominio.articulos import Articulo
from dominio.categoria import Categoria
from dominio.grafoarticulocategoria import GrafoArticuloCategoria
from dominio.lector_datos import LectorArch


def main():

    grafo = GrafoArticuloCategoria()
    # CARPETA RESULTADOS
    carpeta_resultados = "../../resultados"
    os.makedirs(carpeta_resultados, exist_ok=True)

    # LECTURA DATASETS
    enlaces = LectorArch.leer_mtx_filtrado("../../datos/wiki-topcats.mtx",limite=10000)

    relaciones = LectorArch.leer_mtx_categorias("../../datos/wiki-topcats_Categories.mtx",limite=10000)

    nombres_articulos = LectorArch.leer_nombres_articulos("../../datos/wiki-topcats_pagenames.txt")

    nombres_categorias = LectorArch.leer_nombres_categorias("../../datos/wiki-topcats_Category_names.txt")

    articulo_por_id = {
        i + 1: nombre
        for i, nombre in enumerate(nombres_articulos)
    }

    categoria_por_id = {
        i + 1: nombre
        for i, nombre in enumerate(nombres_categorias)
    }

    # CREACION GRAFO
    for origen, destino in enlaces:
        if origen not in grafo.articulos:
            grafo.agregar_articulo(Articulo(origen, articulo_por_id.get(origen, f"Articulo {origen}") ))

        if destino not in grafo.articulos:
            grafo.agregar_articulo(Articulo(destino,articulo_por_id.get(destino, f"Articulo {destino}")))

        grafo.agregar_enlace(origen, destino)

    for id_articulo, id_categoria in relaciones:
        if id_articulo not in grafo.articulos:
            grafo.agregar_articulo(Articulo(id_articulo,articulo_por_id.get(id_articulo,f"Articulo {id_articulo}")))

        if id_categoria not in grafo.categorias:
            grafo.agregar_categoria(Categoria(id_categoria,categoria_por_id.get(id_categoria,f"Categoria {id_categoria}")))

        grafo.asociar_articulo_categoria(id_articulo,id_categoria)

    # BFS Y DFS
    inicio = list(grafo.articulos.keys())[0]
    resultado_bfs = grafo.bfs(inicio)
    print("BFS:", resultado_bfs[:10])
    resultado_dfs = grafo.dfs(inicio)
    print("DFS:", resultado_dfs[:10])

    # CAMINO SIMPLE
    lista_articulos = list(grafo.articulos.keys())
    articulo_origen = lista_articulos[0]
    articulo_destino = lista_articulos[1]

    camino = grafo.existe_camino(articulo_origen,articulo_destino)

    print("\nCamino encontrado:", camino)

    # =========================
    # GRADO ENTRADA
    # =========================

    top_articulos = grafo.articulos_mayor_grado_entrada()

    print("\nArticulos con mayor grado de entrada:")

    for articulo, grado in top_articulos:

        nombre = grafo.articulos[articulo].nombre_articulo

        print(nombre, "-", grado)

    # =========================
    # GRAFICO GRADO ENTRADA
    # =========================

    nombres = []
    grados = []

    for articulo, grado in top_articulos:

        nombre = grafo.articulos[articulo].nombre_articulo

        nombres.append(nombre)
        grados.append(grado)

    plt.figure(figsize=(10, 5))

    plt.bar(nombres, grados)

    plt.xticks(rotation=45, ha="right")

    plt.title("Top articulos por grado de entrada")

    plt.xlabel("Articulos")
    plt.ylabel("Cantidad enlaces entrantes")

    plt.tight_layout()

    plt.savefig(f"{carpeta_resultados}/grafico_grado_entrada.png")

    plt.show()

    # =========================
    # PAGERANK
    # =========================

    ranks = grafo.pagerank()

    top_pagerank = sorted(ranks.items(),key=lambda x: x[1],reverse=True)[:10]

    print("\nTop PageRank:")

    for id_articulo, valor in top_pagerank:
        nombre = grafo.articulos[id_articulo].nombre_articulo
        print(nombre, "-", round(valor, 6))

    # =========================
    # TXT PAGERANK
    # =========================

    with open(
        f"{carpeta_resultados}/ranking_pagerank.txt", "w",encoding="utf-8") as archivo:
        archivo.write("Top PageRank\n\n")

        for id_articulo, valor in top_pagerank:
            nombre = grafo.articulos[id_articulo].nombre_articulo
            archivo.write(f"{nombre} - {round(valor, 6)}\n")

    # GRAFICO PAGERANK
    nombres_pagerank = []
    valores_pagerank = []

    for id_articulo, valor in top_pagerank:
        nombre = grafo.articulos[id_articulo].nombre_articulo
        nombres_pagerank.append(nombre)
        valores_pagerank.append(valor)

    plt.figure(figsize=(10, 5))

    plt.bar(nombres_pagerank,valores_pagerank)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top articulos por PageRank")
    plt.xlabel("Articulos")
    plt.ylabel("Valor PageRank")
    plt.tight_layout()
    plt.savefig(f"{carpeta_resultados}/grafico_pagerank.png")

    plt.show()

    # =========================
    # HISTOGRAMA GRADOS
    # =========================

    grados_totales = []

    for id_articulo in grafo.articulos:
        grado = grafo.grado_entrada(id_articulo)
        grados_totales.append(grado)

    plt.figure(figsize=(10, 5))
    plt.hist(grados_totales, bins=30)
    plt.title("Distribucion de grados")
    plt.xlabel("Cantidad enlaces entrantes")
    plt.ylabel("Cantidad articulos")
    plt.tight_layout()

    plt.savefig(f"{carpeta_resultados}/histograma_grados.png")

    plt.show()


if __name__ == "__main__":
    main()