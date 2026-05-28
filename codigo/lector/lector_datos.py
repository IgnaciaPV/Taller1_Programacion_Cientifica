class LectorArch:
    @staticmethod
    def leer_mtx_filtrado(nom, limite=10000):
        enlaces = []

        with open(nom, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith("%"):
                    continue

                partes = linea.strip().split()

                if len(partes) == 3:
                    continue

                if len(partes) == 2:
                    origen, destino = map(int, partes)
                    enlaces.append((origen, destino))

                    if len(enlaces) >= limite:
                        break

        return enlaces

    @staticmethod
    def leer_mtx_categorias(nom, limite=10000):
        relaciones = []
        with open(nom, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith("%"):
                    continue

                partes = linea.strip().split()

                if len(partes) == 3:
                    continue

                if len(partes) == 2:
                    id_articulo, id_categoria = map(int, partes)
                    relaciones.append((id_articulo, id_categoria))

                    if len(relaciones) >= limite:
                        break
        return relaciones

    @staticmethod
    def leer_nombres_articulos(nom):
        nombres_articulos = []

        with open(nom, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                nombre = linea.strip()

                if nombre:
                    nombres_articulos.append(nombre)

        return nombres_articulos

    @staticmethod
    def leer_nombres_categorias(nom):
        nombres_categorias = []

        with open(nom, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                nombre = linea.strip()

                if nombre:
                    nombres_categorias.append(nombre)

        return nombres_categorias