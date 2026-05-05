class LectorArch:
    
    # Método estático: se puede llamar sin crear un objeto de tipo LectorArch.
    # Ejemplo:
    # enlaces = LectorArch.leer_mtx_filtrado("archivo.mtx")
    @staticmethod
    def leer_mtx_filtrado(ruta, limite=10000):
        
        # Lista donde se almacenarán los enlaces encontrados.
        # Cada enlace se guardará como una tupla: (origen, destino).
        enlaces = []
        
    
        # El uso de with asegura que el archivo se cierre automáticamente.
        with open(ruta, "r", encoding="utf-8") as archivo:
            
            # Recorre el archivo línea por línea.
            for linea in archivo:

                # En archivos .mtx, las líneas que comienzan con "%"
                # suelen ser comentarios o metadatos, por lo tanto se ignoran.
                if linea.startswith("%"):
                    continue

                partes = linea.strip().split()
                
                # Si la línea tiene 3 elementos, se ignora.
                # Normalmente esto puede corresponder a una línea de dimensiones
                # o a una arista con peso, dependiendo del archivo
                if len(partes) == 3:
                    continue

                # Si la línea tiene exactamente 2 elementos,
                # se interpreta como un enlace: origen -> destino.
                if len(partes) == 2:
                    
                    # Convierte ambos valores desde string a entero.
                    origen, destino = map(int, partes)
                    
                    # Guarda el enlace como una tupla.                   
                    enlaces.append((origen, destino))

                    # Si ya se alcanzó el límite definido,
                    # se detiene la lectura para trabajar con un subconjunto.
                    if len(enlaces) >= limite:
                        break
                    
        # Devuelve la lista de enlaces leídos desde el archivo.
        return enlaces