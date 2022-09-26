from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self, nombre="", edad=0, habitat="", genero="",coloescamas="",cantidadaletas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=coloescamas
        self._cantidadAletas=cantidadaletas
    @classmethod
    def getListado(cls):
        return cls._listado     
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,escmas):
        self._colorEscamas=escmas


    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,_cantidadAletas):
        self._cantidadAletas=_cantidadAletas

    @classmethod
    def crearSalmon(cls,nombre="",edad=0,genero=""):
        x=Pez(nombre,edad,genero)
        cls._listado+=[x]
        cls.salmones+=1
        x._cantidadAletas=6
        x._colorEscamas="rojo"
        x.setHabitat("oceano")
        return x
        
    @classmethod
    def crearBacalao(cls,nombre="",edad=0,genero=""):
        x=Pez(nombre,edad,genero)
        cls._listado+=[x]
        cls.bacalaos+=1
        x._cantidadAletas=6
        x._colorEscamas="gris"
        x.setHabitat("oceano")
        return x
    

    @classmethod
    def cantidadPeces(cls):
        return cls.bacalaos+cls.salmones
    def movimiento(self):
        return "nadar"