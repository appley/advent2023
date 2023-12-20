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

    # m = [["." for _ in range(500)] for _ in range(5000)]

    m = [["." for _ in range(10)] for _ in range(10)]

    curr_row = 0
    curr_col = 0


    # curr_row = 400
    # curr_col = 70

    count = 1
    for p in plan:
        meters = p[1]
        # print("count", count)
        print(p)
        # print("turning ", p[0], "from ", curr_row, curr_col)
        if p[0] == "R":
            m = dig_r(m, curr_row, curr_col, meters)
            curr_col = curr_col + meters
            # print("pos", curr_row, curr_col)
        if p[0] == "D":
            m = dig_d(m, curr_row, curr_col, meters)
            curr_row = curr_row + meters
            # print("pos", curr_row, curr_col)

        if p[0] == "L":
            m = dig_l(m, curr_row, curr_col, meters)
            curr_col = curr_col - meters
            # print("complete L new pos", curr_row, curr_col)
        
        if p[0] == "U":
            m = dig_u(m, curr_row-1, curr_col, meters)
            curr_row = curr_row - meters
            # print("pos", curr_row, curr_col)   
        count = count + 1    

    return m


def fill_row(row, start, stop):

    # print(start, stop)

    for i in range(start, stop):
        row[i] = "#"

    return row





def fill(row):

    print(row)

    indices = []

    start = 0
    stop = 0

    for i, j in enumerate(row):

        print("current start stop", (start, stop)) 
        print(i, j)

        count = 1
       
        # if i == stop:
        #     continue

        if j == "#" and start != -1:
            print("setting new start", i)
            start = i
        
        else:         

            while i + count < len(row) and row[i+count] != "#":
                
                count = count + 1
            
            # stop = count + i
            # indices.append((start, stop))
                # print("looking at #s", row[i:len(row)-1])


            if "#" in row[i+1:len(row)-1]:

                stop = i + count
                print("stopping ", stop)
                indices.append((start, stop))
                # fill(row[i+1:len(row)-1])

        
    print(indices)
    if len(indices) != 0:

        for t in indices:
            cp = row.copy()
            row = fill_row(cp, t[0], t[1])

    return row



r = ['.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '#', '.', '.']

x = ['#', '#', '.', '.', '#', '#', '#', '.', '.', '.']

print(fill(r))

def fill2(row):

    indices = []    

    for i, j in enumerate(row):

        # print("considering ,", i, j)
        # print("indices", indices)

        # if j == "#" and row[i+1] == ".":
        #     indices.append(i) # start index
        #     count = 1
        #     print(i + 1 + count)
        #     while row[i+count] == "." and i + count < len(row) - 1:
        #         count = count + 1
        #     indices.append(i+count)

        count = 1
        if j == "#": # and i + count < len(row) - 1:
            indices.append(i)
            if len(row) - 1 > i + count and row[i+count] == ".":
                count = count + 1
                continue
    
    print(indices)
    if len(indices) != 0:

        for i, j in enumerate(indices[0:len(indices)-1]):

            if indices[i+1] - j != 1:
                cp = row.copy()
                row = fill_row(cp, j, indices[i+1])

    return row






def fill_map(map):

    for row_num, row in enumerate(map):
        cp = row.copy()
        map[row_num]= fill(cp)

    # print(map)

    return map

def total(map):

    total = 0

    count = 1
    for row in map:
        print("row",  count)
        for element in row:
            if element == "#":
                total = total + 1
                print("curr total ", total)
        count = count + 1
    
    return total



def to_string(map):

    l = []

    for row in map:
        s = ""
        for i in row:
            s = s + i
        l.append(s)

    return l


def print_map(map):

    for row in map:
        print(row)

    return map



# filled_map = fill_map(dig(get_instructions(t)))
# m = total(filled_map)
# print(m)

# print_map(to_string(filled_map))

# m = to_string(fill_map(dig(get_instructions(t))))
# m = fill_map(dig(get_instructions(t)))
# print_map(m)



