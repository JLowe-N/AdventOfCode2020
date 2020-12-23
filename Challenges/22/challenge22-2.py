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


example = parseInput('example.txt')
example2 = parseInput('example2.txt')
input = parseInput('input.txt')

def calcScore(winning_deck):
    print(winning_deck)
    print(len(winning_deck))
    winning_score = 0
    card_counter = 0
    while len(winning_deck) != 0:
        card_counter += 1
        winning_score += winning_deck.pop() * card_counter
    print(winning_score)




def playGame(p1_deck, p2_deck, recursion_lvl = 0):
    # Change to pass by value instead of ref
    # Avoid mutation
    # print(f'start nest level: {recursion_lvl}')
    p1_copy = p1_deck[:]
    p2_copy = p2_deck[:]

    sequence = None
    played_sequences = {}

    i = 0
    while len(p1_copy) > 0 and len(p2_copy) > 0:
        i+= 1
      
        # print(f'-- Round {i} (Game {recursion_lvl}) --')
        # print(f"Player 1's deck: {p1_copy}")
        # print(f"Player 2's deck: {p2_copy}")
        p1_str = ",".join([str(char) for char in p1_copy])
        p2_str = ",".join([str(char) for char in p2_copy])
        sequence = p1_str + '|' + p2_str
        
        if sequence in played_sequences:
            # print(f'Player 1 wins round {i} of game {recursion_lvl} - repeat sequence {sequence}')
            if recursion_lvl == 0:
                print("player 1 wins!")
                return p1_copy            
            else:
                return "winner: player1"
        played_sequences[sequence] = True
        
        p1_plays = p1_copy.pop(0)
        p2_plays = p2_copy.pop(0)
        # print(f"Player 1 plays: {p1_plays}")
        # print(f"Player 2 plays: {p2_plays}")
        
        if len(p2_copy) < p2_plays or len(p1_copy) < p1_plays:
            # print("Recursion can't happen")
            if p1_plays > p2_plays:
                # print(f"Player 1 wins {p1_plays} > {p2_plays}")
                p1_copy.append(p1_plays)
                p1_copy.append(p2_plays)
            elif p2_plays > p1_plays:
                # print(f"Player 2 wins {p1_plays} < {p2_plays}")
                p2_copy.append(p2_plays)
                p2_copy.append(p1_plays)
            else:
                print("oops!")
        else:
            # Recursive Battle!!!
            # print('Recursive Battle!')
            # print(f'-- Round {i} (Game {recursion_lvl}) --')
            # print(f"Player 1's deck: {p1_copy}")
            # print(f"Player 2's deck: {p2_copy}")
            # print(f"Player1 played {p1_plays}")
            # print(f"Player2 played {p2_plays}")
            # print(f"Entering sub-game with {p1_copy[0:p1_plays]} and {p2_copy[0:p2_plays]}")
            result = playGame(p1_copy[0:p1_plays], p2_copy[0:p2_plays], recursion_lvl + 1)
            if result == "winner: player1":
                p1_copy.append(p1_plays)
                p1_copy.append(p2_plays)
            elif result == "winner: player2":
                p2_copy.append(p2_plays)
                p2_copy.append(p1_plays)
            else:
                print("oops!")
    
    # Exit while loop - one deck must be empty
    if recursion_lvl > 0: # Sub-game
        # print(f'Sub-game {recursion_lvl} resolved')
        if len(p2_copy) == 0:
            return "winner: player1"
        elif len(p1_copy) == 0:
            return "winner: player2"
    elif recursion_lvl == 0:
        if len(p2_copy) == 0:
            print("Player 1 wins!")
            return p1_copy
        elif len(p1_copy) == 0:
            print("Player 2 wins!")
            return p2_copy
    else:
        print("oops")


winning_deck = playGame(*input)
calcScore(winning_deck)