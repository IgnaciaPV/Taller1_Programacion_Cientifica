# Taller 1 Programación Científica

- Ignacia Peña
- Francisco Cortés
- Fabián Díaz


<p align="center">
  <b>Análisis estructural de una red de artículos de Wikipedia mediante grafos dirigidos, métricas topológicas y PageRank simplificado.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Paradigma-POO-green" alt="POO">
  <img src="https://img.shields.io/badge/Grafos-Dirigidos-orange" alt="Grafos">
  <img src="https://img.shields.io/badge/NetworkX-No%20utilizado-red" alt="No NetworkX">
</p>

---

## Descripción del proyecto

Este proyecto corresponde al **Laboratorio 1 de Programación Científica**, cuyo objetivo es modelar y analizar una red de artículos de Wikipedia utilizando estructuras de datos y programación orientada a objetos.

Wikipedia puede entenderse como una red de conocimiento: cada artículo representa un nodo y cada enlace entre artículos representa una arista dirigida. A partir de esta representación, el sistema permite cargar datos reales, construir un subconjunto manejable del grafo, calcular métricas estructurales, recorrer la red y estimar la relevancia de los artículos mediante una versión simplificada del algoritmo **PageRank**.

El desarrollo se implementa en **Python**, sin utilizar librerías especializadas de grafos como `networkx`, con el propósito de construir explícitamente las estructuras internas del grafo y comprender su funcionamiento algorítmico.

---
### Objetivo general

Desarrollar un sistema en Python, basado en programación orientada a objetos, que permita representar, construir y analizar una red dirigida de artículos de Wikipedia.

### Objetivos específicos

- Representar artículos, categorías y relaciones mediante clases.
- Construir un grafo dirigido a partir de archivos reales del dataset.
- Asociar artículos con sus respectivas categorías.
- Calcular métricas estructurales básicas del grafo.
- Implementar recorridos BFS y DFS.
- Encontrar caminos simples entre artículos.
- Implementar una versión simplificada de PageRank.
- Analizar los artículos más relevantes y su relación con las categorías.
- Generar resultados claros por consola o mediante archivos de salida.

---
## Dataset utilizado

El proyecto utiliza el dataset público:

**Graphs SNAP Wiki — Kaggle**  
<https://www.kaggle.com/datasets/wolfram77/graphs-snap-wiki>

En particular, se trabaja principalmente con los archivos asociados a `wiki-topcats`, ya que estos contienen información relacionada con artículos, enlaces y categorías de Wikipedia.

Entre los archivos utilizados se consideran:

```text
wiki-topcats.mtx
wiki-topcats_Categories.mtx
wiki-topcats_pagenames.txt
wiki-topcats_Category_names.txt
```

El dataset contiene:

- Enlaces entre artículos.
- Identificadores de artículos.
- Nombres de artículos.
- Categorías asociadas a los artículos.
- Relaciones entre artículos y categorías.

```markdown
Debido al tamaño del dataset original, se trabaja con un subconjunto de 10.000 enlaces entre artículos y 10.000 relaciones artículo-categoría. Este filtrado permite mantener una ejecución manejable, reproducible y suficiente para aplicar métricas estructurales, recorridos y PageRank simplificado.

El subconjunto no pretende representar la totalidad de Wikipedia, sino permitir un análisis estructural acotado y verificable dentro de los objetivos del laboratorio.
```

## Estructura del proyecto

El proyecto se organiza separando datos, documentación, clases del dominio, lectores, ejecución principal y resultados.

```text
.
├── datos/
│   ├── README.txt
│   ├── wiki-topcats_Category_names.txt
│   └── wiki-topcats_pagenames.txt
│
├── documentacion/
│   ├── Diagrama_Clase_Taller1.pdf
│   ├── Taller_1_PC_S1_2026.pdf
│   └── README.md
│
├── codigo/
│   └── dominio/
│       ├── articulos.py
│       ├── categoria.py
│       ├── grafoarticulocategoria.py
│       ├── lector_datos.py
│       ├── lector_datosmtx.py
│       └── main.py
│
│
├── resultados/
│   ├── ranking_pagerank.txt
│   ├── top_grado_entrada.png
│   ├── top_pagerank.png
│   └── histograma_grados.png
│
└── .gitignore

```

---

## Descripción de carpetas

| Ruta | Descripción |
|---|---|
| `datos/` | Contiene archivos auxiliares del dataset y documentación para descargar los archivos `.mtx` necesarios. |
| `documentacion/` | Contiene el enunciado del taller, el informe y el diagrama de clases. |
| `codigo/dominio/` | Contiene las clases y lógica principal del sistema. |
| `codigo/dominio/main.py` | Archivo principal de ejecución del sistema. |
| `resultados/` | Contiene rankings y gráficos generados automáticamente. |

---
## Descarga de datasets

Los archivos `.mtx` del dataset no se incluyen directamente en el repositorio debido a su tamaño.

Para ejecutar correctamente el proyecto, descargar desde:

https://www.kaggle.com/datasets/wolfram77/graphs-snap-wiki

Luego ubicar en la carpeta `datos/` los siguientes archivos:

- `wiki-topcats.mtx`
- `wiki-topcats_Categories.mtx`

## Funcionalidades principales

| Funcionalidad | Estado |
|---|---|
| Modelado de artículos mediante clase `Articulo` | Implementado |
| Modelado de categorías mediante clase `Categoria` | Implementado |
| Construcción del grafo dirigido | Implementado |
| Representación mediante lista de adyacencia | Implementado |
| Lectura de archivos `.mtx` | Implementado |
| Lectura de nombres de artículos | Implementado |
| Lectura de nombres de categorías | Implementado |
| Asociación artículo-categoría | Implementado |
| Cálculo de grado de entrada | Implementado |
| Cálculo de grado de salida | Implementado |
| Recorrido BFS | Implementado |
| Recorrido DFS | Implementado |
| Verificación de camino entre artículos | Implementado |
| PageRank simplificado | Implementado |
| Exportación de ranking a `.txt` | Implementado |

---
## Modelo orientado a objetos

El sistema se organiza en tres clases principales: `Articulo`, `Categoria` y `GrafoArticuloCategoria`.

---

### Clase `Articulo`

Representa un artículo de Wikipedia.

Atributos principales:

| Atributo | Descripción |
|---|---|
| `id_articulo` | Identificador único del artículo. |
| `nombre_articulo` | Nombre del artículo. |
| `categorias` | Lista de categorías asociadas al artículo. |
| `enlace_origen` | Lista de artículos que apuntan hacia este artículo. |
| `enlace_destino` | Lista de artículos hacia los cuales apunta este artículo. |

Métodos principales:

| Método | Descripción |
|---|---|
| `agregar_categoria(id_categoria)` | Asocia una categoría al artículo evitando duplicados. |
| `agregar_enlace_destino(id_articulo_destino)` | Registra un enlace saliente desde el artículo actual. |
| `agregar_enlace_origen(id_articulo_origen)` | Registra un enlace entrante hacia el artículo actual. |

---

### Clase `Categoria`

Representa una categoría de Wikipedia.

Atributos principales:

| Atributo | Descripción |
|---|---|
| `id_categoria` | Identificador único de la categoría. |
| `nombre_categoria` | Nombre descriptivo de la categoría. |
| `articulos` | Lista de artículos asociados a la categoría. |

Método principal:

| Método | Descripción |
|---|---|
| `agregar_articulo(id_articulo)` | Asocia un artículo a la categoría evitando duplicados. |


---

### Clase `GrafoArticuloCategoria`

Representa el grafo dirigido de artículos de Wikipedia y mantiene, además, la asociación auxiliar entre artículos y categorías. La estructura principal del grafo corresponde a enlaces dirigidos entre artículos, mientras que las categorías se utilizan para contextualizar e interpretar los resultados obtenidos.

Atributos principales:

| Atributo | Descripción |
|---|---|
| `articulos` | Diccionario que almacena los artículos usando su ID como clave. |
| `categorias` | Diccionario que almacena las categorías usando su ID como clave. |
| `adyacencia` | Diccionario que representa la lista de adyacencia del grafo. |

Métodos principales:

| Método | Descripción |
|---|---|
| `agregar_articulo(articulo)` | Agrega un artículo al grafo. |
| `agregar_categoria(categoria)` | Agrega una categoría al grafo. |
| `agregar_enlace(id_origen, id_destino)` | Agrega una arista dirigida entre dos artículos. |
| `asociar_articulo_categoria(id_articulo, id_categoria)` | Relaciona un artículo con una categoría. |
| `grado_entrada(id_articulo)` | Calcula cuántos artículos apuntan hacia un artículo. |
| `grado_salida(id_articulo)` | Calcula cuántos enlaces salen desde un artículo. |
| `articulos_mayor_grado_entrada(top)` | Retorna los artículos con mayor grado de entrada. |
| `bfs(inicio)` | Realiza recorrido en anchura desde un artículo inicial. |
| `dfs(inicio)` | Realiza recorrido en profundidad desde un artículo inicial. |
| `existe_camino(origen, destino)` | Busca y retorna un camino simple entre dos artículos si existe. |
| `pagerank(iteraciones, factor_amortiguacion)` | Calcula el ranking de importancia de los artículos. |

---

## Representación del grafo

El grafo se representa mediante una **lista de adyacencia** implementada con diccionarios de Python.

Ejemplo conceptual:

```python
adyacencia = {
    1: [2, 5, 8],
    2: [3],
    3: [],
    5: [1, 4]
}
```

Esto significa que:

- El artículo `1` tiene enlaces hacia los artículos `2`, `5` y `8`.
- El artículo `2` tiene un enlace hacia el artículo `3`.
- El artículo `3` no posee enlaces salientes.
- El artículo `5` tiene enlaces hacia los artículos `1` y `4`.

Esta estructura permite consultar de forma directa los vecinos de cada nodo y aplicar recorridos como BFS, DFS y PageRank.

---

## Lectura de datos

La lectura de archivos se realiza mediante la clase `LectorArch`.

Actualmente se consideran métodos para:

| Método | Función |
|---|---|
| `leer_mtx_filtrado(ruta, limite)` | Lee enlaces entre artículos desde un archivo `.mtx`. |
| `leer_mtx_categorias(ruta, limite)` | Lee relaciones entre artículos y categorías desde un archivo `.mtx`. |
| `leer_nombres_articulos(ruta)` | Lee los nombres de los artículos desde un archivo `.txt`. |
| `leer_nombres_categorias(ruta)` | Lee los nombres de las categorías desde un archivo `.txt`. |

La lectura de archivos `.mtx` ignora líneas de comentario y líneas de metadatos. Luego interpreta las líneas con dos valores como relaciones entre identificadores.

---
##  Algoritmos implementados

###  Grado de entrada

El grado de entrada de un artículo corresponde a la cantidad de artículos que apuntan hacia él.

En términos del proyecto:

```text
grado_entrada(articulo) = cantidad de enlaces que llegan al artículo
```

Esta métrica permite identificar artículos que reciben muchas referencias desde otros artículos.

---
###  Grado de salida

El grado de salida corresponde a la cantidad de artículos hacia los cuales apunta un artículo determinado.

```text
grado_salida(articulo) = cantidad de enlaces que salen desde el artículo
```

Esta métrica permite identificar artículos que referencian muchas otras páginas.

---
### BFS

BFS, o búsqueda en anchura, recorre el grafo explorando primero los vecinos más cercanos al nodo inicial.

En el proyecto se utiliza para observar la conectividad alcanzable desde un artículo de partida.

---

### DFS

DFS, o búsqueda en profundidad, recorre el grafo avanzando lo más posible por una rama antes de retroceder.

En el proyecto se utiliza para explorar caminos dentro de la red dirigida.

---

### Existencia de camino

El método `existe_camino(origen, destino)` permite determinar si, partiendo desde un artículo de origen, es posible llegar a otro artículo de destino siguiendo los enlaces del grafo.

---

### PageRank simplificado

El algoritmo PageRank estima la relevancia de cada artículo considerando los enlaces entrantes y la importancia de los artículos que lo referencian.

La implementación considera:

- Inicialización uniforme del ranking.
- Número fijo de iteraciones.
- Factor de amortiguación.
- Distribución del valor de un artículo entre sus enlaces salientes.

Parámetros por defecto:

```text
iteraciones = 20
factor_amortiguacion = 0.85
```

---
## Flujo general del programa

El archivo `main.py` realiza las siguientes operaciones:

1. Crea una instancia de `GrafoArticuloCategoria`.
2. Lee enlaces desde `wiki-topcats.mtx`.
3. Lee relaciones artículo-categoría desde `wiki-topcats_Categories.mtx`.
4. Lee nombres de artículos desde `wiki-topcats_pagenames.txt`.
5. Lee nombres de categorías desde `wiki-topcats_Category_names.txt`.
6. Construye objetos de tipo `Articulo`.
7. Construye objetos de tipo `Categoria`.
8. Agrega enlaces dirigidos al grafo.
9. Asocia artículos con categorías.
10. Ejecuta BFS y DFS desde un artículo inicial.
11. Verifica si existe camino entre dos artículos.
12. Calcula artículos con mayor grado de entrada.
13. Calcula PageRank.
14. Exporta el ranking principal al archivo `ranking_pagerank.txt`.

---

## Resultados generados

Al ejecutar `main.py`, el sistema genera resultados por consola y archivos en la carpeta `resultados/`.

### Salida por consola

El programa muestra:

- Primeros nodos visitados mediante BFS.
- Primeros nodos visitados mediante DFS.
- Camino simple encontrado entre dos artículos, si existe.
- Artículos con mayor grado de entrada.
- Top de artículos según PageRank.

### Archivos generados

| Archivo | Descripción |
|---|---|
| `ranking_pagerank.txt` | Ranking textual de los artículos con mayor PageRank. |
| `top_grado_entrada.png` | Gráfico de los artículos con mayor cantidad de enlaces entrantes. |
| `top_pagerank.png` | Gráfico de los artículos con mayor valor de PageRank. |
| `histograma_grados.png` | Histograma de distribución de grados de entrada en el subconjunto analizado. |
