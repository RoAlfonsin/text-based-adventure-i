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
for element in gear_to_unlock:
    print(element)

first_player = sc.Warrior(100, 10, 10, "Player 1")
first_monster = sc.Warrior(10, 15, 9, "First monster created")
second_monster = sc.Warrior(20, 15, 9, "Second monster created")
first_item = sc.Item("hp_item", 100, "primer item")
second_item = sc.Item("atk_item", 100, "primer item")
third_item = sc.Item("def_item", 100, "primer item")
first_player.bag_items.append(first_item)
first_player.bag_items.append(second_item)
first_player.bag_items.append(third_item)
gear_item_1 = sc.Gear(5, -5, "Spear of death")
gear_item_2 = sc.Gear(-5, 5, "Shield of power")
first_player.add_to_gear_bag(gear_item_1)
first_player.add_to_gear_bag(gear_item_2)
#first_player.print_gear_bag()
#first_player.bag_items_print()
#first_player.equip_item(first_item)
#first_player.select_items()
ts.turn(first_player, first_monster)
print(first_player.health_stat)
ts.turn(first_player, second_monster)
print(first_player.health_stat)

