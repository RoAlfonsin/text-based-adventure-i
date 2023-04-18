#This is the main file of the game

#Importing the documents we need
#setup_classes is used to define the Classes
import setup_classes as sc
import turn_settup as ts
import csv
import time 

startingtime = time.localtime()
first_player = sc.Warrior("Player 1", 150, 25, 25)

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

#A items to bag
with open("easy_campaign_items.csv", newline="") as easy_items:
    read_easy_items = csv.reader(easy_items)
    next(read_easy_items)
    for row in read_easy_items:
        new_item = sc.Item(str(row[0]), str(row[1]), int(row[2]))
        first_player.bag_items.append(new_item)


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
    first_player.add_to_gear_bag(gear_to_unlock[monsters_index])
    monsters_index += 1
    if monsters_index > 15:
        print("\nCongratulations You Won The Game!!!\n")
        break

if first_player.is_alive():
    endtime = time.localtime()
    score = int(endtime.tm_sec) - int(startingtime.tm_sec)
    new_scores = {score: first_player.description}

    with open("High-Scores.csv", newline="") as highscores_file:
        highscore_reader = csv.reader(highscores_file)
        for row in highscore_reader:
            new_scores[int(row[1])] = row[0]

    scores_sorted = sorted(new_scores)
    print("List of Scores")
    for key_scores in scores_sorted:
        print(new_scores[key_scores], "-", key_scores)

    with open("High-Scores.csv", "w") as scores_file:
        scores_writer = csv.writer(scores_file)
        for key_score in scores_sorted:
            string_to_write = [str(new_scores[key_score]),str(key_score)]
            scores_writer.writerow(string_to_write)
