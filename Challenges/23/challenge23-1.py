import collections

def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data.append(line)
            linenum += 1
    return data


example = [3,8,9,1,2,5,4,6,7]
input = [3,2,7,4,6,5,1,8,9]



def crabcups(cw_cups):
    maxval = max(cw_cups)
    cups = collections.deque(cw_cups)

    for i in range(100):
        print(cups)
        curcup_val = cups[0]
        print(curcup_val)
        picked_up = []
        cups.rotate(-1)
        for _ in range(3):
            # print(cups)
            picked_up.append(cups.popleft())
        nextcup_val = curcup_val - 1
        while nextcup_val <= 0 or nextcup_val in picked_up:
            nextcup_val = nextcup_val - 1
            if nextcup_val <= 0:
                nextcup_val = maxval
        while cups[0] != nextcup_val:
            cups.rotate(-1)
        cups.rotate(-1) # 1 past destination cup\
        for _ in range(3):
            cups.appendleft(picked_up.pop())
        while cups[0] != curcup_val:
            cups.rotate(-1)
        cups.rotate(-1) #1 past this current cup to set up nextcup
    print(cups)




    
    # for i in range(100):
    #     print(i)
    #     print(cw_cups)
    #     maxval = max(cw_cups)
    #     nextcup_idx = None
    #     nextcup_val = None
    #     picked_up = []
    #     for _ in range(3):
    #         picked_up.append(cw_cups.pop(curcup_idx + 1 if curcup_idx + 1 < len(cw_cups) - 1 else 0))
    #     nextcup_val = curcup_val - 1
    #     while nextcup_val in picked_up or nextcup_val < 0:
    #         nextcup_val = nextcup_val - 1
    #         if nextcup_val < 0:
    #             nextcup_val = maxval
    #     #     print(f'final {nextcup_val}')
    #     # print(nextcup_val)
    #     nextcup_idx = cw_cups.index(nextcup_val)
    #     for _ in range(3):
    #         cw_cups.insert(nextcup_idx + 1, picked_up.pop())
    #     curcup_idx += 1
    #     curcup_val = cw_cups[curcup_idx]

        
            
        


        
        


print(crabcups(input))