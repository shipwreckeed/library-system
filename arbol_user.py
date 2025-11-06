class nodo_user:
  def __init__(self, usuario):
    self.usuario = usuario
    self.izq = None
    self.der = None


class user_arbol:
  def __init__(self):
    self.raiz = None

  def insert_user(self, usuario):
    if self.raiz is None:
      self.raiz = nodo_user(usuario)
    else:
      self._insertar_recursivo(self.raiz, usuario)
  
  def _insertar_recursivo(self, nodo, usuario):
    if usuario["nuip"] < nodo.usuario["nuip"]:
      if nodo.izq is None:
        nodo.izq = nodo_user(usuario)
      else:
        self._insertar_recursivo(nodo.izq, usuario)
    elif usuario["nuip"] > nodo.usuario["nuip"]:
      if nodo.der is None:
        nodo.der = nodo_user(usuario)
      else:
        self._insertar_recursivo(nodo.der, usuario)
    else:   
      nodo.usuario = usuario

  def buscar(self, nuip):
    return self._buscar_recursivo(self.raiz, nuip)

  def _buscar_recursivo(self, nodo, nuip):
    if nodo is None:
      return None
    if nuip == nodo.usuario["nuip"]:
      return nodo.usuario
    elif nuip < nodo.usuario["nuip"]:
      return self._buscar_recursivo(nodo.izq, nuip)
    else:
      return self._buscar_recursivo(nodo.der, nuip)
  
  def listar(self):
    lista = []
    self._inorden(self.raiz, lista)
    return lista

  def _inorden(self, nodo, lista):
    if nodo is not None:
        self._inorden(nodo.izq, lista)
        lista.append(nodo.usuario)
        self._inorden(nodo.der, lista)