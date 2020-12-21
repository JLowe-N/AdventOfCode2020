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
                    'row_top': "".join(tile[0, :]),
                    'row_bottom': "".join(tile[-1, :]),
                    'col_left': "".join(tile[:, 0]),
                    'col_right': "".join(tile[:, -1]),
                    }
                tile_dict['tile'] = tile[1:-1, 1:-1]
                tiles[tile_id] = tile_dict
                for key, border_str in tiles[tile_id].items():
                    if key == 'tile' or key == 'orientation':
                        continue
                    rev_border = border_str[::-1]
                    if border_str in borders or rev_border in borders:
                        if rev_border in borders:
                            if key.startswith('row'):
                                tile_dict['tile'] = np.fliplr(tile_dict['tile'])
                                tile_dict['row_top'] = tile_dict['row_top'][::-1]
                                tile_dict['row_bottom'] = tile_dict['row_bottom'][::-1]
                                tile_dict['col_left'], tile_dict['col_right'] = tile_dict['col_right'], tile_dict['col_left']
                            elif key.startswith('col'):
                                tile_dict['tile'] = np.flipud(tile_dict['tile'])
                                tile_dict['col_left'] = tile_dict['col_left'][::-1]
                                tile_dict['col_right'] = tile_dict['col_right'][::-1]
                                tile_dict['row_top'], tile_dict['row_bottom'] = tile_dict['row_bottom'], tile_dict['row_top']
                            match_id = borders[rev_border]
                            tiles[tile_id] = tile_dict
                        else:
                            match_id = borders[border_str]
                        tiles_with_match[tile_id].append(match_id)
                        tiles_with_match[match_id].append(tile_id)
                    else:
                        borders[border_str] = tile_id
                
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

def flipHorizontal(tile_dict):
    tile_dict['tile'] = np.fliplr(tile_dict['tile'])
    tile_dict['row_top'] = tile_dict['row_top'][::-1]
    tile_dict['row_bottom'] = tile_dict['row_bottom'][::-1]
    tile_dict['col_left'], tile_dict['col_right'] = tile_dict['col_right'], tile_dict['col_left']

def flipVertical(tile_dict):
    tile_dict['tile'] = np.flipud(tile_dict['tile'])
    tile_dict['col_left'] = tile_dict['col_left'][::-1]
    tile_dict['col_right'] = tile_dict['col_right'][::-1]
    tile_dict['row_top'], tile_dict['row_bottom'] = tile_dict['row_bottom'], tile_dict['row_top']

def rotateCorners(tiles, tiles_with_match, corners):
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None
    for corner in corners:
        matching_sides= []
        corner_dict = tiles[corner]
        matchingTiles = tiles_with_match[corner]
        # pprint(corner_dict)
        for key, border_str in corner_dict.items():
            if key == 'tile':
                continue
            for matchkey in matchingTiles:
                match_dict = tiles[matchkey]
                for match_dict_key, match_str in match_dict.items():
                    if match_dict_key == 'tile':
                        continue
                    if border_str == match_str:
                        matching_sides.append(key)
                        print(f'corner {corner} has {key} and match {matchkey} has {match_dict_key}')
                        print(matchkey)
                        print(match_dict_key)
        print(matching_sides)
        if 'row_top' in matching_sides and 'col_right' in matching_sides:
            bottom_left = corner
        elif 'row_top' in matching_sides and 'col_left' in matching_sides:
            bottom_right = corner
        elif 'row_bottom' in matching_sides and 'col_left' in matching_sides:
            top_right = corner
        elif 'row_bottom' in matching_sides and 'col_right' in matching_sides:
            top_left = corner
    corner_assignments = [top_left, top_right, bottom_left, bottom_right]
    print(corner_assignments)
    return corner_assignments
                        
            
            
rotateCorners(example[0], example[2], corners)

def assembleImage(tiles, borders, corners, tiles_with_match):
    img = []
    img_row = []
    corners_stack = corners
    current_corner = corners_stack.pop()
    img_row.append(current_corner)
    possibleMatches = tiles_with_match[img_row[-1]]
    for i in range(3):
        if len(img_row) == 2:
            break
        if i == 1:
            pass

        for match in possibleMatches:
            currentTile = tiles[img_row[-1]]
            currentRight = currentTile['col_right']
            leftMatch = tiles[match]['col_left']
            print(f'testing {leftMatch} against {currentRight}')
            if currentRight == leftMatch:
                img_row.append(match)
    if len(img_row) != 2:
        tile_dict = currentTile
        tile_dict['tile'] = np.flipud(tile_dict['tile'])
        tile_dict['col_left'] = tile_dict['col_left'][::-1]
        tile_dict['col_right'] = tile_dict['col_right'][::-1]
        tile_dict['row_top'], tile_dict['row_bottom'] = tile_dict['row_bottom'], tile_dict['row_top']

    while img_row[-1] not in corners_stack:
        currentTile = tiles[img_row[-1]]
        currentRight = currentTile['col_right']
        possibleMatches = tiles_with_match[img_row[-1]]
        for match in possibleMatches:
            leftMatch = tiles[match]['col_left']
            print(f'testing {leftMatch} against {currentRight}')
            if currentRight == leftMatch:
                img_row.append(match)
                break
        print('Not found!')
    img.append(img_row)
    pprint(img)
    while len(img) * len(img[0]) != len(tiles):
        while len(img_row) != 4:
            upper_tile = img[-1][len(img_row)]
            bottom_to_match = upper_tile['row_bottom']
            possibleMatches = tiles_with_match[upper_tile]
            for match in possibleMatches:
                top_match = tiles[match]['row_top']
                if bottom_to_match == top_match:
                    img_row.append(match)
                    break
        img.append(img_row)
    pprint(img)
        
        
# assembleImage(example[0], example[1], corners, example[2])