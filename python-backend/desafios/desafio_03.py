# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
entrada = "0,10,20,30,40,-5,-15,5,15,25,12,25,30,18,5"

temperaturas_celsius = entrada.split(",")
# temperaturas_celsius = input().split(",")


# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(TC) for TC in temperaturas_celsius]

    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []

    for TC in temperaturas_celsius:
        TF = (TC * 9 / 5) + 32
        temperaturas_fahrenheit.append(TF)

    return temperaturas_fahrenheit


# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))
