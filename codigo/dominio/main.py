from dominio.articulos import Articulo
from dominio.categoria import Categoria
from dominio.grafoarticulocategoria import GrafoArticuloCategoria
from dominio.lector_datos import LectorArch

def main():
    grafo = GrafoArticuloCategoria()

    enlaces = LectorArch.leer_mtx_filtrado("../../datos/wiki-topcats.mtx", limite=10000)
    relaciones = LectorArch.leer_mtx_categorias("../../datos/wiki-topcats_Categories.mtx", limite=10000)

    nombres_articulos = LectorArch.leer_nombres_articulos(
"../../datos/wiki-topcats_pagenames.txt")
    nombres_categorias = LectorArch.leer_nombres_categorias(
"../../datos/wiki-topcats_Category_names.txt")

    articulo_por_id = {i + 1: nombre for i, nombre in enumerate(nombres_articulos)}
    categoria_por_id = {i + 1: nombre for i, nombre in enumerate(nombres_categorias)}

    for origen, destino in enlaces:
        if origen not in grafo.articulos:
            grafo.agregar_articulo(Articulo(origen, articulo_por_id.get(origen, f"Articulo {origen}")))
        if destino not in grafo.articulos:
            grafo.agregar_articulo(Articulo(destino, articulo_por_id.get(destino, f"Articulo {destino}")))
        grafo.agregar_enlace(origen, destino)

    for id_articulo, id_categoria in relaciones:
        if id_articulo not in grafo.articulos:
            grafo.agregar_articulo(Articulo(id_articulo, articulo_por_id.get(id_articulo, f"Articulo {id_articulo}")))
        if id_categoria not in grafo.categorias:
            grafo.agregar_categoria(Categoria(id_categoria, categoria_por_id.get(id_categoria, f"Categoria {id_categoria}")))
        grafo.asociar_articulo_categoria(id_articulo, id_categoria)

    inicio = list(grafo.articulos.keys())[0]
    resultado_bfs = grafo.bfs(inicio)
    print("BFS:", resultado_bfs[:10])

    resultado_dfs = grafo.dfs(inicio)
    print("DFS:", resultado_dfs[:10])

    top_articulos = grafo.articulos_mayor_grado_entrada()

    print("\nArticulos con mayor grado de entrada:")

    for articulo, grado in top_articulos:
        nombre = grafo.articulos[articulo].nombre_articulo
        print(nombre, "-", grado)


if __name__ == "__main__":
    main()