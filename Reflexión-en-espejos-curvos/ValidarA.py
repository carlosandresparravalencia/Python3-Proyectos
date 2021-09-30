# Determinar la posición de la imagen (S´) y tamaño de la imagen (Y´)
from Espejo import Espejo


class Validar():
    def __init__(self):
        self.__espejo = Espejo()

    def darEspejo(self):
        return self.__espejo

    def recibirEspejo(self, pEspejo):
        self.__espejo = pEspejo

    def validarDatos(self, pDistanciaObjeto, pDistanciaImagen, pFoco, pRadio, pGrandorObjeto, pGrandorImagen):
        if pDistanciaObjeto and pDistanciaImagen and pRadio and pGrandorObjeto and pGrandorImagen:
            return 'No es posible procesar todos los campos'
        elif pDistanciaObjeto and pRadio and pGrandorObjeto:  # Hallar tamaño de la imagen => Y´
            self.__espejo.recibirDistanciaObjeto(float(pDistanciaObjeto))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.recibirGrandorObjeto(float(pGrandorObjeto))
            self.__espejo.calcularGrandorImagen()
        elif pDistanciaObjeto and pRadio:  # Hallar distancia de la imagen => S´
            self.__espejo.recibirDistanciaObjeto(float(pDistanciaObjeto))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.calcularDistanciaImagen()


validar = Validar()
print(validar.validarDatos(pDistanciaObjeto=-22, pDistanciaImagen="",
      pFoco="", pRadio=98, pGrandorObjeto=12, pGrandorImagen=""))
print(validar.darEspejo().darDistanciaImagen())  # S´
print(validar.darEspejo().darGrandorImagen())  # Y´
