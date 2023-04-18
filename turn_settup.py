import setup_classes as sc
import time

#This function controls the flow of one battle
def battle(player: sc.Warrior, monster: sc.Warrior):
    while player.is_alive() and monster.is_alive():
        player.action_attack(monster)
        if monster.is_alive():
            monster.action_attack(player)
        player_hp_to_print = max(player.health_stat, 0)
        monster_hp_to_print = max(monster.health_stat, 0)
        print(player.description, "HP:", player_hp_to_print, "-",  monster.description, "HP:", monster_hp_to_print)
        print("...")
        time.sleep(1.5)
        
#This function controls the flow of one turn
def turn(player: sc.Warrior, monster: sc.Warrior):
    player.select_gear()
    player.select_items()
    battle(player, monster)
    if player.is_alive():
        player.health_stat += 30
        player.remove_items()
        player.health_stat = min(player.health_stat, 250)
        player.buff_stats()
    else:
        print("GAME OVER")