TEST_DIR = "LLR"
# TEST = open("1208testinput.txt", "r")

f = open("input/1208.txt", "r")

DIRS = "LRLRLRRLRRRLRRRLRRRLRLRRRLRRRLRRRLLRLRRRLRLRRRLLRRRLRRLRRRLRRLRLRRRLRRRLRLRRLRRRLRRLRRRLRRLRLRRLRRRLRLRRLRRRLLRRRLRLRRLLLRLLRLRRLLRRRLLRLLRRLRLRRRLLLRLRRLRLRRLRRRLRRLLRRLLRLRRRLRRRLRLLLLRLLRLRLRLRRRLRRLRRLRLRRRLLRRLRLLRRLRLRRLRLRLRRLRRLLRLRRLLRLLRRRLLLRRRLRRLRLRRRLRRLRRRLRRLLLRRRR"


def line_to_list(line):
    # return three element tuple
    # clean this code

    temp = line.split(" = ")
    lr = temp[1].strip("(").split(", ")
    r = lr[1].strip(")\n")

    return (temp[0], lr[0], r)


def create_map(input):

    map = {}

    for line in input:
        path = line_to_list(line)
        map[path[0]] = (path[1], path[2])

    return map


# cache start
def index_direction(dir, key, map):

    print(map)

    if dir == "L":
        return map[key][0]
    else:
        return map[key][1]


def go(direction_string, input):

    map = create_map(input)
    result = ""
    key = "AAA"
    count = 0
    # abstract string and pass as parameter
    # cache start
    while result != "ZZZ":

        for dir in direction_string:
            next = index_direction(dir, key, map)
            key = next
            result = next

            count = count + 1

    # print(key) 
    return count


if __name__ == "__main__":

    # part 1
    print(go(DIRS, f))