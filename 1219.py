f = open("input/1219.txt", "r")

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
        d["s"] = int(l[2].strip("}\n").split("=")[1])

        rs.append(d)

    return rs


def parse_rule(rule):

    if (">" and "<") not in rule:
        return (0, rule)
    
    else:
        s = rule.split(":")
        test = (s[0][0], s[0][1], int(s[0][2:len(s[0])]))

    # return tuple with test and result: place to send widget
    return (test, s[1])


def execute_rule(rule_tuple, part):
    # rule_tuple : (test, destination)
    # returns rule's destination after test

    if not rule_tuple[0]:
        # return destination
        return rule_tuple[1]
    
    else:
        letter = rule_tuple[0][0]
        test = rule_tuple[0][1]
        num = rule_tuple[0][2]

        if test == ">":
            if part[letter] > num:
                return rule_tuple[1]
            
        elif test == "<":
            if part[letter] < num:
                return rule_tuple[1]
            
    return False

test_part = {'x': 787, 'm': 2655, 'a': 1222, 's': 1222}

tr = parse_rule("a<2006:qkq")

print(execute_rule(tr, test_part))



# print(parts(tp))







# print(rules(t))

        
