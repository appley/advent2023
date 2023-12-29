f = open("input/1219.txt", "r")

p = open("input/1219p.txt", "r")

t = open("input/1219test.txt", "r")

tp = open("input/1219testparts.txt", "r")


def rules(f):

    d = {}

    for line in f:

        l = line.split("{")
        
        inst = l[1].strip("}\n").split(",")

        rs = []

        for i in inst:
            rs.append(i)

        d[l[0]] = rs

    return d


def parts(f):

    rs = []

    for line in f:

        l = line.split(",")
        d = {}
        # d[l[0].strip("{").split("=")[0]] = int(l[0].strip("{").split("=")[1])

        d["x"] = int(l[0].split("=")[1])
        d["m"] = int(l[1].split("=")[1])
        d["a"] = int(l[2].split("=")[1])
        d["s"] = int(l[3].strip("}\n").split("=")[1])

        rs.append(d)

    return rs


TEST_PARTS = (parts(tp))
TEST_RULES = (rules(t))

WORKFLOWS = rules(f)

PARTS = parts(p)


def parse_rule(rule):

    if (">" not in rule) and ("<" not in rule):
        return (0, rule)
    
    else:
        s = rule.split(":")
        test = (s[0][0], s[0][1], int(s[0][2:len(s[0])]))

    # return tuple with test and result: place to send widget
    return (test, s[1])


# def execute_rule(rule_tuple, part):
#     # rule_tuple : (test, destination)
#     # returns rule's destination after test

#     if not rule_tuple[0]:
#         # return destination
#         return rule_tuple[1]
    
#     else:
#         letter = rule_tuple[0][0]
#         test = rule_tuple[0][1]
#         num = rule_tuple[0][2]

#         if test == ">":
#             if part[letter] > num:
#                 return rule_tuple[1]
            
#         elif test == "<":
#             if part[letter] < num:
#                 return rule_tuple[1]
            
#     return False

test_p = {'x': 787, 'm': 2655, 'a': 1222, 's': 1222}

tr = parse_rule("a<2006:qkq")
# print(tr)
# print(execute_rule(tr, test_part))


def test_part(part, rule_tuple):
    # rule_tuple : (test, destination)
    # returns rule's destination after test

    letter = rule_tuple[0][0]
    test = rule_tuple[0][1]
    num = rule_tuple[0][2]

    if test == ">":
        if part[letter] > num:
            return True
        
    elif test == "<":
        if part[letter] < num:
            return True

    return False



def read_workflow(workflow, part):

    # rules = TEST_RULES[workflow]
    print("workflow ", workflow)

    rules = WORKFLOWS[workflow]
    
    for rule in rules:
        r = parse_rule(rule)
        # print(part)
        # print("r", r)

        if r[0] == 0:
            return r[1]
            # return final rule

        else:
            result = test_part(part, r)
            
            if result is True:
                print("test passes moving to next key", r[1])
                return r[1]
            else:
                continue
    
    return r[1]


# part 1
####

def process_parts(parts):

    accepted = []

    start = "in"

    for part in parts:
        print("considering part", part)

        next = read_workflow(start, part)
        # print("starting next with :", next)

        while (next != "A") and (next != "R"):
            next = read_workflow(next, part)
            # print("next rule", next)
      
        if next == "A":
            accepted.append(part)
        
    return accepted


def total(parts):

    total = 0

    for p in parts:
        pt = 0
        for _, v in p.items():
            pt = pt + v
        total = total + pt

    return total



# part 2
####


TOTAL_COMBOS = 4000**4


def accepted_letter_combos(rule_tuple):

    min = 1
    max = 4000

    letter = rule_tuple[0][0]  # handle letter dest
    test = rule_tuple[0][1]
    num = rule_tuple[0][2]
    dest = rule_tuple[1]


    if test == ">":
        if dest == "A":
            return (letter, max - num + 1)
        elif dest == "R":
            return (letter, num - min + 1)
        
    if test == "<":
        if dest == "A":
            return (letter, num - min + 1)        
        elif dest == "R":            
            return (letter, max - num + 1)


def accepted_workflow_combos(workflow):

    part = {
        "x": 4000,
        "m": 4000,
        "a": 4000,
        "s": 4000
    }

    for rule in workflow:
        print(rule)

        total = 0

        if rule == "R":
            return total
        
        elif rule == "A":
            return part["x"] * part["m"] * part["a"] * part["s"]

        else:
            r = parse_rule(rule)
            a = accepted_letter_combos(r)
            print(a)
            part[a[0]] = a[1]

        print(part)

    return part["x"] * part["m"] * part["a"] * part["s"]

c = ['m<1130:R', 'm>1525:A',]

ci = ['m<1130:R', 'm>1525:abc', 'R']

# x*calc inverse of m*a*s, x*calcm**a*s, return part total

print(accepted_workflow_combos(c))


def read_workflow2(workflow):

    rules = TEST_RULES[workflow]
    print("workflow ", workflow)

    # rules = WORKFLOWS[workflow]
    
    for rule in rules:
        r = parse_rule(rule)
        # print(part)
        # print("r", r)

        if r[0] == 0:
            return r[1]
            # return final rule

        else:
            result = test_part(part, r)
            
            if result is True:
                print("test passes moving to next key", r[1])
                return r[1]
            else:
                continue
    
    return r[1]


def total_accepted_combos(workflows):

    total = 1
    start = "in"
    
    combos = read_workflow2(start)







    







# part 1
# print(total(process_parts(PARTS)))

# print(process_parts(TEST_PARTS))




        
