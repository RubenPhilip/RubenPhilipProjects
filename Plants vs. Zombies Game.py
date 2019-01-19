import time # import time to add delay between print statements

class Plant: # create a class for plants with five different attributes 
    def __init__(self, name, description, health, attack, attack_speed):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed

def plant_stats(plant): # create a function to display the plant stats after the user chooses a specific plant
    """ Display the plant stats after the user chooses a specific plant """
    # Gives stats on the zombie using the class objects 
    print(plant.name, "Stats")
    time.sleep(2)
    print("Name =", plant.name)
    time.sleep(2) 
    print("Description", "=", plant.description)
    time.sleep(2) 
    print("Health", "=", plant.health)
    time.sleep(2) 
    print("Attack", "=", plant.attack)
    time.sleep(2) 
    print("Attack Speed", "=", plant.attack_speed)
    time.sleep(2)
 
# displays five different objects that belongs to the plant class attributes 
Peashooter = Plant("Peashooter", "Shoots peas at attacking zombies", 150, 60, "Medium")
SnowPea = Plant("SnowPea", "Shoot frozen peas that damage and slows the enemy", 250, 70, "Medium")
Chomper = Plant("Chomper", "Bites the zombie until it dies", 300, 90, "Slow")
GatlingPea = Plant("GatlingPea", "Shoot four peas at a time", 400, 120, "Super Fast")
Melonpult = Plant("Melon-pult", "Launches watermelons at the enemy", 450, 110, "Fast")

    

class Zombie: # create a class for zombies with five different attributes
    def __init__(self, name, description, health, attack, toughness):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.toughness = toughness

def zombie_stats(zombie): # create a function to display the zombie stats after the user chooses a specific zombie
    """ Display the plant stats after the user chooses a specific plant """
    print("")
    # Gives stats on the zombie using the class objects 
    print(zombie.name, "Stats")
    time.sleep(2)
    print("Name", "=", zombie.name)
    time.sleep(2)
    print("Description", "=", zombie.description)
    time.sleep(2)
    print("Health", "=", zombie.health)
    time.sleep(2)
    print("Attack", "=", zombie.attack)
    time.sleep(2)
    print("Toughness", "=", zombie.toughness)
    time.sleep(2)
    print("")
 
# displays five different objects that belongs to the zombie class attributes 
RegularZombie = Zombie("RegularZombie", "A normal zombie", 180, 60, "Low") 
BucketheadZombie = Zombie("BucketheadZombie", "Wears bucket that is resistant to damage", 350, 70, "High")
FootballZombie = Zombie("FootballZombie", "Fast moving zombie that has a lot of protection", 400, 80, "High")
PogoZombie = Zombie("PogoZombie", "Makes jumps on plants with his pogo stick", 300, 90, "High")
DoctorZomboss = Zombie("DoctorZomboss", "Simply Indestructible", 500, 150, "Extreme")


# introduction to game 
print("Welcome to Plants vs. Zombies")
time.sleep(2) # delay the print statements by 2 seconds  
# Displays list of characters in the game 
print("List of Plants:", "1.",Peashooter.name, "/", "2.", SnowPea.name, "/", "3.",Chomper.name, "/", "4.",GatlingPea.name, "/", "5.",Melonpult.name)
print("List of Zombies:", "1.", RegularZombie.name, "/", "2.", BucketheadZombie.name, "/", "3.", FootballZombie.name, "/", "4.",PogoZombie.name, "/", "5.",DoctorZomboss.name)
time.sleep(5)
print("")

def fight(plant, zombie): # create function for fight 
    '''Displays the actions that occurs during the battle. Provides information on the damage of the attack and health of the
plant or zombie that was attacked. Once the health of the zombie or plant is 0, the opposing character will win.'''
    zombie_health = zombie.health # set the original health for zombie 
    plant_health = plant.health # set the original health for plant
    while True: # loop to determine the health of the plant and zombie after each attack
        print("Plant attacks zombie.", plant.name, "does", plant.attack,"damage to", zombie.name) # calls upon the classes to display the damage from the plant to zombie
        zombie_health = zombie_health-plant.attack # displays the current health of the zombie after the damage 
        if zombie_health <= 0: # set the zombie health to 0 if the zombie has no health (doesn't display a negative number)
            zombie_health = 0
        print(zombie.name, "has", zombie_health, "health") # Prints out the health of the zombie after the damage from the plant
        time.sleep(5)
        if zombie_health == 0: # If the zombie's health is 0 then the plant wins 
            print (plant.name, "WINS!")
            break # ends loop

        print("Zombie attacks plant.", zombie.name, "does", zombie.attack,"damage to", plant.name) # calls upon the classes to display the damage from the zombie to plant
        plant_health = plant_health-zombie.attack # displays the current health of the plant after the damage 
        if plant_health <= 0: # set the plant health to 0 if the plant has no health (doesn't display a negative number)
            plant_health = 0
        print(plant.name, "has", plant_health, "health") # Prints out the health of the plant after the damage from the zombie 
        time.sleep(5)
        if plant_health == 0:
            print (zombie.name, "WINS!") # If the plant's health is 0 then the zombie wins
            leave()
            break # ends loop

# States the fight and gives stats on the plant using the class objects
def preparation(plant, zombie):
    """ Prints out stats for the fighters"""
    print("Fight:", plant.name, "vs.", zombie.name)
    print("")
    time.sleep(2) 
    plant_stats(plant)
    zombie_stats(zombie)

    # To begin the fight 
    print("Fight begins in....")
    time.sleep(2)
    print("3")
    time.sleep(2)
    print("2")
    time.sleep(2)
    print("1")
    time.sleep(2)
    print("FIGHT")
    print("")
    fight(plant, zombie)
    
def choose_char():
    """User chooses the plant and zombie to battle"""
    plant_list = [Peashooter, SnowPea, Chomper, GatlingPea, Melonpult] # create a list of plants
    num = input("Please only enter the number that corresponds to the plant you want to battle (example: input 3 for plant chomper): ") # user inputs a number that is corresponding to the plant they want to battle
    if num == "1" or num == "2" or num == "3" or num == "4" or num == "5":
        num = int(num) # change num from str to int 
        plant = plant_list[num-1] # the plant chosen by the user will be stored as variable plant
    else:
        print ("Invalid input. Try again.")
        choose_char()
        
    zombie_list = [RegularZombie, BucketheadZombie, FootballZombie, PogoZombie, DoctorZomboss] # create a list of zombies
    num = input("Please only enter the number that corresponds to the zombie you want to battle (example: input 3 for Football Zombie): ")
    # user inputs a number that is corresponding to the zombie they want to battle
    if num == "1" or num == "2" or num == "3" or num == "4" or num == "5":
        num = int(num)# change num from str to int
        zombie = zombie_list[num-1] # the zombie chosen by the user will be stored as variable zombie
        preparation (plant, zombie)
    else:
        print ("Invalid input. Try again")
        choose_char()
    print("")

def leave():
    print("Good Bye!")
    
def repeater(): # function so it only works once 
    x = True
    while x: 
        if "o" == "o": 
            choose_char()
            x = False
repeater()

