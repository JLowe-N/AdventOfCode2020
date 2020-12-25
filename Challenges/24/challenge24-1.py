import re

def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            line = re.split(r'([sn]?[we])', line)
            line = [match for match in line if match != '']
            # print(line)
            data.append(line)
            linenum += 1
    return data

class HexTile:
    def __init__(self, hex_x, hex_y, isBlack = False):
        self.hex_x = hex_x
        self.hex_y = hex_y
        self.black = isBlack

class TileGrid:
    def __init__(self, reference_tile):
        self.black_count = 0
        self.reference_tile = reference_tile
        self.tiles = {} # only black tiles

    def flipTile(self, tile):
        tile.black = not tile.black
        if tile.black == True:
            self.black_count += 1
        else:
            self.black_count -= 1

    def follow_then_flip(self, hex_path):
        # From reference
        hex_x = 0
        hex_y = 0
        for direction in hex_path:
            if direction == 'nw':
                hex_x -= 0.5
                hex_y -= 1
            elif direction == 'ne':
                hex_x += 0.5
                hex_y -= 1
            elif direction == 'w':
                hex_x -= 1
            elif direction == 'e':
                hex_x += 1
            elif direction == 'sw':
                hex_x -= 0.5
                hex_y += 1
            elif direction == 'se':
                hex_x += 0.5
                hex_y += 1
        if (hex_x, hex_y) not in self.tiles:
            self.tiles[(hex_x, hex_y)] = HexTile(hex_x, hex_y, True)
            self.black_count += 1
        else:
            self.tiles.pop((hex_x, hex_y), None)
            self.black_count -= 1

    def livingTiles(self):
        self.black_count = 0
        new_black_tiles = {}  # copy
        visited = {}
        tiles_to_visit = []
        vectors = [(-0.5, -1), (0.5, -1), (-1, 0), (1, 0), (-0.5, 1), (0.5, 1)]
        # Add all neighbors to check first
        for tile in self.tiles.values():
            hex_x = tile.hex_x
            hex_y = tile.hex_y
            tiles_to_visit.append((hex_x, hex_y))
            for (vec_x, vec_y) in vectors:
                new_x, new_y = hex_x + vec_x, hex_y + vec_y
                if (new_x, new_y) not in tiles_to_visit:
                    tiles_to_visit.append((new_x, new_y))
        
        # Now begin visiting, seeing if a flip should occur
        current_position = None
        while len(tiles_to_visit) > 0:
            current_position = tiles_to_visit.pop()
            if current_position in visited:
                continue
            hex_x, hex_y = current_position
            visited[current_position] = True

            blacktile_neighbors = 0
            for vector in vectors:
                neighbor_hex_x, neighbor_hex_y = hex_x + vector[0], hex_y + vector[1]
                if (neighbor_hex_x, neighbor_hex_y) in self.tiles:
                    blacktile_neighbors += 1

            if current_position in self.tiles:
                isBlack = True
            else:
                isBlack = False
        
            if isBlack:
                if blacktile_neighbors == 0 or blacktile_neighbors > 2:
                    continue # Tile flips to white / not added to black tiles dict
                else:
                    new_black_tiles[(hex_x, hex_y)] = HexTile(hex_x, hex_y, True)
                    self.black_count += 1
            else: # isWhite
                if blacktile_neighbors == 2:
                    new_black_tiles[(hex_x, hex_y)] = HexTile(hex_x, hex_y, True)
                    self.black_count += 1
                else:
                    continue # Tile will be white, not be added to black tiles dict
        self.tiles = new_black_tiles
        # print(len(self.tiles))
                
                    


            




example = parseInput('example.txt')
example2 = parseInput('example2.txt')
input = parseInput('input.txt')

myTiles = TileGrid(HexTile(0, 0))
for step, path in enumerate(input):
    # print(f'Tile {step}')
    myTiles.follow_then_flip(path)
for key, tile in myTiles.tiles.items():
    if tile.black == False:
        myTiles.tiles.pop(key, None)

for i in range(100):
    myTiles.livingTiles()
    print(F'Day {i + 1}: {myTiles.black_count}')

print(myTiles.black_count)

