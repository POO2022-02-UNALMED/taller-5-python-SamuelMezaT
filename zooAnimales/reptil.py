from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self, nombre="", edad=0, habitat="", genero="",coloescamas="",largocola=0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=coloescamas
        self._largoCola=largocola
    @classmethod
    def getListado(cls):
        return cls._listado
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,escmas):
        self._colorEscamas=escmas


    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,_largoCola):
        self._largoCola=_largoCola
   
   

    @classmethod
    def crearIguana(cls,nombre="",edad=0,genero=""):
        x=Reptil(nombre,edad,genero)
        cls._listado+=[x]
        cls.iguanas+=1
        x._colorEscamas="blanco"
        x._largoCola=1
        x.setHabitat("jungla")
        return x
        
    @classmethod
    def crearSerpiente(cls,nombre="",edad=0,genero=""):
        x=Reptil(nombre,edad,genero)
        cls._listado+=[x]
        cls.serpientes+=1
        x._colorEscamas="verde"
        x._largoCola=3
        x.setHabitat("humedal")
        return x

    
    def movimiento(cls):
        return("reptar")
    @classmethod
    def cantidadReptiles(cls):
        return cls.iguanas+cls.serpientes