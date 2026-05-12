class GrafoArticuloCategoria:
    def __init__(self):
        
        #dicionario que almacena el objeto articulo
        self.articulos = {}
        
        #diccionario que almacena el objeto categoria
        self.categorias = {}
        
        #dicionario que almacena listas con el id origen del objeto articulo y el id 
        #destino del objeto articulo.
        self.adyacencia = {}
        
        #agregamos en el diccionario de objetos articulo usando como indice
        #el id del articulo (es unico) y como valor el objeto articulo
        
    def agregar_articulo(self, articulo):
        self.articulos[articulo.id_articulo] = articulo
        self.adyacencia[articulo.id_articulo] = []
        
        #agregamos en el diccionario de objetos categoria usando como indice
        #el id de la categoria (es unico) y como valor el objeto categoria
        
    def agregar_categoria(self, categoria):
        self.categorias[categoria.id_categoria] = categoria
        
        #agregamos en el diccionario de adyacencia una lista vacia para el punto de origen
        #y el punto de destino (enlaces).

    def agregar_enlace(self, id_origen, id_destino):
        if id_origen not in self.adyacencia:
            self.adyacencia[id_origen] = []

        self.adyacencia[id_origen].append(id_destino)

        if id_origen in self.articulos:
            self.articulos[id_origen].agregar_enlace_destino(id_destino)

        if id_destino in self.articulos:
            self.articulos[id_destino].agregar_enlace_origen(id_origen)

    def asociar_articulo_categoria(self, id_articulo, id_categoria):
        if id_articulo in self.articulos:
            self.articulos[id_articulo].agregar_categoria(id_categoria)

        if id_categoria in self.categorias:
            self.categorias[id_categoria].agregar_articulo(id_articulo)
            
    #cuántos artículos apuntan hacia ese artículo
    
    def grado_entrada(self, id_articulo):
        return len(self.articulos[id_articulo].enlace_origen)

    def grado_salida(self, id_articulo):
        return len(self.articulos[id_articulo].enlace_destino)

    def articulos_mayor_grado_entrada(self, top=10):
        grados = []

        for id_articulo in self.articulos:
            grado = self.grado_entrada(id_articulo)
            grados.append((id_articulo, grado))
        grados.sort(key=lambda x: x[1], reverse=True)
        return grados[:top]

    def bfs(self, inicio):
        visitados = set()
        cola = [inicio]
        recorrido = []

        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(actual)
                for vecino in self.adyacencia.get(actual, []):
                    if vecino not in visitados:
                        cola.append(vecino)
        return recorrido

    def dfs(self, inicio):
        visitados = set()
        pila = [inicio]
        recorrido = []

        while pila:
            actual = pila.pop()
            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(actual)
                for vecino in self.adyacencia.get(actual, []):
                    if vecino not in visitados:
                        pila.append(vecino)

        return recorrido

    def existe_camino(self, origen, destino):
        visitados = set()
        cola = [origen]

        while cola:
            actual = cola.pop(0)

            if actual == destino:
                return True

            if actual not in visitados:
                visitados.add(actual)

                for vecino in self.adyacencia.get(actual, []):
                    if vecino not in visitados:
                        cola.append(vecino)

        return False

    def pagerank(self, iteraciones=20, factor_amortiguacion=0.85):
        cantidad_nodos = len(self.articulos)
        rank = {}

        for id_articulo in self.articulos:
            rank[id_articulo] = 1 / cantidad_nodos


        for i in range(iteraciones):
            nuevo_rank = {}

            for id_articulo in self.articulos:
                suma = 0

                # Revisamos qué nodos apuntan al artículo actual
                for otro_articulo in self.articulos:

                    enlaces = self.articulos[otro_articulo].enlace_destino

                    if id_articulo in enlaces and len(enlaces) > 0:
                        suma += rank[otro_articulo] / len(enlaces)

                nuevo_rank[id_articulo] = (
                        (1 - factor_amortiguacion) / cantidad_nodos
                        + factor_amortiguacion * suma
                )
            rank = nuevo_rank

        return rank