# model/item.py

class Item:
    """Clase que representa un objeto en el juego."""
    
    def __init__(self, name, effect):
        self.name = name  # Nombre del objeto
        self.effect = effect  # Efecto del objeto

    def use(self, character):
        """Usa el objeto en un personaje."""
        if self.effect == "heal":
            character.health += 20  # Recupera 20 puntos de salud
            print(f"{character.name} ha usado {self.name} y ha recuperado 20 puntos de salud.")
        else:
            print(f"{self.name} no tiene un efecto conocido.")  # Mensaje si el efecto no es conocido
