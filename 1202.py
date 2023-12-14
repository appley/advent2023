f = open("input/1202.txt", "r")

# Cubes:
RED = 12
GREEN = 13
BLUE = 14


def load_dict(f):

    game_dict = {}
    
    for i in f:

        # split lines by id and list of games per id
        s = i.split(":")
        game_id = s[0].split("Game ")[1]
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
        # print(game_id, game_dict[game_id])

    return game_dict


def is_valid_game(game_list):
    
    for g in game_list:
        if g["green"] <= GREEN and g["red"] <= RED and g["blue"] <= BLUE:
            continue
        else:
            return False

    return True


def total_valid_games(games_dict):

    total = 

    for k, v in game_dict:
        if is_valid_game(v):
            total = total + k

    return total


print(total_valid_games(load_dict(f)))





