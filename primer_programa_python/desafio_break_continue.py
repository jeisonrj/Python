def run():
    LIMITE = 1000
    contador = 0
    potencia= 2**contador
    while potencia < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia))
        contador += 1
        potencia= 2**contador

        # if potencia != 8:
        #     continue

        if potencia == 64:
            break


if __name__ =='__main__':
    run()