from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    _listado=[]
    def __init__(self, nombre="", edad=0, habitat="", genero="",colorplumas=""):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorplumas

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,colorplumas):
        self._colorPlumas=colorplumas
    @classmethod
    def getListado(cls):
        return cls._listado     

    @classmethod
    def crearHalcon(cls,nombre="",edad=0,genero=""):
        x=Ave(nombre,edad,genero)
        cls._listado+=[x]
        cls.halcones+=1
        x._colorPlumas="cafe glorioso"
        x.setHabitat("montanas")
        return x
        
    @classmethod
    def crearAguila(cls,nombre="",edad=0,genero=""):
        x=Ave(nombre,edad,genero)
        cls._listado+=[x]
        cls.aguilas+=1
        x._colorPlumas="blanco y amarillo"
        x.setHabitat("montanas")
        return x

    
    def movimiento(cls):
        return "volar"
    @classmethod
    def cantidadAves(cls):
        return cls.halcones+cls.aguilas