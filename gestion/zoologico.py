class Zoologico:
    def __init__(self,nombre="",ubicacion="",zona=None):
        if zona==None:
            zona=[]
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zona=zona

    def agregarZonas(self,zona):
        self._zona+=[zona]

    def cantidadTotalAnimales(self):
        x=0
        for zona in self._zona:
            x=x+zona.cantidadAnimales()
        return x
            
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre


    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    

    def getZona(self):
        return self._zona
    def setZona(self,zona):
        self._zona=zona