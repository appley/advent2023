f = open("input/1203.txt", "r")

def create_map(f):

    m = []

    for line in f:
        l = []
        for i in line:
            l.append(i.strip())
        m.append(l)

    return m

print(create_map(f))
        

# for each num if num adjacent to num or symbol include
        