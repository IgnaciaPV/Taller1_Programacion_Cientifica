class Articulo:
    
    def __init__(self, id_articulo, nombre_articulo):
        
        self.id_articulo = id_articulo
        self.nombre_articulo = nombre_articulo
        
        #Agregamos una lista de categorias a cada articulo,
        # para luego poder relacionar cada articulo con sus categorias
        # correspondientes, y asi construir el grafo de articulos y categorias.
        self.categorias=[]  
        
        #El "wiki-topcats.mtx" nos entrega que un articulo tiene enlace con otro
        
        self.enlace_origen=[]
        
        self.enlace_destino=[]

    def agregar_categoria(self, id_categoria):
        
        if id_categoria not in self.categorias:
        
            self.categorias.append(id_categoria)
            
    def agregar_enlace_destino(self, id_articulo_destino):
        
        if id_articulo_destino not in self.enlace_destino:
            self.enlace_destino.append(id_articulo_destino)

    def agregar_enlace_origen(self, id_articulo_origen):
        if id_articulo_origen not in self.enlace_origen:
            self.enlace_origen.append(id_articulo_origen)

