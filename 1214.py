f = open("input/1214.txt", "r")

t = open("input/1214test.txt", "r")

t2 = open("input/1214test2.txt", "r")

t3 = open("input/1214test3.txt", "r")


def create_map(f):

    m = []
    
    for line in f:
        l = []
        for i in line:
            l.append(i.strip())
        m.append(l)

    return m


# string map
# def create_map(f):

#     map = []
    
#     for line in f:
#         map.append(line.strip())

#     return map

# print(create_map(t))


def to_string(map):

    l = []

    for row in map:
        s = ""
        for i in row:
            s = s + i
        l.append(s)

    return l


def roll_rock(map, row, col):

    print("creating new map: ", row, col)
    print(".....incoming map.......")
    print(map)

    map[row+1][col] = "O"
    map[row][col] = "."

    print(".....returning map......")
    print(map)
    return map


def tilt(map):

    # cp = map.copy()
    # cp.reverse()

    # m = []

    for row, string in enumerate(map[0:len(map)-1]):
        print("level:", row)
        print(string)
        for col, element in enumerate(string):
            if element == "O":
                print("handling rock: row, col", row, col)
                if map[row+1][col] == ".":
                    cp = map.copy()
                    map = roll_rock(cp, row, col) 
                    # map[row+1][i] == "O"
                    # markers[i] = "."

    # for i in reversed(cp):
    #     m.append(i)

    # cp.reverse()
    return map



                
m = create_map(t)
# m.reverse()
# print(m)
x = tilt(m)
# print(x)
# x.reverse()
print(to_string(x))

