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

# for printing delete after 
def to_string(map):

    l = []

    for row in map:
        s = ""
        for i in row:
            s = s + i
        l.append(s)

    return l


# part 1
####
def roll_rock_south(map, row, col):

    map[row+1][col] = "O"
    map[row][col] = "."

    return map


def tilt_south(map):

    for row, string in enumerate(map[0:len(map)-1]):

        for col, element in enumerate(string):
            if element == "O":
                if map[row+1][col] == ".":
                    cp = map.copy()
                    map = roll_rock_south(cp, row, col)
    
    return map


def is_tilted(map):

    for row, string in enumerate(map[0:len(map)-1]):

        for col, element in enumerate(string):
            if element == "O" and map[row+1][col] == ".":
                return False
    return True


def tilt_all_south(map):

    while is_tilted(map) != True:
        map = tilt_south(map)

    return map

def tilt_all_north(map):

    map.reverse()
    new_map = tilt_all_south(map)
    new_map.reverse()
    return new_map


def total_weight(map):

    total = 0

    for row, string in enumerate(map):
        for element in string:
            if element == "O":
                l = len(map) - row
                total = total + l

    return total


# part 2
####

# refactor into part 1 code
def roll_rock_east(row, col):

    row[col] = "."
    row[col+1] = "O"

    return row



def tilt_east_row(row):

    count = 0

    while count < len(row) - 1:

        for i, j in enumerate(row[0:len(row)-1]):
            if j == "O" and row[i+1] == ".":
                cp = row.copy()
                row = roll_rock_east(cp, i)

        count = count + 1
    
    return row


def tilt_all_east(map):

    new_map = []

    for row in map:
        cp = row.copy()
        new_row = tilt_east_row(cp)
        new_map.append(new_row)
    
    return new_map


def tilt_all_west(map):

    m = []
    for row in map:
        rev = row.copy()
        rev.reverse()
        tw = tilt_east_row(rev)
        tw.reverse()
        m.append(tw)

    return m


def to_list(s):

    l = []

    for i in s:
        l.append(i)

    return l


# generalize this
def tilt_in_cycle(map):

    nm = map.copy()

    map = tilt_all_east(tilt_all_south(tilt_all_west(tilt_all_north(nm))))

    return map



def tilt_cycles(map, num_cycles):

    for cycle in range(num_cycles):
        print("cycle ", cycle)
        cp = map.copy()
        map = tilt_in_cycle(cp)
    
    return map



if __name__ == '__main__':


    m = create_map(f)

    # part 1             
    print(total_weight(tilt_all_north(m)))

    # part 2
    print(total_weight(tilt_cycles(m, 1000)))



