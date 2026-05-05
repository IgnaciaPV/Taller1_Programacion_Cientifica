class LectorArch:
    @staticmethod
    def leer_mtx_filtrado(ruta, limite=10000):
        enlaces = []

        with open(ruta, "r", encoding="utf-8") as archivo:
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