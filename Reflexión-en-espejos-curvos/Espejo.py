class Espejo():
    def __init__(self):
        self.__distanciaObjeto = 0  # S
        self.__distanciaImagen = 0  # S´
        self.__distanciaFocal = 0  # Foco
        self.__radioEspejo = 0  # Radio
        self.__grandorObjeto = 0  # Y
        self.__grandorImagen = 0  # Y´

    # Get
    def darDistanciaObjeto(self):
        return self.__distanciaObjeto

    # Set
    def recibirDistanciaObjeto(self, pDistanciaObjeto):
        self.__distanciaObjeto = pDistanciaObjeto

    # Get
    def darDistanciaImagen(self):
        return self.__distanciaImagen

    # Set
    def recibirDistanciaImagen(self, pDistanciaImagen):
        self.__distanciaImagen = pDistanciaImagen

    # Get
    def darDistanciaFocal(self):
        return self.__distanciaFocal

    # Set
    def recibirDistanciaFocal(self, pDistanciaFocal):
        self.__distanciaFocal = pDistanciaFocal

    # Get
    def darRadioEspejo(self):
        return self.__radioEspejo

    # Set
    def recibirRadioEspejo(self, pRadioEspejo):
        self.__radioEspejo = pRadioEspejo

    # Get
    def darGrandorObjeto(self):
        return self.__grandorObjeto

    # Set
    def recibirGrandorObjeto(self, pGrandorObjeto):
        self.__grandorObjeto = pGrandorObjeto

    # Get
    def darGrandorImagen(self):
        return self.__grandorImagen

    # Set
    def recibirGrandorImagen(self, pGrandorImagen):
        self.__grandorImagen = pGrandorImagen

    def calcularDistanciaFocal(self):
        self.__distanciaFocal = self.__radioEspejo / 2

    # Imagen => S'
    def calcularDistanciaImagen(self):
        self.calcularDistanciaFocal()
        self.__distanciaImagen = self.__distanciaFocal * self.__distanciaObjeto / \
            (self.__distanciaObjeto - self.__distanciaFocal)

    # Imagen => y'
    def calcularGrandorImagen(self):
        if self.__distanciaObjeto == 0:
            self.calcularDistanciaObjeto()

        self.calcularDistanciaImagen()
        self.__grandorImagen = (-(self.__distanciaImagen *
                                self.__grandorObjeto) / self.__distanciaObjeto)

    # Objeto => S
    def calcularDistanciaObjeto(self):
        self.calcularDistanciaFocal()
        self.__distanciaObjeto = self.__distanciaFocal * self.__distanciaImagen / \
            (self.__distanciaImagen - self.__distanciaFocal)

    # Objeto => Y
    def calcularGrandorObjeto(self):
        self.calcularDistanciaObjeto()
        self.__grandorObjeto = - \
            (self.__grandorImagen * self.__distanciaObjeto) / self.__distanciaImagen


'''
espejo = Espejo()
print(espejo.darDistanciaObjeto())
print(espejo.recibirDistanciaObjeto(1000))
print(espejo.darDistanciaObjeto())
print(espejo.darDistanciaImagen())
print(espejo.recibirDistanciaImagen(900))
print(espejo.darDistanciaImagen())
print(espejo.darDistanciaFocal())
print(espejo.recibirDistanciaFocal(800))
print(espejo.darDistanciaFocal())
print(espejo.darRadioEspejo())
print(espejo.recibirRadioEspejo(700))
print(espejo.darRadioEspejo())
print(espejo.darGrandorObjeto())
print(espejo.recibirGrandorObjeto(600))
print(espejo.darGrandorObjeto())
print(espejo.darGrandorImagen())
print(espejo.recibirGrandorImagen(500))
print(espejo.darGrandorImagen())
'''
