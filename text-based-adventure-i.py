#This is the main file of the game

#Importing the documents we need
#setup_classes is used to define the Classes
import setup_classes as sc
import turn_settup as ts

first_player = sc.Warrior(100, 10, 10, "Player 1")
first_monster = sc.Warrior(10, 15, 8, "First monster created")
second_monster = sc.Warrior(20, 15, 8, "Second monster created")
first_item = sc.Item("hp_item", 100, "primer item")
second_item = sc.Item("atk_item", 100, "primer item")
third_item = sc.Item("def_item", 100, "primer item")
first_player.bag_items.append(first_item)
first_player.bag_items.append(second_item)
first_player.bag_items.append(third_item)
#first_player.bag_items_print()
#first_player.equip_item(first_item)
#first_player.select_items()
ts.turn(first_player, first_monster)
print(first_player.health_stat)
ts.turn(first_player, second_monster)
print(first_player.health_stat)

