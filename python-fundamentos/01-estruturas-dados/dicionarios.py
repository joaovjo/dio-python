pessoa = {"nome": "João", "idade":28}

pessoa = dict(nome="João", idade=28)

pessoa["telefone"] = "1234-5678"

print(pessoa["idade"])

municipe = {
    1: "João",
    2: "Maria",
    3: {
        "nome": "José",
        "idade": 28
    }
}

print(dict.keys(municipe))