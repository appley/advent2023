f = open("input/1214.txt", "r")

t = open("input/1214test.txt", "r")

t2 = open("input/1214test2.txt", "r")


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


# def tilt(map):

#     for row, markers in enumerate(map[0:len(map)-1]):
#         print("level:", row)
#         print(markers)
#         for i, j in enumerate(markers):
#             if j == "O":
#                 print("handling rock: row, col", row, i)
#                 count = 1 # check next row
#                 # roll rock
#                 # print("count + row ", count + row, len(map))
#                 while count + row < len(map) - 1 and map[row+count][i] == ".":
#                     print("checking row: ", row+count, "contents: ", map[row+count][i])
                    
#                     print ("adding rock to ", row + count, i)
#                     map[row+count][i] = "O"
#                     print("setting row, col to .", row, i)
#                     # markers[i] = "."
#                     map[row][i] = "."
#                     count = count + 1
#             else:
#                 print("skipping not rock: ", i, j)

#     return map



def roll_rock(map, row, index):

    print("orginal map: ", map)

    map[row+1][index] = "O"
    map[row][index] = "."
    print(map)
    return map
    

def tilt(map):

    for row, markers in enumerate(map[0:len(map)-1]):
        print("level:", row)
        print(markers)
        for i, j in enumerate(markers):
            if j == "O":
                print("handling rock: row, col", row, i)
                if map[row+1][i] == ".":
                    map = roll_rock(map, row, i) 
                    # map[row+1][i] == "O"
                    print("set map row : ", row + 1, map[row+1])
                    # markers[i] = "."
            else:
                print("skipping ", i, j)
    return map
    #             count = 1 # check next row
    #             # roll rock
    #             # print("count + row ", count + row, len(map))
    #             while count + row < len(map) - 1 and map[row+count][i] == ".":
    #                 print("checking row: ", row+count, "contents: ", map[row+count][i])
                    
    #                 print ("adding rock to ", row + count, i)
    #                 map[row+count][i] = "O"
    #                 print("setting row, col to .", row, i)
    #                 # markers[i] = "."
    #                 map[row][i] = "."
    #                 count = count + 1
    #         else:
    #             print("skipping not rock: ", i, j)

    # return map


# def tilt(map):

#     for row, markers in enumerate(map[0:len(map)-1]):
#         print("level:", row)
#         for i, j in enumerate(markers):
#             if j == "O":
                

                
m = create_map(t2)
# m.reverse()
# print(m)
x = tilt(m)
# print(x)
# x.reverse()
print(to_string(x))

