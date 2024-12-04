# pokeapi/models/pokemon.py
class Pokemon:
    def __init__(self, id, name, height, weight, abilities):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.abilities = abilities
    
    def __str__(self):
        return f"Pokemon {self.name} (ID: {self.id})"
