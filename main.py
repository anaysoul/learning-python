# ###### Scope #################################################################
# enemies = 1 

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# # print(potion_strength)

# # global scope 
# player_health = 100

# def game():
#     def drink_potion():
#         potion_strength = 21
#         print(player_health)
#     drink_potion()

# print(player_health)

# # if 3 > 2:
# #     a_variable = 10

# # There is no block scope for python
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

enemies = 1 
# avoid modifiying global scope
def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"Enemies outside function: {enemies}")

#global constants define and not change again

PI = 3.14159
URL = "http://www.python.org"


