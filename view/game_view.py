# view/game_view.py

class GameView:
    def display_start_message(self):
        print("Welcome to the RPG Game!")

    def display_message(self, message):
        print(message)

    def display_health(self, character):
        print(f"{character.name} Health: {character.health}")

    def display_winner(self, player):
        print(f"Congratulations {player.name}, you have defeated all enemies!")

    def display_mission(self, mission):
        print(f"Mission: {mission.description} Reward: {mission.reward} coins")

    def display_shop(self, shop_items):
        print("=== Shop Items ===")
        for index, item in enumerate(shop_items):
            print(f"{index + 1}: {item}")
        print("===================")
