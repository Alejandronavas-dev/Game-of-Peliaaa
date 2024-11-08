# model/mission.py

class Mission:
    """Clase que representa una misión en el juego."""
    
    def __init__(self, title, description, reward):
        self.title = title  # Título de la misión
        self.description = description  # Descripción de la misión
        self.reward = reward  # Recompensa de la misión

    def __str__(self):
        """Representa la misión como una cadena de texto."""
        return f"Misión: {self.title} - {self.description} | Recompensa: {self.reward}"
