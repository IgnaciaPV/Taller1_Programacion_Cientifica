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

Debido al tamaño del dataset original, el proyecto permite trabajar con un **subconjunto filtrado** de datos, definido mediante criterios razonables para facilitar el análisis y asegurar una ejecución eficiente.

## Estructura del proyecto

El proyecto se organiza separando datos, documentación, clases del dominio, lectores, ejecución principal y resultados.

```text
.
├── datos/
│   ├── rfa/
│   ├── talk/
│   ├── topcats/
│   └── vote/
│
├── documentacion/
│   ├── Taller.pdf
│   ├── diagrama_clases.png
│   └── informe.pdf
│
├── codigo/
│   └── dominio/
│       ├── articulos.py
│       ├── categoria.py
│       ├── grafoarticulocategoria.py
│       ├── lector_datosmtx.py
│       ├── main.py
│       └── lector_datos.py
│
├── ranking_pagerank.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 6. Descripción de carpetas

| Ruta | Descripción |
|---|---|
| `datos/rfa/` | Contiene archivos asociados a la red RFA del dataset. |
| `datos/talk/` | Contiene archivos asociados a conversaciones o discusiones de Wikipedia. |
| `datos/topcats/` | Contiene los archivos principales usados para artículos, categorías y enlaces. |
| `datos/vote/` | Contiene archivos asociados a redes de votación. |
| `documentacion/` | Contiene el enunciado del taller, el informe y el diagrama de clases. |
| `codigo/dominio/` | Contiene las clases principales del modelo orientado a objetos y Contiene los módulos responsables de leer archivos `.txt` y `.mtx`. |
| `src/main.py` | Archivo principal de ejecución del sistema. |
| `ranking_pagerank.txt` | Archivo generado con los artículos mejor posicionados según PageRank. |

---
