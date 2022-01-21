import random
#INICIO DEL JUEGO LA GUÍA DEL VIAJAEROINTERGALACTICO

print(f" _                  _____ _    _  __            _____  ______ _       __      _______              _ ______ _____   ____    _____ _   _ _______ ______ _____   _____          _         __   _____ _______ _____ _____ ____  ")
print(f"| |        /\      / ____| |  | |/_/    /\     |  __ \|  ____| |      \ \    / /_   _|   /\       | |  ____|  __ \ / __ \  |_   _| \ | |__   __|  ____|  __ \ / ____|   /\   | |       /_/  / ____|__   __|_   _/ ____/ __ \ ")
print(f"| |       /  \    | |  __| |  | |_ _|  /  \    | |  | | |__  | |       \ \  / /  | |    /  \      | | |__  | |__) | |  | |   | | |  \| |  | |  | |__  | |__) | |  __   /  \  | |       / \ | |       | |    | || |   | |  | |")
print(f"| |      / /\ \   | | |_ | |  | || |  / /\ \   | |  | |  __| | |        \ \/ /   | |   / /\ \ _   | |  __| |  _  /| |  | |   | | | . ` |  | |  |  __| |  _  /| | |_ | / /\ \ | |      / _ \| |       | |    | || |   | |  | |")
print(f"| |____ / ____ \  | |__| | |__| || | / ____ \  | |__| | |____| |____     \  /   _| |_ / ____ \ |__| | |____| | \ \| |__| |  _| |_| |\  |  | |  | |____| | \ \| |__| |/ ____ \| |____ / ___ \ |____   | |   _| || |___| |__| |")
print(f"|______/_/    \_\  \_____|\____/|___/_/    \_\ |_____/|______|______|     \/   |_____/_/    \_\____/|______|_|  \_ \____/  |_____|_| \_|  |_|  |______|_|  \_\_____ /_/    \_\______/_/   \_\_____|  |_|  |_____\_____\____/ ")

inicio1 = input("Bienvenido para comenzar a jugar Pulsa Cualquier tecla")
print(inicio1)


#SUMA DE LOS 3 DADOS
def primerasuma(dado1, dado2, dado3):
    primerasuma = dado1 + dado2 + dado3
    return primerasuma

#COMIENZA LA PARTIDA
def partida():
    casillas = 0
    muerte = 33
    extraterrestres = 31
    tirada = 0
    resultadofinal =0

    #BUCLE HASTA LA CASILLA 42 SI ES 33 MUERE
    while (casillas<42 and casillas != muerte):

        #INICIO 2 Q AL PULSAR TIRARA LOS DADOS
        inicio2 = input("Pulsa Cualquier tecla para tirar los dados")
        print(inicio2)


        #LOS DADOS SACAN UN NUMERO RANDOM DESDE 0 AL 9
        dado1=(random.randrange(10))
        dado2=(random.randrange(10))
        dado3=(random.randrange(10))

        #IMPRIME LOS RESULTADOS DE LOS DADOS
        print(f"Dado 1: {dado1}")
        print(f"Dado 2: {dado2}")
        print(f"Dado 3: {dado3}")

        #LLAMA A LA SUMA DE LOS 3 DADOS
        print(f"Resultado: {primerasuma(dado1,dado2,dado3)}")

        tirada = resultadofinal
        print(f"Has guardado {tirada}")

        #EL RUSULTADO DE LOS DADOS SE PARTEN Y SE SUMAN
        num = primerasuma(dado1,dado2,dado3)
        cortar1 = [int(a) for a in str(num)]
        resultadofinal=sum(cortar1)

        print(f"Has sacado un {resultadofinal}")



        resultado = resultadofinal - tirada
        resultado= abs(resultado)

        #CONDICION SI EL RESULTADO E SMUY PEQUEÑO NO AVANZA Y SACA MAS D EUN 4 SI AVANZARÁ DICHAS CASILLAS
        if resultado > 4:
            print(f"Te mueves a la casilla {casillas}")
        else:
            casillas =  resultado + casillas
            print(f"Lo siento esa galaxia es muy lejana te mueves a la casilla {casillas}")

        #CONDICION DE QUE SI CAE EN LA CASILLA 31(LOS EXTRATERRESTRES) TE MANDA A LA CASILLA 23
        if casillas == extraterrestres:
            casillas=23
            print(f"Te atacaron extraterrstres te mueves a la Galaxia {casillas}")

        #SI CAES JUSTO EN LA CASILLA 42 LLEGASTE A LA GALAXIA ADECUADA Y GANAS
        if casillas == 42:
            print(f"Muy Bien, Has GANADO Llegaste a la GALAXIA ACORDADA")

        #SI SUPERAS LA CASILLA 42 ENCUENTRAS UN MULTIVERSO Y GANAS
        if casillas > 42:
            print(f"Muy Bien, Has GANADO Encontraste Un MULTIVERSO")

#SE LLAMA A LA PARTIDA
partida()






