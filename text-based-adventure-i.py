#This is the main file of the game

#Importing the documents we need
#setup_classes is used to define the Classes
import setup_classes as sc
import turn_settup as ts
import csv

#Create the gear to unlock
gear_to_unlock = [sc.Gear]
with open("easy_campaign_gear.csv", newline="") as easy_gear:
    read_easy_gear = csv.reader(easy_gear)
    next(read_easy_gear)
    for row in read_easy_gear:
        aux_gear = sc.Gear(str(row[0]), int(row[1]), int(row[2]))
        gear_to_unlock.append(aux_gear)

#Create monsters to battle
monsters_to_battle = [sc.Warrior]
with open("easy_campaign_monsters.csv", newline="") as easy_monsters:
    read_easy_monsters = csv.reader(easy_monsters)
    next(read_easy_monsters)
    for row in read_easy_monsters:
        aux_monster = sc.Warrior(str(row[0]), int(row[1]), int(row[2]), int(row[3]))
        monsters_to_battle.append(aux_monster)

first_player = sc.Warrior("Player 1", 100, 10, 10)
first_item = sc.Item("hp_item", 100, "primer item")
second_item = sc.Item("atk_item", 100, "primer item")
third_item = sc.Item("def_item", 100, "primer item")
first_player.bag_items.append(first_item)
first_player.bag_items.append(second_item)
first_player.bag_items.append(third_item)
gear_item_1 = sc.Gear("Spear of death", 5, -5,)
gear_item_2 = sc.Gear("Shield of power", -5, 5)
first_player.add_to_gear_bag(gear_item_1)
first_player.add_to_gear_bag(gear_item_2)

monsters_index = 1
while first_player.is_alive():
    first_player.player_print()
    print("\nvs\n")
    monsters_to_battle[monsters_index].monster_print()
    ts.turn(first_player, monsters_to_battle[monsters_index])
    monsters_index += 1


