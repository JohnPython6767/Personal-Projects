import random

player_position = {"Lat":0 , "Long":0}

biomes = {"Desert":10 , "Forrest":10 , "Mountains":10}

map = { 0:{"Lat":0 , "Long":0 , "Biome":"Desert"}

}

def output_player_position(map):
    for i in range(len(map)):
        if player_position["Lat"] == map[i]["Lat"] and player_position["Long"] == map[i]["Long"]:
            position = map[i]["Biome"]
            print(f"Player is in a {position}")

    return position


def check_position_exists(check , temp_player_position , map):
    for i in range(len(map)):
        if temp_player_position["Lat"] != map[i]["Lat"] and temp_player_position["Long"] != map[i]["Long"]:
            check = False
        elif temp_player_position["Lat"] == map[i]["Lat"] and temp_player_position["Long"] == map[i]["Long"]:
            check = True
        

    return check

def create_position(temp_player_position , player_position , map , position):
    print("Generating position")

    # Increase weight of current biome
    if position in biomes:
        biomes[position] += 10

    # Pick weighted random biome
    new_position_biome = random.choices(
        list(biomes.keys()),
        weights=list(biomes.values()),
        k=1
    )[0]

    # Reset weight back to normal
    if position in biomes:
        biomes[position] -= 10
    new_lat = temp_player_position["Lat"]
    new_long = temp_player_position["Long"]

    new_key = len(map)
    map[new_key] = {"Lat": new_lat, "Long": new_long, "Biome": new_position_biome}

    return temp_player_position , player_position , map


def player_move(player_position , map , position):
    check = 0
    print("Movement options (enter full word):")
    print("North")
    print("South")
    print("East")
    print("West")

    choice = input(">>")


    ##### North == positive lat     South == negative Lat   East == positive long   West == negative long
    if choice.lower() == "north":
        new_lat = player_position["Lat"] + 1
        new_long = player_position["Long"]
        

    if choice.lower() == "south":
        new_lat = player_position["Lat"] - 1
        new_long = player_position["Long"] 
        

    if choice.lower() == "east":
        new_lat = player_position["Lat"] 
        new_long = player_position["Long"] + 1
        

    if choice.lower() == "west":
        new_lat = player_position["Lat"] 
        new_long = player_position["Long"] - 1
        

    temp_player_position = {"Lat":new_lat , "Long":new_long}
    
    check = check_position_exists(check , temp_player_position , map)

    if check == True:
        player_position = temp_player_position
        print("Moved")
    else:
        
        temp_player_position , player_position , map = create_position(temp_player_position , player_position , map , position)
        player_position = temp_player_position
    
    return player_position , map

            

###
while True:
    position = output_player_position(map)
    player_position , map = player_move(player_position , map , position)
    input("")