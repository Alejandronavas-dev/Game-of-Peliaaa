# controller/town_controller.py
import time
from model.villager import Villager  # Importa la clase Villager

def slow_print(message, delay=2):
    """Imprime un mensaje con un retraso específico para crear suspense."""
    for char in message:
        print(char, end='', flush=True)  # Imprime cada carácter uno a uno
        time.sleep(0.05)  # Retraso de 50ms entre cada carácter
    print()  # Imprime una nueva línea al final
    time.sleep(delay)  # Espera el tiempo especificado después de imprimir el mensaje

class TownController:
    """Clase que controla la lógica del pueblo y la interacción con los aldeanos."""
    
    def __init__(self, player):
        self.player = player  # Referencia al jugador
        self.villagers = [Villager("Ana"), Villager("Luis"), Villager("Pedro")]  # Lista de aldeanos

    def visit_town(self):
        """Método para visitar el pueblo y hablar con aldeanos."""
        print("Has llegado al pueblo. Aquí puedes hablar con los aldeanos.")
        for index, villager in enumerate(self.villagers):
            print(f"{index + 1}: {villager.name}")  # Muestra la lista de aldeanos

        choice = int(input("Elige a un aldeano para hablar (1-3): ")) - 1  # Elige un aldeano
        if 0 <= choice < len(self.villagers):
            villager = self.villagers[choice]  # Obtiene el aldeano elegido
            print(villager.talk())  # Muestra el diálogo del aldeano
            quest = villager.give_quest()  # Obtiene la misión del aldeano
            print(f"Has recibido la misión: {quest}")  # Muestra la misión
            return quest  # Devuelve la misión
        else:
            print("Selección inválida.")  # Mensaje de error
