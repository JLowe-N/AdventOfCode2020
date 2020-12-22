from pprint import pprint
import numpy as np
import sys

from numpy.testing._private.utils import measure

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
                    'matching_sides': []
                    }
                tile_dict['tile'] = tile[1:-1, 1:-1]
                tiles[tile_id] = tile_dict
                for key, border_str in tiles[tile_id].items():
                    if key == 'tile' or key == 'matching_sides':
                        continue
                    rev_border = border_str[::-1]
                    if border_str in borders or rev_border in borders:
                        tile_dict['matching_sides'].append(key)
                        tiles[tile_id] = tile_dict
                        if rev_border in borders:
                            match_id = borders[rev_border]
                        else:
                            match_id = borders[border_str]
                        matching_tile = tiles[match_id]
                        matching_side = None
                        for match_key, match_side in matching_tile.items():
                            if match_key == 'tile' or match_key == 'matching_sides':
                                continue
                            if match_side == border_str or match_side == rev_border:
                                matching_side = match_key
                        matching_tile['matching_sides'].append(matching_side)
                        tiles[match_id] = matching_tile
                        tiles_with_match[tile_id].append(match_id)
                        tiles_with_match[match_id].append(tile_id)
                    else:
                        borders[border_str] = tile_id
                tile = []
            else: # append tile row)
                tile_row = [pixel for pixel in line]
                tile.append(tile_row)
            linenum += 1
        # pprint(tiles_with_match)
    return (tiles, borders, tiles_with_match)

# example = parseInput('example.txt')
input = parseInput('input.txt')

def findAndMultipleCorners(tiles_with_match):

    corners = []
    prod = 1
    for tile, match_list in tiles_with_match.items():
        if len(match_list) == 2:
            corners.append(tile)
            prod *= int(tile)
    print(prod)
    return corners

corners = findAndMultipleCorners(input[2])

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

def rotateLeft(tile_dict):
    tile_dict['tile'] = np.rot90(tile_dict['tile'])
    new_top = tile_dict['col_right']
    new_left = tile_dict['row_top']
    new_bottom = tile_dict['col_left']
    new_right = tile_dict['row_bottom']
    tile_dict['row_top'] = new_top
    tile_dict['col_left'] = new_left
    tile_dict['row_bottom'] = new_bottom
    tile_dict['col_right'] = new_right
    tile_dict['col_left'] = tile_dict['col_left'][::-1]
    tile_dict['col_right'] = tile_dict['col_right'][::-1]


def rotateCorners(tiles, tiles_with_match, corners):
    return
    top_left = '1699'
    for corner in corners:
        corner_dict = tiles[corner]
        print(f'{corner} has matches on {tiles[corner]["matching_sides"]}') 
    corner_assignments = [top_left, top_right, bottom_left, bottom_right]
    print(corner_assignments)
    return corner_assignments
                        
            
            
rotateCorners(input[0], input[2], corners)

def assembleImage(tiles, borders, corners, tiles_with_match):
    img = []
    img_row = []
    corners_remaining = ['1699', '3229', '2351', '1433']
    img_row.append('1699') # top-left
    corners_remaining.remove('1699')
    while len(corners_remaining) > 0:
        # first_row
        if len(img) == 0:
            right_side_to_match = tiles[img_row[-1]]['col_right']
            for possible_match in tiles_with_match[img_row[-1]]:
                possible_tile = tiles[possible_match]
                matched = False
                if not matched:
                    for i in range(16):
                        left_side_to_test = possible_tile['col_left']
                        if right_side_to_match == left_side_to_test:
                            img_row.append(possible_match)
                            matched = True
                            break
                        if i % 4 == 0:
                            flipHorizontal(possible_tile)
                        elif i % 4 == 1:
                            flipVertical(possible_tile)
                        elif i % 4 == 2:
                            flipHorizontal(possible_tile)
                        elif i % 4 == 3:
                            flipVertical(possible_tile)
                            rotateLeft(possible_tile)

                        
        # subsequent rows
        else:
            # first column
            if len(img_row) == 0:
                bottom_side_to_match = tiles[img[-1][0]]['row_bottom']
                for possible_match in tiles_with_match[img[-1][0]]:
                    possible_tile = tiles[possible_match]
                    matched = False
                    if not matched:
                        for i in range(16):
                            top_side_to_test = possible_tile['row_top']
                            if bottom_side_to_match == top_side_to_test:
                                img_row.append(possible_match)
                                matched = True
                                break
                            if i % 4 == 0:
                                flipHorizontal(possible_tile)
                            elif i % 4 == 1:
                                flipVertical(possible_tile)
                            elif i % 4 == 2:
                                flipHorizontal(possible_tile)
                            elif i % 4 == 3:
                                flipVertical(possible_tile)
                                rotateLeft(possible_tile)
                                # print('could not find match')
                        
            # rest of columns
            else:
                bottom_side_to_match = tiles[img[-1][len(img_row)]]['row_bottom']
                right_side_to_match = tiles[img_row[-1]]['col_right']
                for possible_match in tiles_with_match[img_row[-1]]:
                    possible_tile = tiles[possible_match]
                    matched = False
                    if not matched:
                        for i in range(16):
                            top_side_to_test = possible_tile['row_top']
                            left_side_to_test = possible_tile['col_left']
                            if bottom_side_to_match == top_side_to_test and right_side_to_match == left_side_to_test:
                                img_row.append(possible_match)
                                matched = True
                                break
                            if i % 4 == 0:
                                flipHorizontal(possible_tile)
                            elif i % 4 == 1:
                                flipVertical(possible_tile)
                            elif i % 4 == 2:
                                flipHorizontal(possible_tile)
                            elif i % 4 == 3:
                                flipVertical(possible_tile)
                                rotateLeft(possible_tile)

        # reset after row length hit
        # if len(img_row) > 0 and img_row[-1] in corners_remaining:
        if len(img_row) > 0:
            if img_row[-1] in corners_remaining:
                corners_remaining.remove(img_row[-1])
        if len(img_row) == 12:
                img.append(img_row)
                img_row = []
        # print(img)
        # print(img_row)
    print('Rows:')
    print(len(img))
    print('Cols:')
    print(len(img[0]))
    print('Elements:')
    print(len(img[0]) * len(img))
    print('Pixels:')
    print(len(img[0]) * len(img)* 64)
    return img

def joinImgTiles(tiles, img_name_array):
    img = None
    for row in img_name_array:
        img_row = None

        for tile_id in row:
            tile = tiles[tile_id]['tile']
            if img_row is None:
                img_row = tile
            else:
                img_row = np.concatenate((img_row, tile), axis=1)
        if img is None:
            img = img_row
        else:
            img = np.concatenate((img, img_row), 0)
    print('Processed img pixels:')
    print(img.size)
    return img

test_img = '''.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###'''

test_img = [[char for char in line] for line in test_img.split('\n')]
test_img = np.asarray(test_img)
print(test_img)

def countSeaMonsters(img):
    sea_monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.lstrip('\n').split('\n')
    sea_monster = [[char for char in line] for line in sea_monster]
    sea_monster = np.asarray(sea_monster)
    monster_targets = np.count_nonzero(sea_monster == '#')
    print(monster_targets)
    sea_monster_count = 0
    for iter in range(8):
        i = 0
        j = 0
        monster_x_length = sea_monster.shape[1]
        # print("monster cols")
        # print(monster_x_length)
        monster_y_length = sea_monster.shape[0]
        # print("monster rows")
        # print(monster_y_length)
        while i < img.shape[0] - monster_y_length:
            j = 0
            while j < img.shape[1] - monster_x_length:
                sea_to_search = img[i: i+monster_y_length, j: j+monster_x_length]
                targets_found = 0
                for a in range(monster_y_length):
                    for b in range(monster_x_length):
                        # print(f'{a} {b} {sea_monster[a,b]} {sea_to_search[a,b]}')
                        if sea_monster[a, b] == '#':
                            if sea_to_search[a, b] == '#':
                                targets_found += 1
                # print(targets_found)
                if targets_found == monster_targets:
                    print(sea_monster)
                    print(sea_to_search)
                    sea_monster_count += 1
                # elif targets_found > monster_targets:
                #     print("Whoops!")
                # # elif targets_found >= 10:
                # #     print(sea_to_search)
                # else:
                #     print(f'targets found: {targets_found}')
                
                j += 1
            i += 1
        # after i & j finish, we have scanned the sea with 1 monster possibility
        # rotate the monster before next scan
        # if iter % 4 == 0:
        #     sea_monster = np.fliplr(sea_monster)
        # elif iter % 4 == 1:
        #     sea_monster = np.flipud(sea_monster)
        # elif iter % 4 == 2:
        #     sea_monster = np.fliplr(sea_monster)
        # elif iter % 4 == 3:
        #     sea_monster = np.flipud(sea_monster)
        #     sea_monster = np.rot90(sea_monster)
        # repeat the iter loop

        # rotate the image before the next scan
        if iter % 4 == 0:
            img = np.fliplr(img)
        elif iter % 4 == 1:
            img = np.flipud(img)
        elif iter % 4 == 2:
            img = np.fliplr(img)
        elif iter % 4 == 3:
            img = np.flipud(img)
            img = np.rot90(img)

    print(f'sea monsters: {sea_monster_count}')
    return sea_monster_count

def measure_water_roughness(img, sea_monster_count):
    sea_monster_tiles = 15
    total_monster_tiles = sea_monster_tiles * sea_monster_count
    potential_roughness = np.count_nonzero(img == '#')
    return potential_roughness - total_monster_tiles
    
img_name_array = assembleImage(input[0], input[1], corners, input[2])
print(img_name_array)
img = joinImgTiles(input[0], img_name_array)
sea_monster_count = countSeaMonsters(img)
print(measure_water_roughness(img, sea_monster_count))
