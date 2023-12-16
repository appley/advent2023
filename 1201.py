input_one = open("1201input.txt", "r")

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


def calibrate_line(line):
    first = ""
    last = ""

    for i in line:
        if i in NUMS and first == "":
            first = i
            last = i
        elif i in NUMS:
            last = i

    return int(first + last)


def total(file):

    total = 0

    for i in file:
        total = total + calibrate_line(i)
    
    return total


if __name__ == "__main__":

    print(total(input_one))

