f = open("input/1215.txt", "r")

TEST = ['rn=1' , 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

# part 1
def to_input_list(f):

    l = []

    for i in f:
        l.append(i.strip().split(","))

    return [item for row in l for item in row]


def hash(chars):

    curr = 0

    for i in chars:
        curr = ((curr + ord(i)) * 17) % 256

    return curr


def total(input_list):

    total = 0

    for i in input_list:
        total = total + hash(i)

    return total


# part 2

def get_box(chars):

    s = chars.split("-")[0]

    return (hash(s), s)


def focal_length(chars):

    s = chars.split("=")

    return (hash(s[0]), ((s[0]), int(s[1])))


# print(get_box('qp-'))

# print(focal_length('rn=1'))

def insert_focal_lens(lens, box):

    if all(i == 0 for i in box):
        box.insert(0, lens)
        return box
    else:
        for i, j in enumerate(box):
            if j == 0:
                continue
            else:
                box.insert(i, lens)
                return box
            

# def insert_dash_lens(box, lens):

#     if lens[1] in box[(lens[0])]:
#         box[lens[0]] = 0
#         for i, j in enumerate(box):
#             if box(i+1) == 0:
#             else:
#                 box[i+1] = j
#             else:
#                 return box
#     else:
#         return box
    

def slide_lenses(box):

    box.reverse()
    for i, j in enumerate(box):
        if j == 0:
            continue
        else:
            curr = i
            prev = curr - 1

            while curr > 0 and box[prev] == 0:
                box[prev] = j
                box[curr] = 0
                curr = curr - 1
                prev = curr - 1
    
    box.reverse()
    return box

TEST_BOX = [0, "rn=1", 0, 0, "abc", 0, 0]

print(slide_lenses(TEST_BOX))


def insert_lens(lens, box):

    if all(i == 0 for i in box):
        box[0] = lens
    else:
        for i, j in enumerate(box):
            while j == 0:
                continue


        

def organize_lenses(input_list):

    boxes = [0] * 256
    # i will be raw chars
    for i in input_list:

        if "=" in i:
            # box: label, focal length
            # (0, ('rn', 1))
            inst = focal_length(i)
            if inst[1][1] in boxes[inst[0]]:
                boxes[inst[0]] = i
            else:
                boxes = insert_lens(i)

        # handle box shifting
        else:
            # box: label
            # (1, 'qp')
            inst = get_box(i)
            if inst[1] in boxes[i]:
                boxes[i] = 0
                boxes = slide_lenses(boxes)

    return boxes

# print(organize_lenses("abc"))



# if __name__ == '__main__':
    
#     print(total(to_input_list(f)))