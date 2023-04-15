class Gear:
    def __init__(self, input_attack, input_defense, input_description):
        self.attack_modifier = input_attack
        self.defense_modifier = input_defense
        self.description = input_description + "equipped."

no_gear = Gear(0, 0, "No gear")        

#Item class that is used for every expendable item
#item_type is a string from [hp_item, atk_item, def_item]
class Item:    
    def __init__(self, input_type: str, input_value: int, input_description: str):
        self.item_type = input_type
        self.item_value = input_value
        self.description = input_description

class Warrior:
    
    def __init__(self, input_hp, input_attack, input_defense, input_description):
        self.max_hp_stat = input_hp
        self.attack_stat = input_attack
        self.defense_stat = input_defense
        self.health_stat = self.max_hp_stat
        self.equipped_gear = no_gear
        self.description = input_description
        self.bag_items = [Item]
        self.equipped_item_list = []
    
    def equip_item(self, item_to_equip: Item):
        self.equipped_item_list.append(item_to_equip)
        #On the next if's we modify the Warrior object stats
        if item_to_equip.item_type == "hp_item":
            self.health_stat += item_to_equip.item_value
        if item_to_equip.item_type == "atk_item":
            self.attack_stat += item_to_equip.item_value
        if item_to_equip.item_type == "def_item":
            self.defense_stat += item_to_equip.item_value
    
    def bag_items_print(self):
        print("Health Items")
        printing_atk_items = False
        printing_def_items = False
        for index in range(1, len(self.bag_items)):
            item_to_print = self.bag_items[index]
            if item_to_print.item_type == "hp_item":
                print(index, "-", item_to_print.description, item_to_print.item_value)
            if item_to_print.item_type == "atk_item":
                if not printing_atk_items:
                    printing_atk_items = True
                    print("Attack Items")
                print(index, "-",item_to_print.description, item_to_print.item_value)
            if item_to_print.item_type == "def_item":
                if not printing_def_items:
                    printing_def_items = True
                    print("Defense Items")
                print(index, "-",item_to_print.description, item_to_print.item_value)
                    
    
    def is_alive(self):
        if self.health_stat <= 0:
            return False
        else:
            return True
    
    def select_items(self):
        user_command = print('To equip an item input the id_number else input "Go"')
        self.bag_items_print(self.bag_items)
        while user_command != 'Go':
            break
    
    def action_attack(self, enemy):
        enemy.health_stat -= self.attack_stat - enemy.defense_stat 
        
        

