f = open("1201iiinput.txt", "r")

NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

STRING_NUMS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }


def create_string_slices(s):

    slices = []
    start_pos = 0

    while start_pos < len(s):

        considered_string = s[start_pos:len(s)]

        for i, _ in enumerate(considered_string):
            new_string = considered_string[0:i+1]
            slices.append(new_string)
        
        start_pos = start_pos + 1
        
    return slices


def check_line_for_word(line, word):

    new_word = ""

    for i in line:
        new_word = new_word + i
        if new_word != word:
            continue
        else:    
            return new_word


def create_line_num(slices_list, nums, num_dict):

    first = ""
    last = ""
    start_pos = 0

    for i in slices_list:

        if i in nums and first == "":
            first = i
            last = i
        
        elif i in nums:
            last = i

        else:
            for k in num_dict:
                new_word = check_line_for_word(i, k)
                if new_word: 
                    word_num = num_dict[new_word]
                    if first == "":
                        first = word_num
                    last = word_num

    return int(first + last)


def total_nums(f, nums, num_dict):

    total = 0

    for line in f:
        slices = create_string_slices(line)
        total = total + create_line_num(slices, nums, num_dict)

    return total


print(total_nums(f, NUMS, STRING_NUMS))