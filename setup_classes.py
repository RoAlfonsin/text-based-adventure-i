class Gear:
    def __init__(self, input_description, input_attack, input_defense):
        self.description = input_description
        self.attack_modifier = input_attack
        self.defense_modifier = input_defense
    
    def __repr__(self):
        desc =  self.description
        atc = " - Atk: " + str(self.attack_modifier)
        df = " Def: " + str(self.defense_modifier)
        while len(desc) < 22:
            desc += " "
        while len(atc) < 11:
            atc += " "
        gear_print = desc + atc + df
        return gear_print


no_gear = Gear("No gear", 0, 0)        

#Item class that is used for every expendable item
#item_type is a string from [hp_item, atk_item, def_item]
class Item:    
    def __init__(self, input_description: str, input_type: str, input_value: int):
        self.item_type = input_type
        self.item_value = input_value
        self.description = input_description

class Warrior:
    
    def __init__(self, input_description, input_hp, input_attack, input_defense):
        self.max_hp_stat = input_hp
        self.attack_stat = input_attack
        self.defense_stat = input_defense
        self.health_stat = self.max_hp_stat
        self.equipped_gear = no_gear
        self.description = input_description
        self.bag_items = [Item]
        self.gear_bag = [Gear]
        self.equipped_item_list = []
    
    def add_to_gear_bag(self, gear_item: Gear):
        self.gear_bag.append(gear_item)
    
    def print_gear_bag(self):
        print("\nEquiped Gear:\n", self.equipped_gear)
        print("\nGear Bag")
        for index in range(1, len(self.gear_bag)):
            print(index, self.gear_bag[index])
    
    def equip_gear(self, gear_item: Gear):
        aux = self.equipped_gear
        self.attack_stat -= aux.attack_modifier
        self.defense_stat -= aux.defense_modifier
        self.gear_bag.append(aux)
        self.equipped_gear = gear_item
        self.attack_stat += gear_item.attack_modifier
        self.defense_stat += gear_item.defense_modifier
    
    def select_gear(self):
        self.print_gear_bag()
        user_command = str(input('\nTo equip Gear input the id_number else input "Go" '))
        while user_command != 'Go':
            if not user_command.isnumeric():
                print('ERROR! The command should be a number or "Go"')
                user_command = str(input('\nTo equip Gear input the id_number else input "Go" '))
                continue
            if int(user_command) >= len(self.gear_bag) or int(user_command) < 1:
                print("ERROR! The id_number was not found")
                user_command = str(input('\nTo equip Gear input the id_number else input "Go" '))
                continue
            
            aux_gear = self.gear_bag.pop(int(user_command))
            self.equip_gear(aux_gear)
            self.player_print()
            self.print_gear_bag()
            user_command = str(input('\nTo equip Gear input the id_number else input "Go" '))
        
    
    def equip_item(self, item_to_equip: Item):
        self.equipped_item_list.append(item_to_equip)
        #On the next if's we modify the Warrior object stats
        if item_to_equip.item_type == "hp_item":
            self.health_stat += item_to_equip.item_value
        if item_to_equip.item_type == "atk_item":
            self.attack_stat += item_to_equip.item_value
        if item_to_equip.item_type == "def_item":
            self.defense_stat += item_to_equip.item_value
    
    def remove_items(self):
        for item_to_remove in self.equipped_item_list:
            if item_to_remove.item_type == "hp_item":
                self.health_stat -= item_to_remove.item_value
            if item_to_remove.item_type == "atk_item":
                self.attack_stat -= item_to_remove.item_value
            if item_to_remove.item_type == "def_item":
                self.defense_stat -= item_to_remove.item_value
        if self.health_stat < 0:
            self.health_stat = 1
        self.equipped_item_list.clear()
            
    
    def bag_items_print(self):
        print("\nItems In Bag")
        printing_hp_items = False
        printing_atk_items = False
        printing_def_items = False
        for index in range(1, len(self.bag_items)):
            item_to_print = self.bag_items[index]
            if item_to_print.item_type == "hp_item":
                if not printing_hp_items:
                    printing_hp_items = True
                    print("\nHealth Items")                   
                print(index, "-", item_to_print.description, item_to_print.item_value)
            if item_to_print.item_type == "atk_item":
                if not printing_atk_items:
                    printing_atk_items = True
                    print("\nAttack Items")
                print(index, "-",item_to_print.description, item_to_print.item_value)
            if item_to_print.item_type == "def_item":
                if not printing_def_items:
                    printing_def_items = True
                    print("\nDefense Items")
                print(index, "-",item_to_print.description, item_to_print.item_value)
                    
    
    def is_alive(self):
        if self.health_stat <= 0:
            return False
        else:
            return True
    
    def select_items(self):
        self.bag_items_print()
        user_command = str(input('\nTo equip an item input the id_number else input "Go" '))
        while user_command != 'Go':
            if not user_command.isnumeric():
                print('ERROR! The command should be a number or "Go"')
                user_command = str(input('\nTo equip an item input the id_number else input "Go" '))
                continue
            if int(user_command) >= len(self.bag_items) or int(user_command) < 1:
                print("ERROR! The id_number was not found")
                user_command = str(input('\nTo equip an item input the id_number else input "Go" '))
                continue
            
            self.equip_item(self.bag_items.pop(int(user_command)))
            self.player_print()
            self.bag_items_print()
            user_command = str(input('\nTo equip an item input the id_number else input "Go" '))
            
                
    
    def action_attack(self, enemy):
        if self.attack_stat - enemy.defense_stat > 0:
            enemy.health_stat -= self.attack_stat - enemy.defense_stat
        else:
            enemy.health_stat -= 1
            
    def monster_print(self):
        print("Name:", self.description)
        print("HP:  ", self.max_hp_stat)
        print("ATK: ", self.attack_stat)
        print("DEF: ",  self.defense_stat)
    
    def player_print(self):
        print("Name:  ", self.description)
        print("HP:    ", self.health_stat)
        print("ATK:   ", self.attack_stat)
        print("DEF:   ",  self.defense_stat)
        
    def buff_stats(self):
        print("Congratulations on winning the Battle")
        user_input = input("Select a stat to level up (atk/def): ")
        while user_input != "atk" and user_input != "def":
            print("Error! Not a valid option")
            user_input = input("Select a stat to level up (atk/def): ")
        if user_input == "atk":
            self.attack_stat += 10
        else:
            self.defense_stat += 10
        
        

