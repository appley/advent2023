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

# tr = parse_rule("a<2006:qkq")
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


def accepted_letter_combos(rule_tuple, curr):

    letter = rule_tuple[0][0]  # handle letter dest
    test = rule_tuple[0][1]
    num = rule_tuple[0][2]
    dest = rule_tuple[1]

    if test == ">":
        if dest == "R":
            if curr > num:
                return (letter, num - 1)
            return (letter, curr)     

        else:
            if curr < num:
                return (letter, 0)
            return (letter, curr - num - 1)
        
    if test == "<":        
        if dest == "R":      
            if curr < num:
                return (letter, 0)
            return (letter, curr - num - 1)     
        else:
            if curr > num:
                return (letter, num - 1)
            return (letter, curr)        


def read_workflow(workflow, part):
    print("workflow", workflow)

    rules = TEST_RULES[workflow]

    # rules = WORKFLOWS[workflow]

    combos = []

    for rule in rules:
        r = parse_rule(rule)
        print("working on rule", rule)
        dest = r[1]

        if r[0] == 0 and dest == "R":
            print("returning rejected")
            return combos

        elif r[0] == 0:
            combos.append((dest, part))
            continue

        elif dest == "R":
            letter = r[0][0]
            a = accepted_letter_combos(r, part[letter])
            new_part = part.copy()
            # check this formula
            new_part[a[0]] = a[1]
            part = new_part
            continue

        else:
            # append rule and continue w inverse of rule
            letter = r[0][0]
            orig_part = part.copy()
            
            a = accepted_letter_combos(r, part[letter])
            if a[1] == 0:
                continue
            else:
                part[a[0]] = a[1]
                combos.append((dest, part))
                
                # check this formula
                orig_part[a[0]] = orig_part[a[0]] - a[1]
                part = orig_part
                continue
    
    print("returning combos from workflow", workflow, combos)
    return combos





p = {
    "x": 4000,
    "m": 4000,
    "a": 4000,
    "s": 4000
        }

s = "in"


p2 = {'x': 4000, 'm': 1801, 'a': 4000, 's': 1418}


p3 =  {'x': 2584, 'm': 4000, 'a': 2006, 's': 1351}

p4 = {'x': 4000, 'm': 2090, 'a': 1994, 's': 1351}

p5 = {'x': 4000, 'm': 4000, 'a': 4000, 's': 2649}


# print(read_workflow("in", p))

# print(read_workflow("qqz", p5))

# part 1
####


def process_parts(part, start):

    parts = []

    print("CALL fn start ", start)
    print("PART", part)

    combos = read_workflow(start, part)
    print("starting combos :", combos)

    for combo in combos:
        print("combo", combo)

        # while (next != "A") and (next != "R"):

        # print("next rule", next)

        cp = combo

        if cp[0] == "A":
            print("APPENDING FROM call", cp, parts)
            parts.append(cp[1])
 
        else:
            s = cp[0]
            np = cp[1]
            new_parts = parts.copy()
            new_parts.append(process_parts(np, s))
            parts = new_parts

    print("parts", parts)
    return parts

print(process_parts(p, s))


# combo qkq ('A', {'x': 1416, 'm': 4000, 'a': 2006, 's': 1351})

ps = [{'x': 1415, 'm': 4000, 'a': 2005, 's': 1350}, {'x': 4000, 'm': 1909, 'a': 1995, 's': 1350}, {'x': 2439, 'm': 2091, 'a': 1995, 's': 814}, {'x': 4000, 'm': 961, 'a': 4000, 's': 2650}, {'x': 4000, 'm': 839, 'a': 1715, 's': 2650}]


def total(parts):

    total = 0

    for p in parts:
        combos = 1
        for _, v in p.items():
            combos = combos * v        
        total = total + combos

    return total

print(total(ps))




        
