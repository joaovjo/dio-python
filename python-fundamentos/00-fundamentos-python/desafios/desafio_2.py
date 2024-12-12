def verificador_ano_bissexto():
    ano = int(input('Digite um ano para saber se é bissexto: '))
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("O ano é bissexto")
    else:
        print("O ano não é bissexto")

verificador_ano_bissexto()