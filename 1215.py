f = open("input/1215.txt", "r")


def to_input_list(f):

    l = []

    for i in f:
        l.append(i.strip().split(","))

    return [item for row in l for item in row]


# part 1
####
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
####
def get_box_id(chars):
    s = chars.split("-")[0]
    return (hash(s), s)


def focal_length(chars):
    s = chars.split("=")
    return (hash(s[0]), ((s[0]), int(s[1])))


def handle_focal_length(inst,  box):

    for i, j in enumerate(box):
        if inst[1] in j:
            box.remove(j)

    return box


def insert_lens(lens, inst, box):

    if len(box) == 0:
        box.append(lens)
        return box
    
    else:
        for i, j in enumerate(box):
            if inst[1][0] in j:
                box[i] = lens     
                return box
    
        box.append(lens)
        return box


def organize_lenses(input_list):

    boxes = [[]] * 256
    # i will be raw chars
    for i in input_list:

        if "=" in i:
            # box: label, focal length
            # (0, ('rn', 1))
            inst = focal_length(i)
            box_state = boxes[inst[0]].copy()
            boxes[inst[0]] = insert_lens(i, inst, box_state)

        else:
            # box: label
            # (1, 'qp')
            inst = get_box_id(i)
            print(inst, boxes[inst[0]])
            box_state = boxes[inst[0]].copy()
            boxes[inst[0]] = handle_focal_length(inst, box_state)

    return boxes


def total_power(boxes):

    total = 0

    for box_id, box in enumerate(boxes):
        for slot, lens in enumerate(box):
            power = (box_id + 1) * (slot + 1) * focal_length(lens)[1][1]
            total = total + power

    return total



if __name__ == '__main__':

    l = to_input_list(f)
    
    # part 1
    print(total(l))

    # part 2
    print(total_power(organize_lenses(l)))
