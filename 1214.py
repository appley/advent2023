f = open("input/1214.txt", "r")

t = open("input/1214test.txt", "r")

def create_map(f):

    map = []
    
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
        for i in s:
            s = s + 
        l.append(s)

    return l


def tilt_north(map):

    # count = 0

    for row, markers in enumerate(map[0:len(map)-1]):
        print("level:", row)
        for i, j in enumerate(markers):
            if j == "O":
                # roll rock
                if map[row+1][i] == ".":
                    map[row+1][i] = "O"
                    markers[i] = "."
        # count = count + 1

    return map

                
m = create_map(t)
print(tilt_north(m))

