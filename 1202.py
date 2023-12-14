f = open("input/1202.txt", "r")

def load_dict(f):

    game_dict = {}
    
    for i in f:

        # split lines by id and list of games per id
        s = i.split(":")
        game_id = int(s[0].split("Game ")[1])
        games = s[1].strip().split("; ")

        # for each id create list of dicts for each game played
        game_list = []

        for game in games:
            colors = game.split(", ")
            color_dict = {}
            for color in colors:
                c = color.split(" ")
                color_dict[c[1]] = int(c[0])
            game_list.append(color_dict)
        
        game_dict[game_id] = game_list

    return game_dict


# part 1
####
# Cubes:
RED = 12
GREEN = 13
BLUE = 14

def is_valid_game(game):
    
    if game.setdefault("green", 0) <= GREEN and game.setdefault("red", 0) <= RED and game.setdefault("blue", 0) <= BLUE:
        return True
    else:
        return False


def total_valid_games(game_dict):

    total = 0

    for k, v in game_dict.items():
        if all(is_valid_game(i) for i in v): 
            total = total + k

    return total


# part 2
####

def power_set(game_list):

    total = 1
    
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
        }

    for game in game_list:

        if game.setdefault("red", 0) > maxes["red"]:
            maxes["red"] = game["red"]
        if game.setdefault("green", 0) > maxes["green"]:
            maxes["green"] = game["green"]
        if game.setdefault("blue", 0) > maxes["blue"]:
            maxes["blue"] = game["blue"]

    for k, v in maxes.items():
        total = total * v

    return total


def total_power_sets(game_dict):

    total = 0

    for k, v in game_dict.items():
        total = total + power_set(v)

    return total



if __name__ == "__main__":

    g = load_dict(f)

    print(total_valid_games(g))
    print(total_power_sets(g))






