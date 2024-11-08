# controller/battle_controller.py
import random 
# controller/battle_controller.py

from model.enemy import Enemy  # Importa la clase Enemy
# ... el resto de tu código
 # Asegúrate de importar la biblioteca random

import pygame
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
espada = pygame.mixer.Sound("sound/espada.wav")

class BattleController:
    def __init__(self, player):
        """Inicializa el controlador de combate."""
        self.player = player  # Referencia al jugador

    def generate_enemy(self):
        """Genera un enemigo aleatorio."""
        enemy_name = random.choice(["Lobo", "Orco", "Goblin"])  # Nombre aleatorio del enemigo
        enemy_health = random.randint(30, 100)  # Salud aleatoria del enemigo
        enemy_attack = random.randint(5, 15)  # Ataque aleatorio del enemigo
        return Enemy(enemy_name, enemy_health, enemy_attack)  # Devuelve el enemigo

    def start_battle(self):
        """Inicia una batalla entre el jugador y un enemigo."""
        enemy = self.generate_enemy()  # Genera un enemigo
        print(f"¡Un {enemy.name} aparece! Salud: {enemy.health}, Ataque: {enemy.attack}")

        while self.player.health > 0 and enemy.health > 0:
            action = input("¿Quieres atacar (1) o huir (2)? ").strip().lower()
            if action == '1':
                # El jugador ataca al enemigo
                enemy.health -= self.player.attack
                print(f"{self.player.name} ataca a {enemy.name} y causa {self.player.attack} puntos de daño.")
                print(f"Salud de {enemy.name}: {enemy.health}")
                espada.play()

                if enemy.health > 0:  # El enemigo ataca si aún está vivo
                    enemy.attack_character(self.player)  # Llama al método para que el enemigo ataque
                    print(f"Salud de {self.player.name}: {self.player.health}")

            elif action == '2':
                print(f"{self.player.name} ha huido de la batalla.")
                return  # Sale de la batalla
            else:
                print("Acción inválida.")  # Mensaje de error

        if self.player.health <= 0:
            print("¡Has sido derrotado!")  # Mensaje si el jugador es derrotado
        elif enemy.health <= 0:
            print(f"{enemy.name} ha sido derrotado. ¡Victoria!")  # Mensaje si el enemigo es derrotado
            self.player.coins += 20  # Otorga monedas al jugador
            print(f"{self.player.name} ha ganado 20 monedas. Total: {self.player.coins}")
