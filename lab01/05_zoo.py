#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# Медведь между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавить птиц
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

# Убрать слона
zoo.remove('elephant')
print(zoo)

# Позиции (для обычного человека счет с 1)
lion_pos = zoo.index('lion') + 1
lark_pos = zoo.index('lark') + 1
print('Лев сидит в клетке номер', lion_pos)
print('Жаворонок сидит в клетке номер', lark_pos)