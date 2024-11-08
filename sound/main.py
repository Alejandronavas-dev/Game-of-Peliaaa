import time  # Importa la biblioteca time para controlar el retraso entre los mensajes
from controller.town_controller import TownController
from controller.battle_controller import BattleController
from model.character import Character     

def slow_print(message, delay=2):
    """Imprime un mensaje con un retraso específico para crear suspense."""
    for char in message:
        print(char, end='', flush=True)  # Imprime cada carácter uno a uno
        time.sleep(0.05)  # Retraso de 50ms entre cada carácter
    print()  # Imprime una nueva línea al final
    time.sleep(delay)  # Espera el tiempo especificado después de imprimir el mensaje

def main():
    """Función principal que controla el flujo del juego."""
    # Introducción del juego
    slow_print("En un reino olvidado por el tiempo, la oscuridad acecha...", delay=3)
    slow_print("Las leyendas hablan de un héroe que surgirá para desafiar al mal...", delay=3)
    slow_print("Pero, ¿quién será ese héroe?...", delay=3)
    slow_print("La respuesta yace en tu elección...", delay=3)

    name = input("Elige tu nombre: ")  # Nombre del jugador
    player_class = input("Elige tu clase (guerrero/mago/curador): ").lower()
    player = Character(name, 100, 10, 5, 0, player_class)  # Crea un personaje

    slow_print(f"¡Bienvenido, {player.name}! Tu aventura comienza ahora...", delay=3)

    town_controller = TownController(player)  # Controlador del pueblo
    battle_controller = BattleController(player)  # Controlador de combate

    while player.health > 0:  # Mientras el jugador esté vivo
        slow_print("¿Quieres visitar el pueblo (v) o explorar (e)?", delay=3)
        action = input("Elige tu acción: ").strip().lower()

        if action == 'v':
            town_controller.visit_town()  # Visita el pueblo
        elif action == 'e':
            battle_controller.start_battle()  # Inicia el combate
        else:
            print("Acción inválida.")

    slow_print("Has caído en batalla. Fin del juego.", delay=3)  # Mensaje final si el jugador pierde

if __name__ == "__main__":
    main()
