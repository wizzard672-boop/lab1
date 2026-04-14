#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

print(distances)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {}

# Ручное вычисление всех пар
moscow_london = ((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5
moscow_paris = ((550 - 480) ** 2 + (370 - 480) ** 2) ** 0.5
london_paris = ((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = london_paris

print(distances)
# Пример вывода: {'Moscow': {'London': 145.602, 'Paris': 131.529}, ...}

