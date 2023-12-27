
f = open("1204input.txt", "r")


def create_winners_and_mine(card):

    cards = card.split(":")[1].split("|")
    
    w = cards[0].strip().split(" ")
    m = cards[1].strip().split(" ")

    winners = [i for i in w if i != '']
    mine = [i for i in m if i != '']

    return (winners, mine)


def process_card(card):

    matches = 0
    
    for i in card[0]:
        if i in card[1]:
            matches = matches + 1

    if matches > 0:
        return 2**(matches-1)
    
    else:
        return matches

def process_all_cards(card_stack):

    total = 0

    for card in card_stack:

        card_total = process_card(create_winners_and_mine(card))
        
        total = total + card_total

    return total


print(process_all_cards(f))