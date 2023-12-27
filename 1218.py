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

    m = [["." for _ in range(500)] for _ in range(5000)]

    # m = [["." for _ in range(10)] for _ in range(10)]

    # curr_row = 0
    # curr_col = 0

    curr_row = 400
    curr_col = 70

    count = 1
    for p in plan:
        meters = p[1]
        # print("count", count)
        # print(p)
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


def is_inbounds(coord, map):

    row = coord[0]
    col = coord[1]

    def left():
        if "#" in map[row][:col]:
            # print("in bounds r")
            return True
        
    def right():
        if "#" in map[row][col:len(map[row])]:
            return True
        
    def up():
        for r in map[:row]:
            if "#" in r[col]:
                return True
    
    def down():
        for r in map[row+1:]:
            if "#" in r[col]:
                return True
            
    
    if left() and right() and up() and down():
        return True
    
    else:
        return False
    


def fill(map):

    for row_num, row in enumerate(map):
        cp = row.copy()
    
        for col_num, col in enumerate(cp):

            if col == ".":
                coord = (row_num, col_num)
                if is_inbounds(coord, map):
                    cp[col_num]= "#"

        map[row_num] = cp


    return map

    

# def fill(row):

#     print(row)

#     indices = []

#     start = 0
#     stop = 0
#     last = ("","")

#     for i, j in enumerate(row):

#         print("current start stop", (start, stop)) 
        

#         count = 1
#         print(i, j, count)
       

#         if j == "#":
#             print("setting new start", i)
#             start = i + 1

#             if i == last[1]:

#                 print("skipping index ", i)
#                 continue

#             else:

#                 while i + count < len(row) and row[i+count] != "#":
                    
#                     count = count + 1

#                     print("curr stop", stop, count)
                
#                 # stop = count + i
                    
#                 # indices.append((start, stop))
#                     # print("looking at #s", row[i:len(row)-1])


#                 if "#" in row[i+1:len(row)]:

#                     stop = i + count
#                     print("setting stop ", stop)
#                     last = (start, stop)
#                     indices.append(last)
 
        
#     print(indices)
#     if len(indices) != 0:

#         for t in indices:
#             cp = row.copy()
#             row = fill_row(cp, t[0], t[1])

#     return row



r = ['.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '#', '.', '.']

x = ['#', '#', '.', '.', '#', '#', '#', '.', '.', '.']


y = ['#', '#', '.', '.', '#', '#', '#', '.', '.', '.']


# print(fill(y))



# def fill_map(map):

#     for row_num, row in enumerate(map):
#         cp = row.copy()
#         map[row_num]= fill(cp)

#     # print(map)

#     return map

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



# filled_map = fill_map(dig(get_instructions(f)))
# m = total(filled_map)
# print(m)

# print_map(to_string(filled_map))

# m = to_string(fill_map(dig(get_instructions(t))))
# m = fill_map(dig(get_instructions(t)))
# print_map(m)


m = fill(dig(get_instructions(f)))
print_map(to_string(m))

# print(total(m))



