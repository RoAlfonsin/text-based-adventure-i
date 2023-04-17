import setup_classes as sc
import time

def battle(player: sc.Warrior, monster: sc.Warrior):
    while player.is_alive() and monster.is_alive():
        player.action_attack(monster)
        if monster.is_alive():
            monster.action_attack(player)
        print(player.description, "HP:", player.health_stat, "-",  monster.description, "HP:", monster.health_stat)
        print("...")
        time.sleep(1.5)
        

def turn(player: sc.Warrior, monster: sc.Warrior):
    player.select_gear()
    player.select_items()
    battle(player, monster)
    if player.is_alive():
        player.remove_items()
    else:
        print("GAME OVER")