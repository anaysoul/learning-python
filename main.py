###### Scope #################################################################
enemies = 1 

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

# global scope 
player_health = 100

def game():
    def drink_potion():
        potion_strength = 21
        print(player_health)
    drink_potion()

print(player_health)