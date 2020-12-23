def parseInput(filename):
    p1deck = []
    p2deck = []
    switch = False
    with open(filename) as file:
        linenum = 0
        for line in file:
            if line.startswith('Player'):
                continue

            if line.isspace():
                switch = True
                continue

            line.rstrip('\n')
            
            if switch:
                p2deck.append(int(line))
            else:
                p1deck.append(int(line))
            linenum += 1

    # treat like deque <<< deck top
    return (p1deck, p2deck)


# example = parseInput('example.txt')
input = parseInput('input.txt')

def calcScore(p1_deck, p2_deck):
    winning_deck = p1_deck if len(p1_deck) > len(p2_deck) else p2_deck

    winning_score = 0
    card_counter = 0
    while len(winning_deck) != 0:
        card_counter += 1
        winning_score += winning_deck.pop() * card_counter
    
    print(winning_score)

def playCards(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_plays = p1_deck.pop(0)
        p2_plays = p2_deck.pop(0)

        if p1_plays > p2_plays:
            p1_deck.append(p1_plays)
            p1_deck.append(p2_plays)
        elif p2_plays > p1_plays:
            p2_deck.append(p2_plays)
            p2_deck.append(p1_plays)
        else:
            print('Tie!')
    print(calcScore(p1_deck, p2_deck))
    
 


playCards(*input)