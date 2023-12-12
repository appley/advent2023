SEEDS = [
    222541566, 218404460, 670428364, 432472902,
      2728902838, 12147727, 3962570697, 52031641, 2849288350,
    113747257, 3648852659, 73423293, 4036058422, 190602154, 
        1931540843, 584314999, 3344622241, 180428346, 1301166628, 310966761]


SEEDS_TEST = [79, 14, 55, 13]


soil = open("seed_to_soil.txt", "r")
fert = open("soil_to_fert.txt", "r")
water = open("fert_to_water.txt", "r")
light = open("water_to_light.txt", "r")
temp = open("light_to_temp.txt", "r")
hum = open("temp_to_hum.txt", "r")
loc = open("hum_to_loc.txt", "r")


soil_test = open("test_soil.txt", "r")


def unload_range(dest, source, length):
    
    source_range = [x for x in range(int(source), int(source) + int(length))]
    dest_range = [x for x in range(int(dest), int(dest) + int(length))]

    return (source_range, dest_range)
    

def convert_seed_to_next(map):

    converted = {}

    for line in map:
        l = line.rstrip("\n").split(" ")
        ranges = unload_range(l[0], l[1], l[2])

        for k, v in zip(ranges[0], ranges[1]):
            converted[k] = v

    print(converted)
    return converted


def convert_input(input_list, map):

    print("converting new list: ", input_list)

    converted_list = []
    next_values = convert_seed_to_next(map)
    
    for i in input_list:
        if i in next_values:
            converted_list.append(next_values[i])
        else:
            converted_list.append(i)

    # print(converted_list)
    return converted_list

x = convert_input(convert_input(convert_input(
    convert_input(convert_input(convert_input(convert_input(SEEDS, soil), fert), water), light), temp), hum), loc)

print(x)
print(min(x))


soil = open("seed_to_soil.txt", "r")
fert = open("soil_to_fert.txt", "r")
water = open("fert_to_water.txt", "r")
light = open("water_to_light.txt", "r")
temp = open("light_to_temp.txt", "r")
hum = open("temp_to_hum.txt", "r")
loc = open("hum_to_loc.txt", "r")
