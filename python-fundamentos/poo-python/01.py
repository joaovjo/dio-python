class carro:
    def __init__(self, marca, modelo, cor, marchas, suspensao):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marchas = marchas
        self.suspensao = suspensao

    def exibir(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Cor:', self.cor)
        print('Marchas:', self.marchas)
        print('Suspensão:', self.suspensao)
        
    def ligar(self):
        print('Carro ligado')
        
    def desligar(self):
        print('Carro desligado')
    
    def acelerar(self):
        print('Acelerando')
    
    def frear(self):
        print('Freando')
    
    def trocar_marcha(self):
        print('Marcha trocada')
    
    def __str__(self):
        return f"Carro top: {self.marca} {self.modelo} {self.cor} {self.marchas} {self.suspensao}"
    
carro1 = carro('Fiat', 'Uno', 'Vermelho', 5, 'Macia')
carro1.exibir()

