input_one = open("input/1201.txt", "r")

NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


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