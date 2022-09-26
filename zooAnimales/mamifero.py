from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]
    def __init__(self, nombre="", edad=0, habitat="", genero="",pelaje=False,patas=0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje=pelaje
        self._patas=patas

    def setPatas(self,patas):
        self._patas=patas
    def getPatas(self):
        return self._patas
    
    def isPelaje(self):
        return self._pelaje
    def getPelaje(self,pelaje):
        self._pelaje=pelaje
        
    @classmethod
    def getListado(cls):
        return cls._listado


    @classmethod
    def crearCaballo(cls,nombre="",edad=0,genero=""):
        x=Mamifero(nombre,edad,genero)
        cls._listado+=[x]
        cls.caballos+=1
        x._patas=4
        x._pelaje=True
        x.setHabitat("pradera")
        return x

    @classmethod
    def crearLeon(cls,nombre="",edad=0,genero=""):
        x=Mamifero(nombre,edad,genero)
        cls._listado+=[x]
        cls.leones+=1
        x._patas=4
        x._pelaje=True
        x.setHabitat("selva")
        return x
    @classmethod
    def cantidadMamiferos(cls):
        return cls.caballos+cls.leones