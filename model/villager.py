# model/villager.py

from model.mission import Mission  # Importa la clase Mission

class Villager:
    """Clase que representa un aldeano en el juego."""
    
    def __init__(self, name):
        self.name = name  # Nombre del aldeano

    def talk(self):
        """Método para que el aldeano hable."""
        return f"Hola, soy {self.name}. Estoy buscando ayuda para recuperar el amuleto perdido en el bosque."

    def give_quest(self):
        """Método para que el aldeano dé una misión al jugador."""
        return Mission("Amuleto Perdido", "Encuentra el amuleto en el bosque.", 50)  # Crea una misión
