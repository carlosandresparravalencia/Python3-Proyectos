# Posición del objeto (S) tamaño de la imagen (Y´)
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
        ########
        elif pDistanciaImagen and pRadio and pGrandorObjeto:  # Hallar tamaño de la imagen => Y´
            self.__espejo.recibirDistanciaImagen(float(pDistanciaImagen))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.recibirGrandorObjeto(float(pGrandorObjeto))
            self.__espejo.calcularGrandorImagen()
        #######
        elif pDistanciaImagen and pRadio and pGrandorImagen:  # Hallar tamaño del objeto => Y
            self.__espejo.recibirDistanciaImagen(float(pDistanciaImagen))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.recibirGrandorImagen(float(pGrandorImagen))
            self.__espejo.calcularGrandorObjeto()
        elif pDistanciaImagen and pRadio:  # Hallar distancia del objeto => S
            self.__espejo.recibirDistanciaImagen(float(pDistanciaImagen))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.calcularDistanciaObjeto()
        elif pDistanciaObjeto and pRadio:  # Hallar distancia de la imagen => S´
            self.__espejo.recibirDistanciaObjeto(float(pDistanciaObjeto))
            self.__espejo.recibirRadioEspejo(float(pRadio))
            self.__espejo.calcularDistanciaImagen()


validar = Validar()
print(validar.validarDatos(pDistanciaObjeto="", pDistanciaImagen=82,
      pFoco="", pRadio=98, pGrandorObjeto=12, pGrandorImagen=""))

print(validar.darEspejo().darDistanciaObjeto())
print(validar.darEspejo().darGrandorImagen())  # Y´
