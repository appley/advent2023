f = open("input/1218.txt", "r")

t = open("input/1218test.txt", "r")

# parse input into instructions
# draw map
# fill in map
# count #


def get_instructions(f):

    l = []

    for line in f:
        s = line.strip().split(" ")
        t = (s[0], int(s[1]))
        l.append(t)

    return l

# print(get_instructions(f))

def dig_r(m, row, col, num):

    for i in range(num):

        m[row][i+col+1] = "#"

    return m


def dig_l(m, row, col, num):

    for i in range(num):
        m[row][col-i-1] = "#"

    return m


def dig_d(m, row, col, num):

    for i in range(num):

        m[i+row+1][col] = "#"

    return m


def dig_u(m, row, col, num):

    for i in range(num):
        m[row-i][col] = "#"

    return m


def dig(plan):

    m = [["." for _ in range(10000)] for _ in range(10000)]

    curr_row = 0
    curr_col = 0

    for p in plan:
        meters = p[1]
        print(p)
        print("turning ", p[0], "from ", curr_row, curr_col)
        if p[0] == "R":
            m = dig_r(m, curr_row, curr_col, meters)
            curr_col = curr_col + meters
            print("pos", curr_row, curr_col)
        if p[0] == "D":
            m = dig_d(m, curr_row, curr_col, meters)
            curr_row = curr_row + meters
            print("pos", curr_row, curr_col)

        if p[0] == "L":
            m = dig_l(m, curr_row, curr_col, meters)
            curr_col = curr_col - meters
            print("complete L new pos", curr_row, curr_col)
        
        if p[0] == "U":
            m = dig_u(m, curr_row-1, curr_col, meters)
            curr_row = curr_row - meters
            print("pos", curr_row, curr_col)       

    return m


def fill_row(row, start, stop):

    print(start, stop)

    for i in range(start, stop):
        row[i] = "#"

    return row


def fill(row):

    indices = []    

    for i, j in enumerate(row):

        print("considering ,", i, j)
        print("indices", indices)

        # if j == "#" and row[i+1] == ".":
        #     indices.append(i) # start index
        #     count = 1
        #     print(i + 1 + count)
        #     while row[i+count] == "." and i + count < len(row) - 1:
        #         count = count + 1
        #     indices.append(i+count)

        count = 1
        if j == "#":
            indices.append(i)
            if row[i+count] == ".":
                count = count + 1
                continue
    
    print(indices)
    if len(indices) != 0:

        for i, j in enumerate(indices[0:len(indices)-1]):

            if indices[i+1] - j != 1:
                cp = row.copy()
                row = fill_row(cp, j, indices[i+1])

    return row


r = ['.', '#', '.', '#', '.', '.', '.', '.', '#', '.']


row = ['.', '.', '#', '.', '.', '.', '#', '.']

# print(fill(row))


def fill_map(map):

    for row_num, row in enumerate(map):
        cp = row.copy()
        map[row_num]= fill(cp)

    print(map)

    return map


def total(map):

    total = 0

    for row in map:
        for element in row:
            if element == "#":
                total = total + 1
    
    return total



def to_string(map):

    l = []

    for row in map:
        s = ""
        for i in row:
            s = s + i
        l.append(s)

    return l

# print(total(dig(get_instructions(t))))


print(total(fill_map(dig(get_instructions(f)))))


            




