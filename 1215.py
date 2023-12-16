f = open("input/1215.txt", "r")

TEST = ['rn=1'] # , 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

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

def get_box_id(chars):

    s = chars.split("-")[0]

    return (hash(s), s)


def focal_length(chars):

    s = chars.split("=")

    return (hash(s[0]), ((s[0]), int(s[1])))


def handle_focal_length(inst,  box):

    for i, j in enumerate(box):
        print("hi", inst[1], j)
        if inst[1] in j[1]:
            box[i] = ""
            cp = box.copy()
            box = slide_lenses(cp)
        return box
            
        

>>>>>>> Stashed changes
def slide_lenses(box):

    box.reverse()
    for i, j in enumerate(box):
        if j == "":
            continue
        else:
            curr = i
            prev = curr - 1

            while curr > 0 and box[prev] == "":
                box[prev] = j
                box[curr] = ""
                curr = curr - 1
                prev = curr - 1
    
    box.reverse()
    return box

TEST_BOX = [0, "rn=1", 0, 0, "abc", 0, 0]


def insert_lens(lens, box):

<<<<<<< Updated upstream
    if all(i == 0 for i in box):
        box[0] = lens
=======
    if all(i == "" for i in box):
        box[0] = inst
>>>>>>> Stashed changes
        return box
    else:
        for i, j in enumerate(box):
<<<<<<< Updated upstream
            print("examining index ", i, j)
            if j == 0:
                continue
            else:
                box[i-1] = lens
                return box

=======
            if inst[1][0] in j[1][0]:
                box[i] = inst
                cp = box.copy()
                box = slide_lenses(cp)
                
                return box
    
        box.append(inst)
        cp = box.copy()
        box = slide_lenses(cp)
        return box
>>>>>>> Stashed changes

def organize_lenses(input_list):

    boxes = [""] * 256
    # i will be raw chars
    for i in input_list:

        if "=" in i:
            # box: label, focal length
            # (0, ('rn', 1))
            inst = focal_length(i)
            if inst[1][0] in boxes[inst[0]]:
                boxes[inst[0]] = i
            else:
                boxes = insert_lens(i, boxes)

        # handle box shifting
        else:
            # box: label
            # (1, 'qp')
            inst = get_box_id(i)
            if inst[1] in boxes[inst[0]]:
                boxes[inst[0]] = ""
                boxes = slide_lenses(boxes)

    return boxes

print(organize_lenses(TEST))


<<<<<<< Updated upstream
=======
# def power(box, slot, fl)





>>>>>>> Stashed changes

# if __name__ == '__main__':
    
#     print(total(to_input_list(f)))