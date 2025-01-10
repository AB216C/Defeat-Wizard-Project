
print('''
---------------------------DEFEAT EVIL WIZARD----OOP------------------FNiyongira--------------------------------------
''')

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
       
    
class Mage(Character):
    def __init__(self, name):
         super().__init__(name, health=100, attack_power=35)

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

class Archer(Character):
     def __init__(self, name,special_ability=45 ):
        super().__init__(name, health=140, attack_power=10)
        self.special_ability = special_ability

     def special_tricks(self,opponent):
        opponent.health -= self.special_ability
        print(f"{self.name} attacks using special ability: {self.special_ability} damages")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

class Paladin(Character):
     def __init__(self, name):
        super().__init__(name, health=130, attack_power=10)
     def heal(self):
        self.health += 40
        print(f"{self.name} regenerates 40 health! Current health: {self.health}")

class The_Great(Character):
    def __init__(self, name,special_weapon=40 ):
        super().__init__(name, health=100, attack_power=5)
        self.special_weapon = special_weapon

    def special_force(self,opponent):
        opponent.health -= self.special_weapon
        print(f"{self.name} attacks using special weapon: {self.special_weapon} damages")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def heal(self):
        self.health += 30
        print(f"{self.name} regenerates 30 health! Current health: {self.health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    print("5. The_Great")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    elif class_choice == '5':
        return The_Great(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Special force")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_tricks(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.special_force(wizard)
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()

#The main function down below will execute all functions as defined from create charaater  to  battle(player,wizard) function and will continue to 
# be executed because of while loop untill either player or wizard is defeated.


