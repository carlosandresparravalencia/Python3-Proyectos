# @author Carlos Andres Parra Valencia

import string
letras = list(string.ascii_uppercase)


def siguienteIdDominio(antId):
    antIdNum = int(antId[4:7])
    if antIdNum < 999:
        if antIdNum >= 99:
            nextId = antId[0:4] + str(int(antId[4:7]) + 1)
            return nextId
        elif antIdNum >= 9 and antIdNum < 99:
            nextId = antId[0:4] + '0' + str(int(antId[4:7]) + 1)
            return nextId
        else:
            nextId = antId[0:4] + '00' + str(int(antId[4:7]) + 1)
            return nextId
    else:
        # Cuarta letra
        antIdLetra = antId[3:4]
        if antIdLetra != 'Z':
            # Guardar la siguiente letra
            nextIdLetra = letras.index(antIdLetra) + 1
            nextId = antId[0:3] + letras[nextIdLetra] + '001'
            return nextId
        else:
            # Tercera letra
            antIdLetra = antId[2:3]
            if antIdLetra != 'Z':
                # Guardar la siguiente letra
                nextIdLetra = letras.index(antIdLetra) + 1
                nextId = antId[0:2] + letras[nextIdLetra] + 'Z' + '001'
                return nextId
            else:
                # Segunda letra
                antIdLetra = antId[1:2]
                if antIdLetra != 'Z':
                    # Guardar la siguiente letra
                    nextIdLetra = letras.index(antIdLetra) + 1
                    nextId = antId[0:1] + letras[nextIdLetra] + 'ZZ' + '001'
                    return nextId
                else:
                    # Primer letra
                    antIdLetra = antId[0:1]
                    if antIdLetra != 'Z':
                        # Guardar la siguiente letra
                        nextIdLetra = letras.index(antIdLetra) + 1
                        nextId = letras[nextIdLetra] + 'ZZZ' + '001'
                        return nextId

# Ingresar String ultimo id registrado
print(siguienteIdDominio('ABZZ099'))
print()
print(siguienteIdDominio('ABCD009'))
print()
print(siguienteIdDominio('FFFF999'))