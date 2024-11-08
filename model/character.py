# model/character.py

class Character:
    """Clase que representa a un personaje en el juego."""
    
    def __init__(self, name, health, attack, defense=0, coins=0, character_class="Guerrero"):
        self.name = name  # Nombre del personaje
        self.health = health  # Salud inicial del personaje
        self.attack = attack  # Ataque inicial del personaje
        self.defense = defense  # Defensa inicial del personaje (por defecto 0)
        self.coins = coins  # Monedas del personaje (por defecto 0)
        self.character_class = character_class  # Clase del personaje

    def __str__(self):
        """Representa el objeto como una cadena de texto."""
        return f"{self.name} - Clase: {self.character_class}, Salud: {self.health}, Ataque: {self.attack}, Defensa: {self.defense}, Monedas: {self.coins}"

    def level_up(self):
        """Aumenta el nivel del personaje."""
        self.health += 10  # Aumenta la salud en 10
        self.attack += 5  # Aumenta el ataque en 5
        self.defense += 2  # Aumenta la defensa en 2
        print(f"{self.name} ha subido de nivel!")  # Mensaje de nivelación
