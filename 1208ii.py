import itertools

TEST_DIR = "LLR"

TEST = open("1208testinput.txt", "r")

f = open("1208input.txt", "r")


DIRS = "LRLRLRRLRRRLRRRLRRRLRLRRRLRRRLRRRLLRLRRRLRLRRRLLRRRLRRLRRRLRRLRLRRRLRRRLRLRRLRRRLRRLRRRLRRLRLRRLRRRLRLRRLRRRLLRRRLRLRRLLLRLLRLRRLLRRRLLRLLRRLRLRRRLLLRLRRLRLRRLRRRLRRLLRRLLRLRRRLRRRLRLLLLRLLRLRLRLRRRLRRLRRLRLRRRLLRRLRLLRRLRLRRLRLRLRRLRRLLRLRRLLRLLRRRLLLRRRLRRLRLRRRLRRLRRRLRRLLLRRRR"

# print(a[1].split(","))

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


def find_start_keys(map):

    starts = []
    
    for key in map:
        if key[len(key)-1] == "A":
            starts.append(key)
    
    return starts


def build_key_list(dir, key_list, map):

    new_keys = []

    if dir == "L":
        for key in key_list:
            new_keys.append(map[key][0])
    else:
        for key in key_list:
            new_keys.append(map[key][1])
    print(new_keys)

    return new_keys


# x = create_map(f)
# start_keys = ['LQA', 'SGA', 'AAA', 'BJA', 'SVA', 'GFA']


# def go(direction_string, input):

#     map = create_map(input)
#     key_list = find_start_keys(map)
#     count = 0
#     # abstract string and pass as parameter
#     # cache start

#     while all(r[len(r)-1] != "Z" for r in key_list):
#         print(key_list)

#         for dir in direction_string:
#             print(dir)
#             next = build_key_list(dir, key_list, map)
#             key_list = next

#             count = count + 1

#     print(key_list)
 
#     return count


def go(direction_string, input):

    map = create_map(input)
    key_list = find_start_keys(map)
    count = 0
    # abstract string and pass as parameter
    # cache start

    if all(r[len(r)-1] == "Z" for r in key_list):
        return count
    
    else:
        print(key_list)

        for dir in itertools.cycle(direction_string):
            print(dir)
            next = build_key_list(dir, key_list, map)
            key_list = next

            count = count + 1

    print(key_list)
 
    return count

# print(len(DIRS))
print(go(DIRS, f))


# a = create_map(TEST)

# print(a)

# result_list = ['AZG', 'ZZZ',]



# r = result_list[0]
# print(r[len(r)- 1] == "Z")

# print(all(r[len(r)-1] != "Z" for r in result_list))


# [print(r[len(r)- 1]) for r in result_list]