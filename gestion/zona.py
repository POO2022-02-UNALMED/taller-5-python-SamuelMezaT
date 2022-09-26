class Zona:
    def __init__(self,nombre="",zoologico=None,animales=None):
        if animales==None:
            animales=[]
        self._nombre=nombre
        self._zoologico=zoologico
        self._animales=animales
    
    def agregarAnimales(self,animal):
        self._animales+=[animal]

    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre


    def getAnimales(self):
        return self._animales
    def setAnimales(self,animales):
        self._animales=animales
    

    def getZoo(self):
        return self._zoologico
    def setZoo(self,zoologico):
        self._zoologico=zoologico