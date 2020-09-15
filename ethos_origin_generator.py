#!/usr/bin/env python
import random
from random import choices

ethos_ranges_and_antipodes = [
    ['militarist', 'pacifist', (0, 16)], # ethos, its antipode, its number range
    ['xenophobe', 'xenophile', (16, 32)],
    ['egalitarian', 'authoritarian', (32, 48)],
    ['materialist', 'spiritualist', (48, 64)],
    ['pacifist', 'militarist', (64, 80)],
    ['xenophile', 'xenophobe', (80, 96)],
    ['authoritarian', 'egalitarian', (96, 112)],
    ['spiritualist', 'materialist', (112, 125)],
]

def generate():
    gestalt = random.random() < 3/20 # 3 out of 20 chance for gestalt
    points = 3
    ethos = {'militarist': 0,
             'xenophobe': 0,
             'egalitarian': 0,
             'materialist': 0,
             'pacifist': 0,
             'xenophile': 0,
             'authoritarian': 0,
             'spiritualist': 0,
             'hive-mind': 0,
             'machine intelligence': 0}

    while points > 0:
        number = random.randint(1, 125)
        if gestalt:
            if number < 64:
                ethos['hive-mind'] += 1
            else:
                ethos['machine intelligence'] += 1
            break
        for e, antipode, (num_min, num_max) in ethos_ranges_and_antipodes:
            if num_min < number <= num_max and ethos[e] < 2 and ethos[antipode] == 0:
                ethos[e] += 1
                points -= 1
                continue

    chances = {}

    chances['Void Dwellers'] = 0 if gestalt else 0.25 if ethos['authoritarian'] and (ethos['materialist'] or ethos['militarist']) else 0.5
    chances['Shattered Ring'] = 0 if ethos['machine intelligence'] or ethos['materialist'] or ethos['authoritarian'] or ethos['militarist'] else 0.1
    chances['On the Shoulders of Giants'] = 0 if gestalt else 1
    chances['Doomsday'] = 1.5 if ethos['militarist'] else 0 if ethos['machine intelligence'] else 0.75
    chances['Remnants'] = 0.25 * ethos['xenophile'] if ethos['xenophile'] else 0.25 * ethos['xenophobe'] if ethos['xenophobe'] else 0.75 if ethos['materialist'] else 1
    chances['Post-Apocalyptic'] = 1
    chances['Life-Seeded'] = 0 if ethos['machine intelligence'] else 1
    chances['Resource Consolidation'] = 3 if ethos['machine intelligence'] else 0
    chances['Tree Of Life'] = 1 if ethos['hive-mind'] else 0
    chances['Syncretic Evolution'] = 0 if gestalt or ethos['egalitarian'] else 2 if ethos['authoritarian'] else 1
    chances['Mechanist'] = 0.25 * ethos['materialist']
    chances['Calamitous Birth'] = 0 if ethos['machine intelligence'] else 1
    chances['Prosperous Unification'] = 1
    chances['Galactic Doorstep'] = 1

    scaled_chances = {k: v/max(chances.values()) for k, v in chances.items()}
    scaled_chances_2 = {k: v/sum(chances.values()) for k, v in scaled_chances.items()}

    origin = choices(population=list(scaled_chances_2.keys()),
              weights=list(chances.values()), k=1)[0]
    return ethos, origin, gestalt

def main():
    ethos, origin, gestalt = generate()
    print(f'Origin: {origin}')
    print()
    print('Ethoses:')
    for name, points in ethos.items():
      if points:
        print(f'{name}: {points}')
    print(f'Gestalt: {gestalt}')

if __name__ == '__main__':
    main()
