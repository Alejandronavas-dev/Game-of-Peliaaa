# model/enemy.py

class Enemy:
    """Clase que representa a un enemigo en el juego."""

    def __init__(self, name, health, attack, defense=0):
        """
        Inicializa un nuevo enemigo.
        
        :param name: str - Nombre del enemigo.
        :param health: int - Puntos de salud del enemigo.
        :param attack: int - Daño de ataque del enemigo.
        :param defense: int - Defensa del enemigo (opcional, por defecto es 0).
        """
        self.name = name  # Nombre del enemigo
        self.health = health  # Puntos de salud del enemigo
        self.attack = attack  # Daño de ataque del enemigo
        self.defense = defense  # Defensa del enemigo

    def attack_character(self, character):
        """
        Permite que el enemigo ataque a un personaje.
        
        :param character: Character - El personaje al que el enemigo atacará.
        """
        # Calcula el daño infligido teniendo en cuenta la defensa del personaje
        damage_dealt = max(0, self.attack - character.defense)
        character.health -= damage_dealt  # Resta el daño de la salud del personaje
        print(f"{self.name} ataca a {character.name} y causa {damage_dealt} puntos de daño.")  # Mensaje de ataque

    def is_defeated(self):
        """
        Verifica si el enemigo ha sido derrotado.
        
        :return: bool - True si el enemigo está derrotado, False en caso contrario.
        """
        return self.health <= 0  # Retorna True si la salud es menor o igual a 0

    def __str__(self):
        """
        Representación en cadena del enemigo, mostrando su estado.
        
        :return: str - Información del enemigo.
        """
        return f"{self.name}: Salud={self.health}, Ataque={self.attack}, Defensa={self.defense}"  # Retorna la info del enemigo

# Ejemplo de uso de la clase Enemy
if __name__ == "__main__":
    # Se puede descomentar el siguiente bloque para probar la clase Enemy de forma independiente
    enemy = Enemy(name="Orco", health=100, attack=15, defense=5)  # Crea un enemigo
    print(enemy)  # Imprime información del enemigo

    class Character:
        """Clase que representa un personaje en el juego (simplificada para pruebas)."""
        def __init__(self, name, health, attack, defense=0):
            self.name = name  # Nombre del personaje
            self.health = health  # Puntos de salud del personaje
            self.attack = attack  # Daño de ataque del personaje
            self.defense = defense  # Defensa del personaje

    player = Character(name="Héroe", health=100, attack=20, defense=5)  # Crea un personaje jugador
    enemy.attack_character(player)  # El enemigo ataca al jugador
    print(player.health)  # Imprime la salud del jugador de
