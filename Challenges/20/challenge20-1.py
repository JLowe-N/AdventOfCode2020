from pprint import pprint
import numpy as np

def parseInput(filename):
    tiles = {}
    borders = {}
    tiles_with_match = {}
    with open(filename) as file:
        linenum = 0
        tile = []
        tile_id = None
        for line in file:   
            line = line.strip('\n') 
            if line.startswith('Tile'):
                tile_id = line.lstrip('Tile ').rstrip(':')
                tiles_with_match[tile_id] = []
            elif line == '' or line == 'x':
                tile = np.array(tile)
                tile_dict = {
                    'tile': tile,
                    'top_row': "".join(tile[0, :]),
                    'bottom_row': "".join(tile[-1, :]),
                    'left_col': "".join(tile[:, 0]),
                    'right_col': "".join(tile[:, -1]),
                    'orientation': 'up'
                    }
                tile_dict['tile'] = tile[1:-1, 1:-1]
                tiles[tile_id] = tile_dict
                for key, border_str in tiles[tile_id].items():
                    if key == 'tile' or key == 'orientation':
                        continue
                    rev_border = border_str[::-1]
                    if border_str in borders or rev_border in borders:                            
                        match_id = borders[border_str]
                        tiles_with_match[tile_id].append(match_id)
                        tiles_with_match[match_id].append(tile_id)
                    else:
                        borders[border_str] = tile_id
                        borders[rev_border] = tile_id
                tile = []
            else: # append tile row)
                tile_row = [pixel for pixel in line]
                tile.append(tile_row)
            linenum += 1
        # pprint(tiles)
        # pprint(tiles_with_match)
    return (tiles, borders, tiles_with_match)

example = parseInput('example.txt')
# input = parseInput('input.txt')

def findAndMultipleCorners(tiles_with_match):
    pprint(tiles_with_match)
    corners = []
    prod = 1
    for tile, match_list in tiles_with_match.items():
        if len(match_list) == 2:
            corners.append(tile)
            prod *= int(tile)
    print(prod)
    return corners

corners = findAndMultipleCorners(example[2])
        
print(corners)