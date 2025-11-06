class nodo_libro:
  def __init__(self, libro):
    self.libro = libro
    self.izq = None
    self.der = None
    
class libro_arbol:    
    def __init__(self):
        self.raiz = None
        
    def insert_libro(self, libro):
        if self.raiz is None:
            self.raiz = nodo_libro(libro)
        else:
            self._insertar_recursivo(self.raiz, libro)
            
    def _insertar_recursivo(self, nodo, libro):
        if libro["isbn"] < nodo.libro["isbn"]:
            if nodo.izq is None:
                nodo.izq = nodo_libro(libro)
            else:
                self._insertar_recursivo(nodo.izq, libro)
        elif libro["isbn"] > nodo.libro["isbn"]:
            if nodo.der is None:
                nodo.der = nodo_libro(libro)
            else:
                self._insertar_recursivo(nodo.der, libro)
        else:
            nodo.libro = libro
            
    def buscar(self, isbn):
        return self._buscar_recursivo(self.raiz, isbn)
    
    def consultar_por_nombre(self, title):
        return self._buscar_nombre(self.raiz, title)
    
    def _buscar_recursivo(self, nodo, isbn):
        if nodo is None:
            return None
        if isbn == nodo.libro["isbn"]:
            return nodo.libro
        elif isbn < nodo.libro["isbn"]:
            return self._buscar_recursivo(nodo.izq, isbn)
        else:
            return self._buscar_recursivo(nodo.der, isbn)
        
    def _buscar_nombre(self, nodo, title):
        if nodo is None:
            return None
        
        if nodo.libro["title"].strip().lower() == title.strip().lower():
            return nodo.libro
        
        left_search = self._buscar_nombre(nodo.izq, title)
        
        if left_search:
            return left_search
        return self._buscar_nombre(nodo.der, title)

    def listar(self):
        lista = []
        self._inorden(self.raiz, lista)
        return lista
    
    def _inorden(self, nodo, lista):
        if nodo is not None:
            self._inorden(nodo.izq, lista)
            lista.append(nodo.libro)
            self._inorden(nodo.der, lista)