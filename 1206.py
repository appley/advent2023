# Time:        60     80     86     76
# Distance:   601   1163   1559   1300

# (race duration - time held) * time held m / s = distance

# 60 - 1 * 1 m / s = 59
# 60 - 2 * 2 m / s = 156

def calculate_num_wins(duration, winning_distance):

    total = 0

    for i in range (duration + 1):

        considered_dist = (duration - i) * i
        # print("considering: ", i,  considered_dist)
        if considered_dist > winning_distance:
            total = total + 1

    print(total)
    return total

# print(
#     calculate_num_wins(
#         60, 601) * calculate_num_wins(
#             80, 1163) * calculate_num_wins(
#                 86, 1558) * calculate_num_wins(76, 1300))
    

# part 2
calculate_num_wins(60808676, 601116315591300)

    