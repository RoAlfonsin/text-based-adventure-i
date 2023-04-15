import setup_classes as sc

def battle(player: sc.Warrior, monster: sc.Warrior):
    while player.is_alive() and monster.is_alive():
        player.action_attack(monster)
        if monster.is_alive():
            monster.action_attack(player)
        print(player.health_stat, monster.health_stat)

def turn(player: sc.Warrior, monster: sc.Warrior):
    player.select_items()
    battle(player, monster)
    player.remove_items()