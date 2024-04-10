class Hero:
    def __init__(self, name, health = 100, attack_power = 20 ):
        self_name = name
        self_health = health
        self_attack_power = attack_power
    def attack(self, other):
        other.health -= self.attack.power
        print(f"{self.name} атакует {other.name}, нанося {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

import time

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        current_attack = self.player
        current_defender = self.computer

        while self.player.is_alive() and self.computer.is_alive():
            current_attacker.attack(current_defender)
            current_attacker, current_defender = current_defender, current_attacker
            time.sleep(1)

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена. Победитель - {winner.name}!")


if __name__ == "main":
    player_name = input("Введите имя вашего героя:")
    player_hero = Hero (player_name)
    computer_hero = Hero("Компьютерный Герой")


    game = Game(player_hero, computer_hero)
    game.start()


