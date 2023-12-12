TEST = [0, 3, 6, 9, 12, 15]

TEST2 = [1, 3, 6, 10, 15, 21]

TEST3 = [10, 13, 16, 21, 30, 45]


f = open("1209input.txt", "r")

test_input = open("1209testinput.txt", "r")

def cache_map(input):

    m = []
    for i in input:
        ints = []
        ni = i.split(" ")
        for s in ni:
            ints.append(int(s.strip()))
        m.append(ints)
    
    return m

def find_diff(num_list):
    new_list = []
    for i in range(len(num_list)-1):
        diff = num_list[i+1] - num_list[i]
        new_list.append(diff)
    return new_list

# print(find_diff(TEST))

def zero_lists(num_list, acc):

    print("considering  ", num_list, " ", acc)
    
    if all(i == 0 for i in num_list):
        return acc
    else:
        nl = find_diff(num_list)
        print("nl ", nl)
        na = acc + nl[len(nl)-1]
        print("na ", na)
        x = zero_lists(nl, na)
        print("returning na + acc ", na, " ", acc)
        return x


print(zero_lists(TEST2, 0))

def find_next_num(map):
    total = 0
    for i in map:
        print("WORKING ON: ", i)
        new_num = i[len(i) - 1] + zero_lists(i, 0)
        print("new nun ", new_num)

        total = total + new_num
    return total

# print(cache_map(f))
# print(find_next_num(cache_map(f)))

# print(find_next_num(cache_map(test_input)))



    
        
