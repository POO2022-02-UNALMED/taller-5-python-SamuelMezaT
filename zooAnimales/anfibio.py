from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self, nombre="", edad=0, habitat="", genero="",colorpiel="",venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel=colorpiel
        self._venenoso=venenoso
    @classmethod
    def getListado(cls):
        return cls._listado
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,colorpiel):
        self._colorPiel=colorpiel


    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso
      

    @classmethod
    def crearRana(cls,nombre="",edad=0,genero=""):
        x=Anfibio(nombre,edad,genero)
        x._colorPiel,x._venenoso="rojo",False
        x.setHabitat("selva")
        cls._listado+=[x]
        cls.ranas+=1
        return x
        
    @classmethod
    def crearSalamandra(cls,nombre="",edad=0,genero=""):
        x=Anfibio(nombre,edad,genero)
        x._colorPiel,x._venenoso="negro y amarillo",False
        x.setHabitat("selva")
        cls._listado+=[x]
        cls.salamandras+=1
        return x
    @classmethod
    def cantidadAnfibios(cls):
        return cls.ranas +cls.salamandras
    

    def movimiento(cls):
        return "saltar"