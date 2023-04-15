class Gear:
    def __init__(self, input_attack, input_defense, input_description):
        self.attack_modifier = input_attack
        self.defense_modifier = input_defense
        self.description = input_description + "equipped."

no_gear = Gear(0, 0, "No gear")        

class Warrior:
    def __init__(self, input_hp, input_attack, input_defense, input_description):
        self.max_hp_stat = input_hp
        self.attack_stat = input_attack
        self.defense_stat = input_defense
        self.health_stat = self.max_hp_stat
        self.equipped_gear = no_gear
        self.description = input_description
    
    def is_alive(self):
        if self.health_stat <= 0:
            return False
        else:
            return True
    
    def action_attack(self, enemy):
        enemy.health_stat -= self.attack_stat - enemy.defense_stat 
        
        

class Item:
    def __init__(self, input_type, input_value, input_description):
        self.item_type = input_type
        self.item_value = input_value
        self.description = input_description