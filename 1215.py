f = open("input/1215.txt", "r")

TEST = ['rn=1', 'cm-', 'qp=3',  'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

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
        if inst[1] in j:
            box[i] = ""
            cp = box.copy()
            box = slide_lenses(cp)
        return box
            
        

def slide_lenses(box):
            
    for i, j in enumerate(box):
        if j == "":
            continue
        else:
            curr = i
            prev = curr - 1
            print("curr: ", curr, "prev: ", prev, box)
            while curr != 0 and box[prev] == "":
                box[prev] = j
                box[curr] = ""
                curr = curr - 1
                prev = curr - 1  
    return box


# TEST_BOX = ["", "rn=1", "acd", "", "abc", "", ""]

# print(handle_focal_length("rn=1", TEST_BOX))


def insert_lens(lens, inst, box):

    if all(i == "" for i in box):
        box[0] = lens
        return box
    
    else:
        for i, j in enumerate(box):
            if inst[1][0] in j:
                box[i] = lens
                cp = box.copy()
                box = slide_lenses(cp)
                
                return box
    
        box.append(lens)
        cp = box.copy()
        box = slide_lenses(cp)
        return box

def organize_lenses(input_list):

    boxes = [[""]] * 256
    print("origibal ", boxes)
    # i will be raw chars
    for i in input_list:

        if "=" in i:
            print("lens ", i)
            # box: label, focal length
            # (0, ('rn', 1))
            inst = focal_length(i)
            print("focal length ", inst)
            print(boxes[inst[0]])
            print(boxes)
            box_state = boxes[inst[0]].copy()
            boxes[inst[0]] = insert_lens(i, inst, box_state)

        # handle box shifting
        else:
            print("examing box id", i)
            # box: label
            # (1, 'qp')
            inst = get_box_id(i)
            box_state = boxes[inst[0]].copy()
            print("box id ", inst)
            boxes[inst[0]] = handle_focal_length(inst, box_state)

    return boxes

print(organize_lenses(TEST))


def power(box, slot, fl):






# if __name__ == '__main__':
    
#     print(total(to_input_list(f)))