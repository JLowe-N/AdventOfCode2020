from pprint import pprint
from functools import reduce

def parseInput(filename):
    food = []
    allergens_in_lines = {}
    unique_ingredients = set()
    foreign_allergens = set()
    foreign_safe = set()
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.rstrip('\n')
            ingredients, allergens = line.split('(')
            ingredients = ingredients.rstrip(' ').split(' ')
            allergens = allergens[len('contains '):].rstrip(')').split(', ')
            food.append({'ingredients': ingredients, 'allergens': allergens})
            for allergen in allergens:
                if allergen not in allergens_in_lines:
                    allergens_in_lines[allergen] = []
                allergens_in_lines[allergen].append(linenum)
            for ingredient in ingredients:
                unique_ingredients.add(ingredient)
            # pprint(ingredients)
            # pprint(allergens)
            linenum += 1

    possible_allergen_translations = {}
    to_remove = []
    for allergen, lines_with_allergen in allergens_in_lines.items():
        foreign_word_set = set()
        for line in lines_with_allergen:
            # print(foreign_word_set)
            foreign_words = set(food[line]['ingredients'])
            if len(foreign_word_set) == 0:
                foreign_word_set = foreign_words
            else:
                foreign_word_set = foreign_word_set.intersection(foreign_words)      
        possible_allergen_translations[allergen] = list(foreign_word_set)
        to_remove.append(list(foreign_word_set))

    while len(to_remove) > 0:
        to_remove.sort(key=len)   
        print(to_remove[0])
        target_removal = to_remove.pop(0)[0]  
        for value_list in to_remove:
            if target_removal is not None and target_removal in value_list:
                    value_list.remove(target_removal)
                    pprint(value_list)
        for value_list in possible_allergen_translations.values():
            if len(value_list) > 1:
                if target_removal is not None and target_removal in value_list:
                    value_list.remove(target_removal)
                    pprint(value_list)
        
    pprint(possible_allergen_translations)
    for value in possible_allergen_translations.values():
        foreign_allergens.add(value[0])

    foreign_safe = unique_ingredients.difference(foreign_allergens)

    return (food, allergens_in_lines, linenum, foreign_allergens, foreign_safe, possible_allergen_translations)




# example = parseInput('example.txt')
input = parseInput('input.txt')



safe_count = 0
for item in input[0]:
    ingredient_list = item['ingredients']
    for ingredient in ingredient_list:
        if ingredient not in input[3]:
            safe_count += 1
print(safe_count)

alphabetical_allergen_order = [key for key in input[5]]
alphabetical_allergen_order.sort()
print(alphabetical_allergen_order)
ordered_foreign_allergens = [input[5][key][0] for key in alphabetical_allergen_order]

print(",".join(ordered_foreign_allergens))


            
# count_non_allergens = len(input[3]) - len(input[4])
# print(count_non_allergens)

def myFunc(startTime, busList):
    pass


print(myFunc)