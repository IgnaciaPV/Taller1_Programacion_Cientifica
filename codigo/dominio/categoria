class Categoria:
    
    def __init__(self, id_categoria, nombre_categoria):
        
        # Constructor de la clase Categoria.
        # Se ejecuta automáticamente cuando se crea un objeto de tipo Categoria.

        # Lista donde se almacenarán los identificadores de los artículos
        # que pertenecen a esta categoría.    
        self.articulos=[]
        
        # Identificador único de la categoría.
        # Sirve para distinguir una categoría de otra.
        self.id_categoria = id_categoria
        
        # Nombre descriptivo de la categoría.
        # Por ejemplo: "Ciencia", "Historia", "Matemáticas".        
        self.nombre_categoria = nombre_categoria
        
    # Método que permite asociar un artículo a esta categoría.
    # Recibe como parámetro el identificador del artículo.   
    def agregar_articulo(self, id_articulo):
        
        # Verifica si el artículo aún no está registrado en la lista.
        # Esto evita agregar el mismo artículo más de una vez.
        
        if id_articulo not in self.articulos:
            
            # Si el artículo no estaba en la lista, se agrega.
            self.articulos.append(id_articulo)
            